# Airflow Docker ETL Project

## Project Overview

This project is a beginner-to-intermediate data engineering pipeline built with Apache Airflow, Docker, PostgreSQL, Python, and Git.

The pipeline extracts raw sales data from a CSV file, transforms the data using Python, loads it into a PostgreSQL database, performs data quality checks, and archives the processed file.

## Tools Used

* Apache Airflow
* Docker
* Docker Compose
* PostgreSQL
* Python
* Pandas
* SQLAlchemy
* Git and GitHub

## Pipeline Flow

```text
Raw CSV Data
    ↓
Extract Task
    ↓
Transform Task
    ↓
Load to PostgreSQL
    ↓
Data Quality Check
    ↓
Archive Processed File
```

## Project Structure

```text
airflow-docker-etl-project/
│
├── dags/
│   └── sales_etl_dag.py
│
├── scripts/
│   ├── extract_sales.py
│   ├── transform_sales.py
│   ├── load_sales.py
│   └── quality_check.py
│
├── data/
│   ├── raw/
│   │   └── sales.csv
│   ├── processed/
│   └── archive/
│
├── logs/
├── plugins/
│
├── sql/
│   └── create_tables.sql
│
├── .env
├── .gitignore
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## What the Project Demonstrates

This project demonstrates how to:

* Build a containerized data engineering environment
* Use Docker Compose to run Airflow and PostgreSQL
* Create an Airflow DAG for ETL orchestration
* Write modular Python ETL scripts
* Load transformed data into a PostgreSQL database
* Apply basic data quality checks
* Use Git for version control
* Prepare a project for GitHub portfolio presentation

## Prerequisites

Before running this project, install:

* Docker Desktop
* Git
* Visual Studio Code
* A GitHub account

## Environment Variables

Create a `.env` file in the project root:

```env
POSTGRES_USER=airflow
POSTGRES_PASSWORD=airflow
POSTGRES_DB=sales_warehouse
POSTGRES_HOST=postgres
POSTGRES_PORT=5432
AIRFLOW_UID=50000
```

Do not upload `.env` to GitHub.

## How to Run the Project

From the project root folder, run:

```bash
docker compose up --build -d
```

Check running containers:

```bash
docker compose ps
```

Open Airflow in your browser:

```text
http://localhost:8080
```

Login details:

```text
Username: admin
Password: admin
```

Trigger the DAG:

```text
DAGs → sales_etl_pipeline → Trigger DAG
```

## How to Check the PostgreSQL Table

Enter the PostgreSQL container:

```bash
docker compose exec postgres psql -U airflow -d sales_warehouse
```

Run:

```sql
SELECT * FROM sales_cleaned;
```

## Useful Docker Commands

```bash
docker compose up --build -d
docker compose ps
docker compose logs -f
docker compose down
docker compose down -v
```

Use `docker compose down -v` carefully because it deletes the database volume.

## Useful Git Commands

```bash
git status
git add .
git commit -m "Your commit message"
git log --oneline
```

## Future Improvements

Possible upgrades include:

* Add API data extraction
* Add multiple source files
* Add dbt transformations
* Add Great Expectations for data validation
* Add Power BI dashboard connected to PostgreSQL
* Add Slack or email alerts
* Add GitHub Actions CI/CD
* Deploy Airflow on cloud infrastructure
* Add unit tests for Python scripts

## Author

Eric Akwete Ajavon
Data Analyst | Data Engineer
