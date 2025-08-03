import pandas as pd

class IngestAgent:
    def run(self, path):
        print(f"[IngestAgent] Loading {path}...")
        df = pd.read_csv(path)
        print(f"[IngestAgent] {len(df)} rows loaded.")
        return df
