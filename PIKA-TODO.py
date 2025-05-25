from cryptography.fernet import Fernet
import os
import getpass
import hashlib
import base64

print(r"""
 _______  _____  ___  ____        _        _________    ____          ______      ____     _____     _   ______   _________  
|_   __ \|_   _||_  ||_  _|      / \      |  _   _  | .'    '.       |_   _ `.  .'    '.  |_   _|   | |.' ____ \ |  _   _  | 
  | |__) | | |    | |_/ /       / _ \     |_/ | | \_||  .--.  | ______ | | `. \|  .--.  |   | |     | || (___ \_||_/ | | \_| 
  |  ___/  | |    |  __'.      / ___ \        | |    | |    | ||______|| |  | || |    | |   | |   _ | | _.____`.     | |     
 _| |_    _| |_  _| |  \ \_  _/ /   \ \_     _| |_   |  `--'  |       _| |_.' /|  `--'  |  _| |__/ ||_|| \____) |   _| |_    
|_____|  |_____||____||____||____| |____|   |_____|   '.____.'       |______.'  '.____.'  |________|(_) \______.'  |_____|   
                                                                                                                             
""")
def load_users():
    if os.path.exists("users.txt"):
        with open("users.txt", "r") as f:
            for line in f:
                if ',' in line:
                    user, password = line.strip().split(',', 1)
                    usr_list.append(user)
                    pass_list.append(password)
                    
                    
def show_Users():
    print("\n--- TO-DO USERS LIST MENU ---")
    print("1. Add User")
    print("2. View Users")
    print("3. Select User")
    print("4. Delete User")
    print("5. Exit")

def save_user(username, password):
    with open("users.txt", "a") as f:
        f.write(f"{username},{password}\n")


def update_user_file():
    with open("users.txt", "w") as f:
        for user, password in zip(usr_list, pass_list):
            f.write(f"{user},{password}\n")


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# def derive_key(password):
#     return base64.urlsafe_b64encode(hashlib.sha256(password.encode()).digest())

# def encrypt_data(data, password):
#     key = derive_key(password)
#     Fernet = Fernet(key)
#     return Fernet.encrypt(data.encode())  

# def decrypt_data(encrypted_data, password):
#     key = derive_key(password)
#     Fernet = Fernet(key)
#     return Fernet.decrypt(encrypted_data).decode()  

usr_list = []
pass_list = []
load_users()


def single_usr(name):

    FILE_NAME = f"{name}_todo.txt"

    # Create the file if it doesn't exist
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as f:
            pass  # create an empty file

    def show_menu():
        print(f"\n--- {name} TO-DO LIST MENU ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            task = input("Enter the task: ")
            # enc = encrypt_data(task, password)#--------------------------------------------------------------------------------------
            with open(FILE_NAME, "a") as f:
                f.write("[ ] " + task + "\n")
            print("Task added.")

        elif choice == "2":
            print("\n--- Your Tasks ---")
            with open(FILE_NAME, "r") as f:
                lines = f.readlines()
            try:
                #tasks = decrypt_data(enc, password).splitlines() #--------------------------------------------------------------
                for i, line in enumerate(lines, 1):
                    print(f"{i}. {line.strip()}")
            except:
                print("Wrong password or corrupted file")
        elif choice == "3":
            with open(FILE_NAME, "r") as f:
                lines = f.readlines()

            for i, line in enumerate(lines, 1):
                print(f"{i}. {line.strip()}")

            idx = int(input("Enter task number to mark as done: "))
            if 1 <= idx <= len(lines):
                if lines[idx - 1].startswith("[ ]"):
                    lines[idx - 1] = lines[idx - 1].replace("[ ]", "[x]", 1)
                else:
                    print("Task is already marked as done.")

                with open(FILE_NAME, "w") as f:
                    f.writelines(lines)
                print("Task updated.")
            else:
                print("Invalid task number.")

        elif choice == "4":
            with open(FILE_NAME, "r") as f:
                lines = f.readlines()

            for i, line in enumerate(lines, 1):
                print(f"{i}. {line.strip()}")

            idx = int(input("Enter task number to delete: "))
            if 1 <= idx <= len(lines):
                lines.pop(idx - 1)
                with open(FILE_NAME, "w") as f:
                    f.writelines(lines)
                print("Task deleted.")
            else:
                print("Invalid task number.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

while True:
    show_Users()
    choice = int(input("Enter the Operation: "))

    if choice == 1:
        usr = input(f"Enter the name for user {len(usr_list)+1}: ")
        if usr in usr_list:
            print("Username already exists.")
            continue
        password = hash_password(getpass.getpass("Enter the password: "))
        usr_list.append(usr)
        pass_list.append(password)
        save_user(usr, password)
        print("User registered successfully.")

        

    
    elif choice == 2:
        print(f"\n--- Registered Users ---")
        for i, user in enumerate(usr_list, 1):
            print(f"{i}. {user}")

    elif choice == 3:
        print(f"\n--- Registered Users ---")
        for i, user in enumerate(usr_list, 1):
            print(f"{i}. {user}")

        if len(usr_list) == 0:
            continue

        selection = int(input("Select the S.No: "))
        entr_pass = getpass.getpass("Enter the password: ")
        if hash_password(entr_pass) == pass_list[selection-1]:
                single_usr(usr_list[selection-1])
        else:
            print("\nGet out from here!! Bastard..")
            break
    
    elif choice == 4:
        print(f"\n--- Registered Users ---")
        for i, user in enumerate(usr_list, 1):
            print(f"{i}. {user}")

        if len(usr_list) == 0:
            continue

        selection = int(input("Select the S.No: "))
        entr_pass = getpass.getpass("Enter the password: ")
        if hash_password(entr_pass) == pass_list[selection-1]:
                del usr_list[selection-1]
                del pass_list[selection-1]
                update_user_file()
                print("User deleted.")
        else:
            print("\nGet out from here!! Bastard..")
            break

    elif choice == 5:
        print("Goodbye!")
        break

    else:
        print("Feature not implemented yet.")
