import hashlib

def register(username, password):
    
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    
    with open('user_data.txt', 'a') as file:
        file.write(f"{username}:{hashed_password}\n")

    print(f"User '{username}' registered successfully.")

def login(username, password):
    
    hashed_password_input = hashlib.sha256(password.encode()).hexdigest()

   
    with open('user_data.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            stored_username, stored_hashed_password = line.strip().split(':')
            if stored_username == username and stored_hashed_password == hashed_password_input:
                print(f"Welcome, {username}! Login successful.")
                return

        print("Invalid username or password. Login failed.")

def main():
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("What are you expecting (a/b/c): ")

        if choice == 'a':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            register(username, password)
        elif choice == 'b':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            login(username, password)
        elif choice == 'c':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a, b, or c.")

if __name__ == "__main__":
    main()


