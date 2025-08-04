from agno.agent import Agent
from agno.models.openai import OpenAIChat

def load_solver_agent():
    return Agent(
        model=OpenAIChat(id="gpt-3.5-turbo"),
        description="You are a math tutor who solves simple problems in geometry, algebra, and arithmetic.",
        instructions=[
            "Solve the problem step-by-step.",
            "Be concise but clear.",
            "Give final answer at the end.",
        ],
        markdown=True
    )
