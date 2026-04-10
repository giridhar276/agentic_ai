'''
Incident Commander Team

Log agent finds the likely issue
Communication agent drafts the update
Incident commander combines both

Key concept:
Coordination across specialist agents
'''

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in environment or .env file")

model = ChatOpenAI(model="gpt-4.1-mini", temperature=0, api_key=api_key)

log_agent = create_agent(
    model,
    system_prompt="You are a log analysis agent. Find the likely technical issue."
)

comm_agent = create_agent(
    model,
    system_prompt="You are a crisis communication agent. Draft a short business update."
)

def analyze_logs(log_text: str) -> str:
    """Analyze logs and return likely issue."""
    result = log_agent.invoke({
        "messages": [{"role": "user", "content": f"Analyze these logs: {log_text}"}]
    })
    return result["messages"][-1].content

def draft_update(issue: str) -> str:
    """Create a simple status update for stakeholders."""
    result = comm_agent.invoke({
        "messages": [{"role": "user", "content": f"Draft a short business update for this issue: {issue}"}]
    })
    return result["messages"][-1].content

incident_commander = create_agent(model, tools=[analyze_logs, draft_update])

logs = "ERROR database connection timeout after deployment. Login service unhealthy. Multiple 500 errors."

result = incident_commander.invoke({
    "messages": [
        {"role": "user", "content": f"Handle this incident and give technical issue plus stakeholder update: {logs}"}
    ]
})

print(result["messages"][-1].content)
