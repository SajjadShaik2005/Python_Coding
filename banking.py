# Initial account balance
balance = 1000.0

def check_balance():
    print(f"\nYour current balance is: ${balance:,.2f}")

def deposit(amount):
    global balance
    if amount > 0:
        balance += amount
        print(f"Successfully deposited ${amount:,.2f}")
    else:
        print("Invalid deposit amount.")

def withdraw(amount):
    global balance
    if amount > balance:
        print("Insufficient funds!")
    elif amount <= 0:
        print("Please enter a positive amount.")
    else:
        balance -= amount
        print(f"Successfully withdrew ${amount:,.2f}")

# --- Simple Interaction Loop ---
print("Welcome to the Python Bank")

while True:
    print("\n1. Check Balance | 2. Deposit | 3. Withdraw | 4. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        check_balance()
    elif choice == '2':
        amt = float(input("Enter deposit amount: "))
        deposit(amt)
    elif choice == '3':
        amt = float(input("Enter withdrawal amount: "))
        withdraw(amt)
    elif choice == '4':
        print("Thank you for banking with us. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")