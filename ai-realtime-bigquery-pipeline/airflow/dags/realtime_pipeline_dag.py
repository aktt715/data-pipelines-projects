from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="realtime_bigquery_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule_interval="@hourly",
    catchup=False
) as dag:

    run_consumer = BashOperator(
        task_id="run_consumer",
        bash_command="python /app/consumer/consumer.py"
    )
