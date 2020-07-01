# branson-local Branch
This branch is intended for the temporary installation of a LocalExecutor to test DAGs in Development.
Modifications made to these DAGs may not be applicable to the CeleryExecutor.
Note, this currently fakes the `efs` directory found within `/usr/local/airflow/dags/` to maintain some reusability. TBD if the distributed version needs DAGs on all instances with a shared volume.

# Airflow---Admin-Tools
Simple scripts to help with administration of Airflow
