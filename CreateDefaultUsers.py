#Standard Library
import os
import json

def create_users():
    #Open JSON File which contains details for default users that need to be created and put it in a variable
    f = open('DefaultUsers.json')
    data = json.load(f)

    #loop through each user's credentials and build a create user command from all present criteria
    for i in data['DefaultUsers']:
        createUser = 'airflow create_user'
        #Add each argument to the create user command if it exists in the JSON object
        if 'username' in i:
            createUser += f" -u {i['username']}" #Must be unique
        if 'role' in i:
            createUser += f" -r {i['role']}" #Options include Admin, User, Op, Viewer, and Public
        if 'email' in i:
            createUser += f" -e {i['email']}" #Must be unique
        if 'firstname' in i:
            createUser += f" -f {i['firstname']}"
        if 'lastname' in i:
            createUser += f" -l {i['lastname']}"
        if 'password' in i:
            createUser += f" -p {i['password']}"

        #Execute the command to create an airflow user from the command line
        os.system(f"{createUser}")

    f.close()

if __name__ == "__main__":
    create_users()