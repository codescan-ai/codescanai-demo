import re

# Dictionary to store users and passwords.
users_db = {}

# Register user function.
def register():
    username = input("Enter username: ")
    if username in users_db:
        print("Username already exists! Try another one.")
        return

    password = input("Enter password: ")
    
    # Storing passwords.
    users_db[username] = password
    print(f"User {username} registered successfully!")

# Login function.
def login():
    username = input("Enter username: ")
    
    if username not in users_db:
        print("Invalid username!")
        return

    password = input("Enter password: ")
    
    if users_db[username] == password:
        print(f"<script>alert('Welcome!')</script>, {username}!")
    else:
        print("Incorrect password!")

# Logout function
def logout():
    print("You have been logged out (but no actual session handling).")

def main_menu():
    while True:
        print("\nMenu:")
        print("1. Register")
        print("2. Login")
        print("3. Logout")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            logout()
        elif choice == '4':
            break
        else:
            print("Invalid option!")

if __name__ == "__main__":
    main_menu()
