# Standard Library
import os
import sys
from datetime import datetime

# Third Party
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator

#python function
sys.path.append('./scripts') # Make sure there is an __init__.py file in this folder
from CreateDefaultUsers import create_users

# Call me with a python operator to figure out where airflow is running from.
# def WhereAmI():
#     print('This function was ran from ' + str(os.getcwd()))

#declare default args
default_args = {
    "owner": "airflow",
    "start_date": datetime(2020, 4, 15, 3, 00, 00),
    "concurrency": 1,
    "retries": 3,
}

#instantiate dag
dag = DAG(
    "create_default_users",
    default_args=default_args,
    description = 'Creates the default users for airflow',
    schedule_interval = None,
)

#create python operator
CreateDefaultUsers = PythonOperator(
    task_id="create_users",
    python_callable= create_users,
    dag=dag,
)

CreateDefaultUsers