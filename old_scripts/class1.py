#!/usr/bin/python3

from random import randint

class Bank():
    def __init__(self):
        self.account = randint(100000, 999999)
        self.full_name = input("Enter your name")
        self.age = int(input("Enter the age"))
        self.balance = 0

    def show_info(self):
        print(f"Account number = {self.account}")
        print(f"Fulla name  = {self.full_name}")
        print(f"Age = {self.age}")
        print(f"balance = {self.balance}")

banks = []
obj = Bank()
banks.append(obj)
obj.show_info()