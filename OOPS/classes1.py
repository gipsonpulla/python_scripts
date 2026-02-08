class Student:
    #Attributes
    #methods
    def info(self):
        print (f"Name = {self.name}")
        print (f"Age = {self.age}")
        print (f"Gender = {self.gender}")
        print (f"Address = {self.address}")
        print (f"roll_no = {self.roll_no}")
    
    def set_info(self):
        self.name = input("Enter your name")
        self.age = int(input("Enter your age"))
        self.gender = input("Enter your gender")
        self.address = input ("Enter your address")
        self.roll_no = input("Enter your roll_number")

s1 = Student()
s2 = Student()
s1.set_info()
s2.set_info()

print ("xxxxxxxxx")

s1.info()
s2.info()

