import asyncio
import os
from typing import AsyncGenerator, Any

import streamlit as st
from dotenv import load_dotenv

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination
from autogen_ext.models.openai import OpenAIChatCompletionClient


st.set_page_config(
    page_title="Autogen Multi-Agent Chat created by SHANTHI SUDHA",
    page_icon="🤖",
    layout="wide",
)

st.title("🤖 Autogen Multi-Agent Chat created by SHANTHI SUDHA")


load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

st.sidebar.header("🔑 API Key Configuration")

api_key = st.sidebar.text_input(
    "Enter your Gemini API Key",
    type="password",
    value=gemini_api_key if gemini_api_key else "",
)


task_description = """
It is 7:30 AM at home.

Father has 3 responsibilities to complete before leaving for work.

1. Kid 1 needs to go to School A.
   Kid 1 must arrive by 8:00 AM.

2. Kid 2 needs to go to School B.
   Kid 2 must arrive by 8:15 AM.

3. Father needs to reach the office.
   Father must arrive by 9:00 AM.

Create a coordinated plan that ensures all three deadlines
are completed on time.
"""

st.info(f"**Task:**\n\n{task_description}")


async def get_team_stream(
    task: str,
    key: str
) -> AsyncGenerator[Any, None]:

    model_client = OpenAIChatCompletionClient(
        model="gemini-3-flash-preview",
        api_key=key,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
        model_info={
            "vision": True,
            "function_calling": True,
            "json_output": True,
            "family": "gemini",
        },
    )

    agent1 = AssistantAgent(
        name="School_Agent_1",
        model_client=model_client,
        system_message="""
You are School Agent 1.

Your responsibility is ONLY to transport Kid 1 to School A.

Requirements:
- Current time is 7:30 AM.
- Kid 1 must arrive at School A by 8:00 AM.
- Create a specific schedule with departure time,
  arrival time, and drop-off time.
- Include a reasonable time buffer.

Do NOT handle:
- Kid 2
- School B
- Father's office commute

After providing your plan, stop and wait for the next agent.
""",
    )

    agent2 = AssistantAgent(
        name="School_Agent_2",
        model_client=model_client,
        system_message="""
You are School Agent 2.

Your responsibility is ONLY to transport Kid 2 to School B.

Requirements:
- Current time is 7:30 AM.
- Kid 2 must arrive at School B by 8:15 AM.
- Create a specific schedule with departure time,
  arrival time, and drop-off time.
- Include a reasonable time buffer.

Do NOT handle:
- Kid 1
- School A
- Father's office commute

After providing your plan, stop and wait for the next agent.
""",
    )

    agent3 = AssistantAgent(
        name="Office_Agent",
        model_client=model_client,
        system_message="""
You are the Office Agent.

Your responsibility is to create the final coordinated plan.

Review the plans provided by:
1. School Agent 1
2. School Agent 2

Father must reach the office by 9:00 AM.

Your final plan must verify:

1. Kid 1 reaches School A by 8:00 AM.
2. Kid 2 reaches School B by 8:15 AM.
3. Father reaches the office by 9:00 AM.

Make sure the schedule is logically coordinated.

If all three deadlines are satisfied,
finish your response with EXACTLY:

ALL TASK COMPLETED TERMINATE

Do not continue after this statement.
""",
    )

    termination = TextMentionTermination("TERMINATE")

    team = RoundRobinGroupChat(
        participants=[
            agent1,
            agent2,
            agent3,
        ],
        termination_condition=termination,
        max_turns=3,
    )

    try:
        async for message in team.run_stream(task=task):
            yield message

    finally:
        await model_client.close()


if "messages" not in st.session_state:
    st.session_state.messages = []


for msg in st.session_state.messages:
    with st.chat_message(msg["source"]):
        st.write(msg["content"])


if st.sidebar.button(
    "🚀 Start Planning",
    type="primary"
):

    if not api_key:
        st.error("❌ Please enter a valid Gemini API Key.")

    else:
        st.session_state.messages = []

        async def run_workflow():

            with st.status(
                "🤖 Planning in progress...",
                expanded=True
            ) as status:

                try:

                    async for message in get_team_stream(
                        task_description,
                        api_key
                    ):

                        source = getattr(
                            message,
                            "source",
                            "System"
                        )

                        content = getattr(
                            message,
                            "content",
                            ""
                        )

                        if not content:
                            continue

                        if not isinstance(content, str):
                            content = str(content)

                        st.session_state.messages.append(
                            {
                                "source": source,
                                "content": content,
                            }
                        )

                        with st.chat_message(source):
                            st.write(content)

                    status.update(
                        label="✅ Planning Completed!",
                        state="complete",
                        expanded=False,
                    )

                except Exception as e:

                    status.update(
                        label="❌ Error occurred",
                        state="error",
                        expanded=True,
                    )

                    st.error(
                        f"Execution Error: {e}"
                    )

        asyncio.run(run_workflow())