# Agent 2 – Data Insights Team (Level 4)

This project simulates a modular, agentic AI system designed to process structured business data (CSV reports), analyze key metrics, and suggest intelligent follow-up actions.

Built in the spirit of Agno's multi-agent architecture, the system demonstrates reasoning, tool integration, and memory coordination among three distinct agents.

---

## 🧠 Agents

### 🟢 IngestAgent
- Reads and validates the uploaded CSV.
- Stores raw data and metadata in shared memory.

### 🔵 InsightsAgent
- Performs statistical analysis using Pandas.
- Generates descriptive insights (mean, std, min/max).
- Optionally creates visualizations.

### 🔴 FollowupAgent
- Detects anomalies or missing data.
- Flags columns or values that may require attention.
- Proposes follow-up actions.

---

## 🧱 Architecture

           +-------------------+
           |   CSV File Input  |
           +---------+---------+
                     |
               IngestAgent
                     |
               InsightsAgent
                     |
               FollowupAgent
                     |
             Shared Agent Memory


- All agents read/write to a central `Memory` object.
- `tools.py` contains core utility logic for plotting, outlier detection, etc.

---

## 🛠️ Tools & Stack

- **Python 3.10+**
- **Pandas** – data processing
- **Matplotlib** – chart generation
- **Custom Agent Framework** – Agno-style
- **Memory** – simple in-memory store (dict)

---

## 📂 Project Structure

data_insights_team/
├── main.py # Orchestrator
├── agents/ # Agent logic
│ ├── ingest_agent.py
│ ├── insights_agent.py
│ └── followup_agent.py
├── core/ # Agno-like base classes
│ ├── base_agent.py
│ ├── memory.py
│ └── tools.py
├── data/ # Input data
│ └── sample.csv
├── requirements.txt
└── README.md


---

## 🚀 How to Run

```bash
cd data_insights_team
pip install -r requirements.txt
python main.py

