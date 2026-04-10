'''
Doctor + Second Opinion

Doctor one gives the first view
Doctor two gives another view
Coordinator combines both opinions

Key concept:
Expert collaboration with synthesis
'''

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in environment or .env file")

doctor1 = ChatOpenAI(model="gpt-4.1-mini", temperature=0, api_key=api_key)
doctor2 = ChatOpenAI(model="gpt-4.1-mini", temperature=0, api_key=api_key)
coordinator = ChatOpenAI(model="gpt-4.1-mini", temperature=0, api_key=api_key)

case = "Patient has fever, sore throat, tiredness, and mild cough for 3 days."

opinion1 = doctor1.invoke(
    f"You are a cautious doctor. Give a simple possible explanation and next steps. Case: {case}"
).content

opinion2 = doctor2.invoke(
    f"You are a second-opinion doctor. Give another simple possible explanation and next steps. Case: {case}"
).content

final_note = coordinator.invoke(
    f"Combine these two opinions into a simple summary with a disclaimer that this is not medical advice.\nOpinion 1:\n{opinion1}\n\nOpinion 2:\n{opinion2}"
).content

print("DOCTOR 1:\n", opinion1)
print("\nDOCTOR 2:\n", opinion2)
print("\nCOORDINATOR SUMMARY:\n", final_note)
