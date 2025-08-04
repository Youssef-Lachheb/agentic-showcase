from agno.agent import Agent
from agno.models.openai import OpenAIChat

def load_classifier_agent():
    return Agent(
        model=OpenAIChat(id="gpt-3.5-turbo"),
        description="You classify math problems into categories like 'algebra', 'geometry', 'arithmetic'.",
        instructions=[
            "Only respond with one word: 'algebra', 'geometry', or 'arithmetic'.",
            "Do not explain or expand.",
        ]
    )
