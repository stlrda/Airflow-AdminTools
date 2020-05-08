# Standard Library
import os
import sys
import datetime as dt

# Third Party
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator

#python function

sys.path.append('/usr/local/airflow') # Make sure there is an __init__.py file in this folder
from admintools.scripts.CreateDefaultUsers import create_users


# Call me with a python operator to figure out where airflow is running from.
# def WhereAmI():
#     print('This function was ran from ' + str(os.getcwd()))

#declare default args
default_args = {
    'owner': 'AdminTools',
    'start_date': dt.datetime.now(),
    'concurrency': 1,
    'retries': 0,
    'catchup': False
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
