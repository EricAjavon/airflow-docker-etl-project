import pandas as pd
from pathlib import Path

EXTRACTED_FILE = Path("/opt/airflow/data/processed/extracted_sales.csv")
TRANSFORMED_FILE = Path("/opt/airflow/data/processed/transformed_sales.csv")

def transform_sales():
    df = pd.read_csv(EXTRACTED_FILE)

    df.columns = df.columns.str.lower().str.strip()

    df["order_date"] = pd.to_datetime(df["order_date"]).dt.date
    df["quantity"] = df["quantity"].astype(int)
    df["unit_price"] = df["unit_price"].astype(float)
    df["total_sales"] = df["quantity"] * df["unit_price"]

    df = df.drop_duplicates(subset=["order_id"])

    df.to_csv(TRANSFORMED_FILE, index=False)

    print(f"Transformed {len(df)} rows")
    print(df.head())

if __name__ == "__main__":
    transform_sales()