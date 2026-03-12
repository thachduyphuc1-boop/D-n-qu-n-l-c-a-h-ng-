import json

def load_users():

    with open("Data/User.json", "r") as f:
        users = json.load(f)

    return users


def login():

    users = load_users()

    username = input("Username: ")
    password = input("Password: ")

    for user in users:

        if user["username"].lower() == username.lower() and user["password"] == password:

            print("Login success")
            return user

    print("Login fail")
    return None


def check_role(user):

    return user["role"]