from random import randint

class Bank:
    def __init__(self):
        self.account = randint(10000, 999999)
        self.name = input("Enter the name = ")
        self.balance = 0
        self.phone_number = int(input("Enter phone number="))

    def show_info(self):
        print(f"Account number = {self.account}")
        print(f"Full name = {self.name}")
        print (f"Balance = {self.balance}")               

    def show_balance(self):
        print (f"current balance = {self.balance}")
    
    def withdraw(self):
        amount = int(input("Enter the amount to withdraw"))
        if self.balance > amount:
            self.balance -= amount
        else:
            print ("Insufficient balance")
        
    def deposit(self) -> None:
        amount = int(input("Enter the amount to deposit ="))
        self.balance += amount

'''
x = Bank()
banks.append(x)

y = Bank()
banks.append(y)

banks[0].show_balance()
'''

banks = []
while True:
    print("1. create an account")
    print("2. show all bank details")
    print("3. Deposit amount")
    print("4. Exit")
    choice = int(input("Enter the choice = "))
    if choice == 1:
        obj = Bank()
        banks.append(obj)
        print (banks)
    elif choice == 2:
        if len(banks) == 0:
            print ("No accounts created")
        else:
            for account in banks:
                account.show_info()
    elif choice == 3:
        if len(banks) == 0:
            print("No banks found")
        else:
            account = int(input("Enter the accont nu to deposit"))
            for obj in banks:
                if obj.account == account:
                    obj.deposit()
                break
    elif choice == 4:
        break
    else:
        print("Invalid choice")

