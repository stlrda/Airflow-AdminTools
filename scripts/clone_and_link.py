import os
import pandas as pd
from subprocess import check_call, CalledProcessError

def main():
    """Clones every repo listed in "projects.csv" into /usr/local/airflow/dags/efs
    """

    # Should refer to raw file found in master branch for prod.
    PROJECTS_CSV = "https://raw.githubusercontent.com/stlrda/Airflow-AdminTools/master/resources/projects.csv"
    PROJECTS_DATAFRAME = pd.read_csv(PROJECTS_CSV)

    for index, row in PROJECTS_DATAFRAME.iterrows():

        project = row["Project"]
        repo = row["Repo"]
        url = row["URL"]

        project_folder = f"/usr/local/airflow/dags/efs/{project}"
        # symlink = f"/usr/local/airflow/dags/efs/{project}"

        # try:
        #     print(f"Deleting project folder: {project_folder}") # efs object
        #     os.system(f"rm -rf {project_folder}")
        #     print(f"Project folder: '{project_folder}' removed.")
        # except Exception as err:
        #     print(err)
        #
        # try:
        #     print(f"Deleting symbolic link: {symlink}")
        #     os.system(f"rm -rf {symlink}")
        #     print(f"Symbolic link: '{symlink}' removed.")
        # except Exception as err:
        #     print(err)


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
        # try:
        #     print(f"Linking {project_folder} to {symlink}")
        #     check_call(["ln", "-s", project_folder, symlink])
        # except CalledProcessError as pe:
        #     print("CalledProcessError : " + str(pe))

