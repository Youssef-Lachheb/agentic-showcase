def split_into_clauses(text):
    # Very basic clause splitter
    clauses = [cl.strip() for cl in text.split(".") if len(cl.strip()) > 30]
    return clauses
