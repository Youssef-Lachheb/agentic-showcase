
from chromadb import PersistentClient

client = PersistentClient(path="./memory")
collection = client.get_or_create_collection("contract_clauses")

def store_clause(clause, label, explanation):
    collection.add(
        documents=[clause],
        metadatas=[{"label": label, "reason": explanation}],
        ids=[f"id-{abs(hash(clause)) % (10 ** 8)}"]  # Avoid ID collisions
    )
