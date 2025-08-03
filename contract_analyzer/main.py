import os
from utils import extract_text_from_pdf
from reader_agent import split_into_clauses
from risk_agent import analyze_clause
from memory_agent import store_clause

def classify_response(response_text):
    if "risky" in response_text.lower():
        return "risky"
    elif "unclear" in response_text.lower():
        return "unclear"
    else:
        return "safe"

def main():
    file_path = "sample_contract.pdf"  # Replace with your test file
    print(f"Reading: {file_path}")
    
    text = extract_text_from_pdf(file_path)
    clauses = split_into_clauses(text)

    for i, clause in enumerate(clauses):
        print(f"\nClause {i+1}:\n{clause}\n")
        analysis = analyze_clause(clause)
        label = classify_response(analysis)
        print(f"→ Label: {label}")
        print(f"→ Explanation: {analysis}")
        store_clause(clause, label, analysis)

    print("\n✅ All clauses analyzed and stored.")

if __name__ == "__main__":
    main()
