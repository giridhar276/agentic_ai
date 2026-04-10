'''
Debate Agents Fight

One agent supports the topic
One agent opposes the topic
They argue over multiple rounds

Key concept:
Conflict and disagreement between agents
'''

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in environment or .env file")

pro_agent = ChatOpenAI(model="gpt-4.1-mini", temperature=0.2, api_key=api_key)
against_agent = ChatOpenAI(model="gpt-4.1-mini", temperature=0.2, api_key=api_key)

topic = "Should Agentic AI be used in high-volume customer support?"
history = f"Topic: {topic}\n"

for round_no in range(1, 4):
    pro_reply = pro_agent.invoke(
        f"You strongly support the topic. Reply in 3 short points. History:\n{history}"
    ).content
    history += f"Support Agent Round {round_no}: {pro_reply}\n"

    against_reply = against_agent.invoke(
        f"You strongly oppose the topic. Reply in 3 short points. History:\n{history}"
    ).content
    history += f"Opposition Agent Round {round_no}: {against_reply}\n"

print(history)
