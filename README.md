# 🧠 Agentic Showcase – Level 4 AI Agents

This repository demonstrates my ability to **design, build, and deploy modular, production-grade agentic AI systems** aligned with **Talent Performer's architecture and philosophy**.

It includes:

- ✅ **3 Level 4 Agents** — multi-agent teams using reasoning, memory, and tools


All agents are structured to simulate real-world client use cases with a focus on:
- Modular Agno-style design
- Clear task decomposition
- Tool and memory integration
- Real LLM behavior (OpenAI API)

---

## 🧪 Level 4 Agents

### 🔧 `contract_analyzer/`

**Use case:** Legal contract review assistant

**Capabilities:**
- PDF clause extraction
- Clause classification via LLM
- Clause memory indexing in ChromaDB
- Risk tagging and feedback stream

**Agents:**
- `ReaderAgent` – extracts contract clauses
- `RiskAnalyzerAgent` – rates clauses as safe or risky
- `MemoryAgent` – stores and retrieves past clause memory

---

### 📊 `data_insights_team/`

**Use case:** Business data summarizer and insight generator

**Capabilities:**
- CSV ingestion and parsing
- Summary + insights via LLM
- Follow-up question routing
- Fully modular Agno-style pipeline

**Agents:**
- `IngestAgent` – loads and normalizes CSV data
- `InsightsAgent` – generates summary and business insight
- `FollowUpAgent` – routes or generates follow-up actions

---

### 🧮 `math_tutor_duo/`

**Use case:** Interactive math tutor simulation

**Capabilities:**
- Classify math questions (algebra, geometry, arithmetic)
- Solve and explain problems via LLM
- Fully real Agno-powered agents
- Lightweight, stable Level 4 showcase

**Agents:**
- `ClassifierAgent` – determines question type
- `SolverAgent` – solves it step-by-step

---



---

## 🧱 Stack

- Python 3.10+
- OpenAI API (GPT-4o / GPT-3.5-turbo)
- LangChain Core, LangChain OpenAI
- ChromaDB, PyMuPDF
- Pandas, dotenv
- Agno framework (real, not mimicked)

---

## 🔑 Contact

**Youssef Lachheb**  
GitHub: [github.com/Youssef-Lachheb](https://github.com/Youssef-Lachheb)

---

## ⚔️ Status

- ✅ Agent 1 deployed and tested
- ✅ Agent 2 deployed and tested
- ✅ Agent 3 (`math_tutor_duo`) deployed and tested
-


