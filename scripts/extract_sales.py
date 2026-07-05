import pandas as pd
from pathlib import Path

RAW_FILE = Path("/opt/airflow/data/raw/sales.csv")
EXTRACTED_FILE = Path("/opt/airflow/data/processed/extracted_sales.csv")

def extract_sales():
    if not RAW_FILE.exists():
        raise FileNotFoundError(f"Raw file not found: {RAW_FILE}")

    df = pd.read_csv(RAW_FILE)

    EXTRACTED_FILE.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(EXTRACTED_FILE, index=False)

    print(f"Extracted {len(df)} rows from {RAW_FILE}")

if __name__ == "__main__":
    extract_sales()