'''
Writer Reviewer Loop

Writer creates the first draft
Reviewer suggests improvements
Writer revises the draft multiple times

Key concept:
Iterative thinking and refinement
'''

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in environment or .env file")

writer = ChatOpenAI(model="gpt-4.1-mini", temperature=0.4, api_key=api_key)
reviewer = ChatOpenAI(model="gpt-4.1-mini", temperature=0, api_key=api_key)

topic = "Promote a beginner workshop on Agentic AI"

draft = writer.invoke(
    f"Write a short promotional message on this topic: {topic}"
).content

for round_no in range(1, 3):
    feedback = reviewer.invoke(
        f"Review this marketing draft and give 3 improvements.\n\nDraft:\n{draft}"
    ).content

    draft = writer.invoke(
        f"Improve this draft using the feedback.\n\nDraft:\n{draft}\n\nFeedback:\n{feedback}"
    ).content

print("FINAL DRAFT:\n", draft)
