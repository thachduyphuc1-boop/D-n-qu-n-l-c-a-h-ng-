
import json

class User:

    def __init__(self, staff_id, staff_name, staff_role, username, password):
        self.staff_id = staff_id
        self.staff_name = staff_name
        self.staff_role = staff_role
        self.username = username
        self.password = password

def load_users():

    with open("Data/User.json", "r") as f:
        users = json.load(f)

    return users


def save_users(users):

    with open("Data/User.json", "w") as f:
        json.dump(users, f, indent=4)
def add_user():

    users = load_users()

    user = {
        "username": input("Username: "),
        "password": input("Password: "),
        "role": input("Role (admin/staff): ")
    }

    users.append(user)

    save_users(users)

    print("User added")
def search_user():

    users = load_users()

    uname = input("Enter username: ")

    for u in users:

        if u["username"].lower() == uname.lower():
            print(u)
            return

    print("User not found")
def update_user():

    users = load_users()

    uname = input("Username to update: ")

    for u in users:

        if u["username"].lower() == uname.lower():

            u["password"] = input("New password: ")
            u["role"] = input("New role: ")

            save_users(users)

            print("User updated")
            return

    print("User not found")
def delete_user():

    users = load_users()

    uname = input("Username to delete: ")

    for u in users:

        if u["username"].lower() == uname.lower():

            users.remove(u)

            save_users(users)

            print("User deleted")
            return

    print("User not found")
def list_user():

    users = load_users()

    for u in users:
        print(u)