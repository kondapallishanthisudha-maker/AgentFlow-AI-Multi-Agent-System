
import asyncio
import os
from dotenv import load_dotenv

from autogen_core.models import UserMessage, ModelInfo
from autogen_ext.models.openai import OpenAIChatCompletionClient

load_dotenv()


async def main():

    # Get Gemini API key
    gemini_api_key = os.getenv("GEMINI_API_KEY")

    if not gemini_api_key:
        raise ValueError("GEMINI_API_KEY is not found in .env file")

    # Gemini model capabilities
    gemini_model_info = ModelInfo(
        vision=True,
        function_calling=True,
        json_output=True,
        family="unknown",
        structured_output=True
    )

    # Create Gemini model client
    model_client = OpenAIChatCompletionClient(
        model="gemini-3-flash-preview",
        api_key=gemini_api_key,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
        model_info=gemini_model_info
    )

    try:
        # Send message to Gemini
        response = await model_client.create([
            UserMessage(
                content="Hello, Gemini! Can you help me with a task?",
                source="user"
            )
        ])

        print("\nResponse:\n")
        print(response.content)

    finally:
        await model_client.close()


if __name__ == "__main__":
    asyncio.run(main())




              