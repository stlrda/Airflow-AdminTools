# Standard Library
import sys
import datetime as dt

# Third party
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

# Custom
sys.path.append("/usr/local/airflow/dags/efs")
from admintools.scripts.install_python_deps import main

default_args = {
    'owner': 'admintools',
    'start_date': dt.datetime(1993, 4, 16, 3, 00, 00),
    'concurrency': 1,
    'retries': 0,
    'catchup': False
}

with DAG('InstallDependenciesProd',
         default_args=default_args,
         schedule_interval='@once',
         ) as dag:

    update = BashOperator(task_id='update', bash_command="apt-get update")

    # install_git = BashOperator(task_id='install_git', bash_command="apt install -y git")

    install_mdbtools = BashOperator(task_id='install_mdbtools', bash_command="apt-get install mdbtools -y")

    install_pandas = BashOperator(task_id="install_pandas", bash_command="pip3 install pandas")

    install_python_deps = PythonOperator(task_id="install_python_deps", python_callable=main)

update >> install_mdbtools >> install_pandas >> install_python_deps