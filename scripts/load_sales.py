import os
import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine, text

TRANSFORMED_FILE = Path("/opt/airflow/data/processed/transformed_sales.csv")

def get_engine():
    user = os.getenv("POSTGRES_USER", "airflow")
    password = os.getenv("POSTGRES_PASSWORD", "airflow")
    host = os.getenv("POSTGRES_HOST", "postgres")
    port = os.getenv("POSTGRES_PORT", "5432")
    db = os.getenv("POSTGRES_DB", "sales_warehouse")

    return create_engine(
        f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}"
    )

def load_sales():
    df = pd.read_csv(TRANSFORMED_FILE)
    engine = get_engine()

    with engine.begin() as conn:
        for _, row in df.iterrows():
            conn.execute(
                text("""
                    INSERT INTO sales_cleaned (
                        order_id,
                        order_date,
                        customer,
                        product,
                        quantity,
                        unit_price,
                        region,
                        total_sales
                    )
                    VALUES (
                        :order_id,
                        :order_date,
                        :customer,
                        :product,
                        :quantity,
                        :unit_price,
                        :region,
                        :total_sales
                    )
                    ON CONFLICT (order_id)
                    DO UPDATE SET
                        order_date = EXCLUDED.order_date,
                        customer = EXCLUDED.customer,
                        product = EXCLUDED.product,
                        quantity = EXCLUDED.quantity,
                        unit_price = EXCLUDED.unit_price,
                        region = EXCLUDED.region,
                        total_sales = EXCLUDED.total_sales,
                        loaded_at = CURRENT_TIMESTAMP;
                """),
                row.to_dict()
            )

    print(f"Loaded {len(df)} rows into sales_cleaned")

if __name__ == "__main__":
    load_sales()