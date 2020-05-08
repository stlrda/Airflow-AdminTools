#Standard Library
import os
import json

def create_users():
    #Open JSON File which contains details for default users that need to be created and put it in a variable
    with open('dags/admintools/resources/defaultUsers.json', 'r') as f:
        data = json.load(f)
        
        #loop through each user's credentials and build a create user command from all present criteria
        for user in data['DefaultUsers']:
            createUser = 'airflow create_user'
            #Add each argument to the create user command if it exists in the JSON object
            if 'username' in user:
                createUser += f" -u {user['username']}" #Must be unique
            if 'role' in user:
                createUser += f" -r {user['role']}" #Options include Admin, User, Op, Viewer, and Public
            if 'email' in user:
                createUser += f" -e {user['email']}" #Must be unique
            if 'firstname' in user:
                createUser += f" -f {user['firstname']}"
            if 'lastname' in user:
                createUser += f" -l {user['lastname']}"
            if 'password' in user:
                createUser += f" -p {user['password']}"

            #Execute the command to create an airflow user from the command line
            os.system(f"{createUser}")

if __name__ == "__main__":
    create_users()