class Student:
    def __init__(self) -> None:
        self.name = input("Enter name = ")
        self.age = input("Enter age =")
    
    def display_info(self):
        print (f"Name = {self.name}")
        print (f"Age = {self.age}")

    def change_name(self, new_name: str):
        self.name = new_name


s1 = Student()
s1.display_info()
s1.change_name("xya")
s1.display_info()