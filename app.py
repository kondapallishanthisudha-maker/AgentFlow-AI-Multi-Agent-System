
import streamlit as st

st.set_page_config(
    page_title="Multi-Agent AI Platform",
    page_icon="@",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .main-title {
        font-size: 38px;
        font-weight: 700;
        text-align: center;
        margin-bottom: 5px;
    }

    .sub-title {
        text-align: center;
        color: #808080;
        font-size: 17px;
        margin-bottom: 30px;
    }

    .project-card {
        padding: 22px;
        border-radius: 12px;
        border: 1px solid rgba(128,128,128,0.3);
        min-height: 155px;
        margin-bottom: 15px;
    }

    .project-card h3 {
        margin-top: 0;
    }

    .footer {
        text-align: center;
        color: #808080;
        padding: 20px;
        font-size: 14px;
    }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.title(" Multi-Agent AI")
    st.caption("Powered by AutoGen + Gemini")

    st.divider()

    st.markdown("### Navigation")
    st.markdown(
        "Select an application from the pages listed above."
    )

    st.divider()

    st.markdown("### Technologies")
    st.markdown("""
    - Python
    - Microsoft AutoGen
    - Google Gemini API
    - Streamlit
    - AsyncIO
    """)

    st.divider()

    st.caption("Developed by SHANTHI SUDHA")

st.markdown(
    '<div class="main-title"> Multi-Agent AI Collaboration Platform</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">An Intelligent Platform for Autonomous AI Agents and LLM Applications</div>',
    unsafe_allow_html=True
)

st.divider()

# ==========================================
# WELCOME SECTION
# ==========================================

st.header("👋 Welcome!")

st.write("""
Explore an AI-powered platform built using Microsoft's AutoGen
framework and Google's Gemini API.

This platform demonstrates how single AI agents and multiple
collaborating agents can solve different real-world tasks.
""")

st.subheader(" Platform Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="AI Applications",
        value="5"
    )

with col2:
    st.metric(
        label="LLM Provider",
        value="Gemini"
    )

with col3:
    st.metric(
        label="Agent Framework",
        value="AutoGen"
    )

st.divider()

st.header(" Explore Applications")

st.write("Choose an application from the Streamlit sidebar.")

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
    <div class="project-card">
        <h3>📅 Morning Planning System</h3>
        <p>Multiple AI agents coordinate school drop-offs
        and office schedules while considering deadlines.</p>
        <b>Module:</b> AG_Father.py
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="project-card">
        <h3>👥 Multi-Agent Collaboration</h3>
        <p>Multiple agents collaborate to solve tasks
        through coordinated conversations.</p>
        <b>Module:</b> AG_Multiagent.py
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="project-card">
        <h3>🎓 AI Technical Mentor</h3>
        <p>A single AI agent explains technical concepts
        using simple real-world examples.</p>
        <b>Module:</b> ag_single_agent.py
    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown("""
    <div class="project-card">
        <h3>💻 AI Code Development Team</h3>
        <p>Analyst, Developer and Reviewer agents
        collaborate to develop and review code.</p>
        <b>Module:</b> ag_multiagents.py
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="project-card">
        <h3>🔌 Gemini API Integration</h3>
        <p>Connect and interact with Google's Gemini
        models through AutoGen.</p>
        <b>Module:</b> AG_Gemini.py
    </div>
    """, unsafe_allow_html=True)

st.divider()


# ARCHITECTURE

st.header(" Platform Architecture")

st.code("""
             USER
               |
               v
        STREAMLIT FRONTEND
               |
               v
        AUTOGEN FRAMEWORK
               |
       +-------+-------+
       |       |       |
       v       v       v
     Agent   Agent   Agent
       |       |       |
       +-------+-------+
               |
               v
          GEMINI API
               |
               v
        AI GENERATED OUTPUT
""", language="text")

# FOOTER

st.divider()

st.markdown("""
<div class="footer">
    Multi-Agent AI Collaboration Platform<br>
    Built with Python | AutoGen | Google Gemini | Streamlit<br>
    Developed by SHANTHI SUDHA
</div>
""", unsafe_allow_html=True)
