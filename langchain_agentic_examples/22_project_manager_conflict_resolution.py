'''
Project Manager Conflict Resolution

Developer explains one side
QA explains the other side
Project manager resolves the conflict

Key concept:
Conflict handling through multi-agent discussion
'''

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in environment or .env file")

developer_agent = ChatOpenAI(model="gpt-4.1-mini", temperature=0.2, api_key=api_key)
qa_agent = ChatOpenAI(model="gpt-4.1-mini", temperature=0.2, api_key=api_key)
pm_agent = ChatOpenAI(model="gpt-4.1-mini", temperature=0, api_key=api_key)

issue = "QA says the release is not stable. Developer says the deadline is too close to delay it."

developer_view = developer_agent.invoke(
    f"You are the developer. Explain your side in 3 short points. Issue: {issue}"
).content

qa_view = qa_agent.invoke(
    f"You are QA. Explain your side in 3 short points. Issue: {issue}"
).content

resolution = pm_agent.invoke(
    f"You are the project manager. Resolve this conflict fairly.\nDeveloper View:\n{developer_view}\n\nQA View:\n{qa_view}"
).content

print("DEVELOPER VIEW:\n", developer_view)
print("\nQA VIEW:\n", qa_view)
print("\nPM RESOLUTION:\n", resolution)
