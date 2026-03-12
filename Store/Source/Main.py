from Auth.Auth import login, check_role

def main():

    user = None

    while user is None:
        user = login()

    role = check_role(user)

    print("Role:", role)


main()