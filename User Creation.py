def create_user():
    print("Create user")

def view_user():
    print("View user")

def edit_user():
    print("Edit user")

def remove_user():
    print("Remove user")

def main():
    selec = "0"

    while selec != "00":
        print("""User Creation Menu
    1. Create User
    2. View User
    3. Edit User
    4. Remove user

    00. Exit program""")

        selec = str(input("Input:  "))

        if selec == "1":
            create_user()

        elif selec == "2":
            view_user()

        elif selec == "3":
            edit_user()

        elif selec == "4":
            remove_user()

        elif selec == "00":
            print("Goodbye")

        else:
            print("Enter a valid input")

main()
