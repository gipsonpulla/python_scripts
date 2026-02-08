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

b1 = Bank()
b1.show_balance()
b1.deposit()
b1.withdraw()
b1.show_balance()
