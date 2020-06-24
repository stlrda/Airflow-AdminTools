# Standard Library
import os
import sys
import datetime as dt

# Third party
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

# Custom
sys.path.append("/usr/local/airflow/dags/efs")
from admintools.scripts.create_connections import create_connections


default_args = {
    'owner': 'admintools',
    'start_date': dt.datetime(1993, 4, 16, 3, 00, 00),
    'concurrency': 1,
    'retries': 0,
    'catchup': False
}


with DAG('CreateConnections',
         default_args=default_args,
         schedule_interval= '@once',
         ) as dag:

    create_connections = PythonOperator(task_id='create_connections',
                    python_callable=create_connections)


create_connections
