# 🧮 Agent 3 – Math Tutor Duo (Level 4 Agno Agent)

This project is a simple two-agent Level 4 AI system built using the real **Agno framework**.

It consists of:

- **ClassifierAgent** – determines if a math problem is about `algebra`, `geometry`, or `arithmetic`.
- **SolverAgent** – explains and solves the math problem step-by-step.

## 📁 Structure

math_tutor_duo/
├── main.py
├── agent/
│ ├── classifier_agent.py
│ └── solver_agent.py
├── requirements.txt
├── .env.template
└── README.md


## 🔧 Setup

```bash
cd math_tutor_duo
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt


## OpenAI  API

create a .env file with OpenAI API key
OPENAI_API_KEY=your_openai_api_key_here


## Run

python main.py

## Example :

🧑 User: What is the area of a circle with radius 3?
🧠 Topic: geometry
🤖 A = π × 3² = 9π

## Tech

Agno
OpenAI Chat (gpt-3.5-turbo or gpt-4o)
Python 3.10+