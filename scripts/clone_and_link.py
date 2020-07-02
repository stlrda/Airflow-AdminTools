import os
import pandas as pd
from subprocess import check_call, CalledProcessError

def main():
    """Clones every repo listed in "projects.csv" into /usr/local/airflow/dags/efs
    """

    # Should refer to raw file found in master branch for prod.
    PROJECTS_CSV = "/usr/local/airflow/dags/efs/admintools/resources/projects.csv"
    PROJECTS_DATAFRAME = pd.read_csv(PROJECTS_CSV)

    for index, row in PROJECTS_DATAFRAME.iterrows():

        project = row["Project"]
        repo = row["Repo"]
        url = row["URL"]

        project_folder = f"/usr/local/airflow/dags/efs/{project}"

        print(f"Cloning {project} : {repo} @ {url}")
        try:
            check_call(["git", "clone", f"{url}.git", project_folder])
        except CalledProcessError as pe:
            print("CalledProcessError : " + str(pe))

        print(f"Updating {project} : {repo} @ {url}")
        try:
            check_call(["git", "pull", f"{url}.git"])
        except CalledProcessError as pe:
            print("CalledProcessError : " + str(pe))
        
