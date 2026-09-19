account= 200
ATM= True
while ATM:
    print(f"Your account balance is: ${account}")
    s= float(input("Enter the amount to withdraw: "))
    if s <= account and s> 0:
        account -= s
        print(f"Withdrawal successful. New balance: ${account}")
    else:
        print(f"You cannot withdraw ${s}. Your balance is ${account}.")
    if s <= 0:
        print("Please enter a positive amount to withdraw.")
    if account == 0:
        print("Account empty.")
        ATM = False
        break
