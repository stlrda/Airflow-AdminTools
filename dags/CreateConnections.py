# Standard Library
import sys
import datetime as dt

# Third party
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

# Custom
sys.path.append(".")
from dags.admintools.scripts.create_connections import create_connections



default_args = {
    'owner': 'AdminTools',
    'start_date': dt.datetime.now(),
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
