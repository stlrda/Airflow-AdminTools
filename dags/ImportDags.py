# Standard Library
import os
import sys
import datetime as dt

# Third party
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

# Custom
sys.path.append("/usr/local/airflow")
from admintools.scripts.clone_and_link import main

default_args = {
    'owner': 'admintools',
    'start_date': dt.datetime(1993, 4, 16, 3, 00, 00),
    'concurrency': 1,
    'retries': 0,
    'catchup': False
}


with DAG('ImportDAGS',
         default_args=default_args,
         schedule_interval='@once',
         ) as dag:

    clone_and_link = PythonOperator(task_id='clone_and_link',
                    python_callable=main)

clone_and_link