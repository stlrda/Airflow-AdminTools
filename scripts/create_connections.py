# Standard library
import os
import json

# Third party
from airflow import settings
from airflow.models import Connection
# from airflow import configuration as conf


def create_connections():
    """Will create an Airflow connection for each json in the 'resources/connections.json' file.
    This function will overwrite the connection if it already exists.
    """
    with open('resources/connections.json', 'r') as f:
        json_objects_array = json.load(f)

    for json_object in json_objects_array:

        ConnId = json_object["Conn Id"]
        ConnType = json_object["Conn Type"]
        Host = json_object["Host"]
        Schema = json_object["Schema"]
        Login = json_object["Login"]
        Password = json_object["Password"]
        Port = json_object["Port"]

        try:
            # The "Extra" field must convert from string to valid json or None, hence the transformations below.
            Extra_In = json_object["Extra"]
            Extra_Out = json.dumps(Extra_In) if (Extra_In != "" and Extra_In != None) else None

        except Exception as err:
            print(f"Program was expecting 'Extra' value to be either an empty string, NoneType, or json / dict.\n{err}")

        new_conn = Connection(conn_id=ConnId,
                        conn_type=ConnType, 
                        host=Host, schema=Schema,
                        login=Login,
                        password=Password,
                        port=Port,
                        extra=Extra_Out)
            

        session = settings.Session() # get the session

        # Checks to see if connection already exists.
        if (session.query(Connection).filter(Connection.conn_id == new_conn.conn_id).first()):
            print(f'Connection with Conn Id: "{ConnId}" already exists. Deleting now...')
            os.system(f"airflow connections -d --conn_id {ConnId}") # deletes connection

        session.add(new_conn)
        session.commit()
        session.close()
        print(f'Connection with Conn Id "{ConnId}" now added.')


# ? Comments below are saved for future reference.
# new_conn.set_extra(None) : disables 'extra' encryption layer
# new_conn.rotate_fernet_key() : theoretically updates fernet key
# conf.get('core','fernet_key') : returns active fernet key