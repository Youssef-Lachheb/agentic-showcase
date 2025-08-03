from agno.agent import Agent
from agno.models.openai import OpenAIChat
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

class InsightsAgent:
    def __init__(self):
        self.agent = Agent(
            model=OpenAIChat(id="gpt-4o"),
            description="Data insights generator",
            instructions=[
                "You are an expert data analyst.",
                "Analyze the summary statistics from the CSV file.",
                "Return your analysis in Markdown format with headers and bullet points.",
                "Highlight trends, outliers, or anomalies."
            ],
            markdown=True
        )

    def run(self, df: pd.DataFrame):
        print("[InsightsAgent] Generating markdown insights...")
        summary = df.describe(include="all").to_string()
        response = self.agent.run(summary)

        markdown_output = response.content  # ✅ FIXED

        with open("plots/insights.md", "w") as f:
            f.write(markdown_output)

        return markdown_output
