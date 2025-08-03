
from langchain_openai import ChatOpenAI  # ✅ Replace old import
from langchain_core.messages import HumanMessage  # ✅ Required for 0.1+
import os
from dotenv import load_dotenv

load_dotenv()
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.1)

def analyze_clause(clause):
    prompt = (
        f"You're a legal analyst. Flag this clause as safe, risky, or unclear:\n\n"
        f"Clause: \"{clause}\"\n\n"
        f"Explain your classification."
    )
    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content
