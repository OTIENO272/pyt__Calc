# Simple Banking Program

accounts = {}
transactions = {}

def create_account():
    username = input("Enter a username: ")
    if username in accounts:
        print("Username already exists!")
        return
    password = input("Enter a password: ")
    accounts[username] = {'password': password, 'balance': 0.0}
    transactions[username] = []
    print("Account created successfully!")

def login():
    username = input("Username: ")
    password = input("Password: ")
    
    if username in accounts and accounts[username]['password'] == password:
        print("Login successful!")
        return username
    print("Invalid credentials!")
    return None

def deposit(username):
    try:
        amount = float(input("Enter deposit amount: $"))
        if amount <= 0:
            print("Amount must be positive!")
            return
        accounts[username]['balance'] += amount
        transactions[username].append(f"Deposited ${amount:.2f}")
        print(f"${amount:.2f} deposited successfully!")
    except ValueError:
        print("Invalid input! Please enter numbers only.")

def withdraw(username):
    try:
        amount = float(input("Enter withdrawal amount: $"))
        if amount <= 0:
            print("Amount must be positive!")
            return
        if amount > accounts[username]['balance']:
            print("Insufficient funds!")
            return
        accounts[username]['balance'] -= amount
        transactions[username].append(f"Withdrew ${amount:.2f}")
        print(f"${amount:.2f} withdrawn successfully!")
    except ValueError:
        print("Invalid input! Please enter numbers only.")

def view_transactions(username):
    print("\nTransaction History:")
    for transaction in transactions[username]:
        print(transaction)

def main():
    while True:
        print("\n=== Main Menu ===")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Enter choice (1-3): ")
        
        if choice == '1':
            create_account()
        elif choice == '2':
            user = login()
            if user:
                while True:
                    print(f"\nWelcome {user}!")
                    print("1. Check Balance")
                    print("2. Deposit")
                    print("3. Withdraw")
                    print("4. View Transactions")
                    print("5. Logout")
                    
                    option = input("Enter option (1-5): ")
                    
                    if option == '1':
                        print(f"Current Balance: ${accounts[user]['balance']:.2f}")
                    elif option == '2':
                        deposit(user)
                    elif option == '3':
                        withdraw(user)
                    elif option == '4':
                        view_transactions(user)
                    elif option == '5':
                        break
                    else:
                        print("Invalid option!")
        elif choice == '3':
            print("Thank you for banking with us!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()