print("#"*55)
print(" Welcome to our Smart ATM Simulator ".center(48,'#'))
print("#"*55)

correct_pin=1234
balance=5000
stored_pin=int(input("Enter your PIN: "))

if stored_pin!=correct_pin:
    print("Wrong PIN.\nTransaction rejected.")
else:
    print("Welcome to your account.")
    process=input("What process do you want to do? (withdraw/check balance): ").strip().lower()
    if process=="withdraw":
        amount=float(input("Enter the amount you want to withdraw: "))
        if amount>balance:
            print("Insufficient balance.\nTransaction rejected.")
        else:
            balance-=amount
            print(f"You have withdrawn {amount}.\nYour new balance is {balance}.")
    elif process=="check balance":
        print(f"Your balance is {balance}.")


