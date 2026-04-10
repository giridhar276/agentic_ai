'''
Planner + Executor + Observer

Planner creates steps
Executor explains the action
Observer reviews the action

Key concept:
Plan action observation cycle
'''

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in environment or .env file")

planner = ChatOpenAI(model="gpt-4.1-mini", temperature=0, api_key=api_key)
executor = ChatOpenAI(model="gpt-4.1-mini", temperature=0, api_key=api_key)
observer = ChatOpenAI(model="gpt-4.1-mini", temperature=0, api_key=api_key)

goal = "Launch a small internal FAQ chatbot for employees"

plan = planner.invoke(
    f"Create a simple 5-step plan for this goal: {goal}"
).content

action = executor.invoke(
    f"Take this plan and explain what the team should do first:\n\n{plan}"
).content

observation = observer.invoke(
    f"Review this action and say whether it is practical. Give 3 short observations.\n\nAction:\n{action}"
).content

print("PLAN:\n", plan)
print("\nACTION:\n", action)
print("\nOBSERVATION:\n", observation)
