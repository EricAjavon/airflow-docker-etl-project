from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator

default_args = {
    "owner": "eric",
    "retries": 2,
    "retry_delay": timedelta(minutes=2),
}

with DAG(
    dag_id="sales_etl_pipeline",
    description="ETL pipeline using Airflow, Docker, PostgreSQL and Git",
    start_date=datetime(2026, 7, 1),
    schedule="@daily",
    catchup=False,
    default_args=default_args,
    tags=["data-engineering", "docker", "postgres", "etl"],
) as dag:

    extract_sales = BashOperator(
        task_id="extract_sales",
        bash_command="python /opt/airflow/scripts/extract_sales.py"
    )

    transform_sales = BashOperator(
        task_id="transform_sales",
        bash_command="python /opt/airflow/scripts/transform_sales.py"
    )

    load_sales = BashOperator(
        task_id="load_sales",
        bash_command="python /opt/airflow/scripts/load_sales.py",
        env={
            "POSTGRES_USER": "airflow",
            "POSTGRES_PASSWORD": "airflow",
            "POSTGRES_HOST": "postgres",
            "POSTGRES_PORT": "5432",
            "POSTGRES_DB": "sales_warehouse",
        }
    )

    quality_check = BashOperator(
        task_id="quality_check",
        bash_command="python /opt/airflow/scripts/quality_check.py",
        env={
            "POSTGRES_USER": "airflow",
            "POSTGRES_PASSWORD": "airflow",
            "POSTGRES_HOST": "postgres",
            "POSTGRES_PORT": "5432",
            "POSTGRES_DB": "sales_warehouse",
        }
    )

    archive_file = BashOperator(
        task_id="archive_file",
        bash_command="""
        cp /opt/airflow/data/raw/sales.csv \
        /opt/airflow/data/archive/sales_{{ ds_nodash }}.csv
        """
    )

    extract_sales >> transform_sales >> load_sales >> quality_check >> archive_file