# Agent 2 – Data Insights Team (Level 4)

This Level 4 agent team parses business data and generates structured insights using Agno + OpenAI.

## Agents
- **IngestAgent** – Loads CSV and parses into a DataFrame
- **InsightsAgent** – Agno-powered; returns Markdown report from LLM
- **FollowUpAgent** – Proposes additional questions based on the dataset

## Usage
```bash
cd data_insights_team
python main.py
