
# Multi-Agent AI System

An AI-powered multi-agent application built using Python, Microsoft AutoGen, Google Gemini API, and Streamlit.

The project demonstrates how multiple AI agents can collaborate, communicate, and solve different tasks through structured workflows.

## Features

- Gemini API integration
- Multi-agent collaboration
- Autonomous task planning
- Analyst, Developer, and Reviewer workflow
- AI Technical Mentor
- Morning Planning System
- Interactive Streamlit dashboard

## Tech Stack

- Python
- Microsoft AutoGen
- Google Gemini API
- Streamlit
- Python-dotenv
- Asyncio

## Project Structure

MultiAgent AI System/
│
├── app.py
├── .env
├── .gitignore
├── requirements.txt
├── README.md
│
├── pages/
│   ├── AG_Father.py
│   ├── AG_Gemini.py
│   ├── AG_Multiagent.py
│   ├── ag_multiagents.py
│   └── ag_single_agent.py
│
├── tests/
│   └── autogen_testing.py
│
└── myenv/

## Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd "MultiAgent AI System"
```

### 2. Create a virtual environment

```bash
python -m venv myenv
```

### 3. Activate the environment

Windows PowerShell:

```powershell
.\myenv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Gemini API

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=your_gemini_api_key
```

### 6. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## Project Modules

| Module | Description |
|---|---|
| AG_Father | Morning planning with multiple agents |
| AG_Gemini | Gemini API integration |
| AG_Multiagent | Multi-agent planning application |
| ag_multiagents | Analyst, Developer, and Reviewer collaboration |
| ag_single_agent | AI Technical Mentor |

## Security

- API keys are stored in environment variables.
- `.env` is excluded from Git using `.gitignore`.
- Never upload API keys or credentials to GitHub.

## Future Enhancements

- Agent memory management
- Tool-using autonomous agents
- Agent performance evaluation
- Human-in-the-loop approval
- Logging and monitoring

