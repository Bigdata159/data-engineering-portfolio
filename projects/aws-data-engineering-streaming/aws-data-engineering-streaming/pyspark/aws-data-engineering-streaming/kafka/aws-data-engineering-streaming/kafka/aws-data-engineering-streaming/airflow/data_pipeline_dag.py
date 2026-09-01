from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator


def extract_data():
    print("Extracting data...")


def validate_data():
    print("Validating data...")


def transform_data():
    print("Transforming data...")


def load_data():
    print("Loading processed data...")


with DAG(
    dag_id="data_engineering_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False
) as dag:

    extract = PythonOperator(
        task_id="extract_data",
        python_callable=extract_data
    )

    validate = PythonOperator(
        task_id="validate_data",
        python_callable=validate_data
    )

    transform = PythonOperator(
        task_id="transform_data",
        python_callable=transform_data
    )

    load = PythonOperator(
        task_id="load_data",
        python_callable=load_data
    )

    extract >> validate >> transform >> load
