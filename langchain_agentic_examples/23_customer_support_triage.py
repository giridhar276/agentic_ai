'''
Customer Support Triage

Triage agent checks severity
Routing agent chooses the team
Supervisor combines both responses

Key concept:
Specialized agent collaboration
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

triage_agent = create_agent(
    model,
    system_prompt="You are a support triage agent. Classify severity as Low, Medium, or High."
)

routing_agent = create_agent(
    model,
    system_prompt="You are a support routing agent. Choose one team: Network, Billing, Platform, Security."
)

def ask_triage(ticket: str) -> str:
    """Ask the triage agent to assess severity."""
    result = triage_agent.invoke({
        "messages": [{"role": "user", "content": f"Assess severity for this ticket: {ticket}"}]
    })
    return result["messages"][-1].content

def ask_routing(ticket: str) -> str:
    """Ask the routing agent to pick the correct team."""
    result = routing_agent.invoke({
        "messages": [{"role": "user", "content": f"Choose the best team for this ticket: {ticket}"}]
    })
    return result["messages"][-1].content

supervisor = create_agent(model, tools=[ask_triage, ask_routing])

ticket = "Client production API is down after deployment and users cannot log in."

result = supervisor.invoke({
    "messages": [
        {"role": "user", "content": f"Review this support ticket and give final triage decision: {ticket}"}
    ]
})

print(result["messages"][-1].content)
