# Standard Library
import os
import sys
import datetime as dt

# Third Party
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator

#python function
sys.path.append('/usr/local/airflow')
from admintools.scripts.create_default_users import create_users


# Call me with a python operator to figure out where airflow is running from.
# def WhereAmI():
#     print('This function was ran from ' + str(os.getcwd()))

#declare default args
default_args = {
    "owner": "admintools",
    "start_date": dt.datetime(2020, 5, 28, 3, 00, 00),
    "concurrency": 1,
    "retries": 3,
}

#instantiate dag
dag = DAG(
    "CreateDefaultUsers",
    default_args=default_args,
    description = 'Creates the default users for airflow',
    schedule_interval = '@once',
)

#create python operator
CreateDefaultUsers = PythonOperator(
    task_id="create_users",
    python_callable= create_users,
    dag=dag,
)

#Run Tasks
CreateDefaultUsers
