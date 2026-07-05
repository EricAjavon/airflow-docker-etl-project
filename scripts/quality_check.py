import os
from sqlalchemy import create_engine, text

def get_engine():
    user = os.getenv("POSTGRES_USER", "airflow")
    password = os.getenv("POSTGRES_PASSWORD", "airflow")
    host = os.getenv("POSTGRES_HOST", "postgres")
    port = os.getenv("POSTGRES_PORT", "5432")
    db = os.getenv("POSTGRES_DB", "sales_warehouse")

    return create_engine(
        f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}"
    )

def run_quality_checks():
    engine = get_engine()

    with engine.connect() as conn:
        row_count = conn.execute(
            text("SELECT COUNT(*) FROM sales_cleaned")
        ).scalar()

        null_order_ids = conn.execute(
            text("SELECT COUNT(*) FROM sales_cleaned WHERE order_id IS NULL")
        ).scalar()

        negative_sales = conn.execute(
            text("SELECT COUNT(*) FROM sales_cleaned WHERE total_sales < 0")
        ).scalar()

    if row_count == 0:
        raise ValueError("Quality check failed: table is empty")

    if null_order_ids > 0:
        raise ValueError("Quality check failed: null order IDs found")

    if negative_sales > 0:
        raise ValueError("Quality check failed: negative sales found")

    print("All quality checks passed")
    print(f"Total rows checked: {row_count}")

if __name__ == "__main__":
    run_quality_checks()