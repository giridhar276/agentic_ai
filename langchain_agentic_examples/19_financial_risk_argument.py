'''
Risk Team vs Growth Team

Growth agent pushes for fast launch
Risk agent warns about problems
Judge agent gives balanced decision

Key concept:
Structured argument and resolution
'''

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in environment or .env file")

growth_agent = ChatOpenAI(model="gpt-4.1-mini", temperature=0.2, api_key=api_key)
risk_agent = ChatOpenAI(model="gpt-4.1-mini", temperature=0.2, api_key=api_key)
judge_agent = ChatOpenAI(model="gpt-4.1-mini", temperature=0, api_key=api_key)

case = "A fintech startup wants to launch instant approval loans in 2 weeks."

growth_view = growth_agent.invoke(
    f"You are the growth team. Argue in favor of fast launch in 4 short points. Case: {case}"
).content

risk_view = risk_agent.invoke(
    f"You are the risk team. Argue against the fast launch in 4 short points. Case: {case}"
).content

judgement = judge_agent.invoke(
    f"Give a balanced final decision using both views.\nGrowth View:\n{growth_view}\n\nRisk View:\n{risk_view}"
).content

print("GROWTH VIEW:\n", growth_view)
print("\nRISK VIEW:\n", risk_view)
print("\nFINAL JUDGEMENT:\n", judgement)
