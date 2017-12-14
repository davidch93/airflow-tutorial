from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2017, 12, 12),
    'retries': 0,
}

dag = DAG(
    'airflow-spark-submit', default_args=default_args, schedule_interval=timedelta(1))

APPLICATION_FILE_PATH = "~/spark/spark-create-orc-from-hbase-1.0.0-jar-with-dependencies.jar"

t1 = BashOperator(
    task_id='spark-submit-java',
    bash_command='spark-submit ' + APPLICATION_FILE_PATH,
    dag=dag)
