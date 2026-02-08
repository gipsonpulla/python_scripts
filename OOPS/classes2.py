class Student:
    #Attributes
    #methods
    def __init__(self): #constructor
        self.name = input("Enter your name")
        self.age = int(input("Enter your age"))
        self.gender = input("Enter your gender")
        self.address = input ("Enter your address")
        self.roll_no = input("Enter your roll_number")
    
    def info(self):
        print (f"Name = {self.name}")
        print (f"Age = {self.age}")
        print (f"Gender = {self.gender}")
        print (f"Address = {self.address}")
        print (f"roll_no = {self.roll_no}")


s1 = Student()
s2 = Student()
s1.info()
s2.info()

