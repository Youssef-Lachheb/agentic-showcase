# 📄 Contract Analyzer Agent (Level 4)

This project simulates a real-world legal assistant AI system that:

- Extracts clauses from PDF contracts  
- Classifies them as **safe**, **risky**, or **unclear** using GPT-3.5  
- Stores the results in a **vector database (ChromaDB)** with classification reasoning attached  

---

## 📦 Agents

- **Reader Agent** – extracts and segments legal clauses from PDF
- **Risk Agent** – uses LLM to classify each clause
- **Memory Agent** – embeds each clause with metadata into ChromaDB

---

## 🔐 Requirements

Create a `.env` file in the `contract_analyzer/` folder:
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

## How to Run

```bash
pip install -r requirements.txt
python main.py

🔗 Stack

    Python 3.10+
    OpenAI GPT-3.5 (via LangChain OpenAI)
    PyMuPDF for PDF parsing
    ChromaDB for persistent vector memory
