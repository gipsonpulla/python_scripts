from random import randint

class Bank:
    def __init__(self):
        self.account = randint(10000, 999999)
        self.name = input("Enter the name = ")
        self.balance = 0
        self.phone_number = int(input("Enter phone number="))
    
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
    print("3. Exit")
    choice = int(input("Enter the choice = "))
    if choice == 1:
        obj = Bank()
        banks.append(obj)
        print (banks)
    elif choice == 2:
        pass
    elif choice == 3:
        break
    else:
        print("Invalid choice")

