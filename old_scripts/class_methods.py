#!/usr/bin/python3

class Student:
    def __init__(self, name, age, gender) -> None:
        self.name = name
        self.age = age
        self.gender = gender

    def display(self):
        print (f"My name is = {self.name}")
        print (f"My age is = {self.age}")
        print (f"My genger is = {self.gender}")

    @classmethod
    def create_student_using_parms(cls, name, age, gender):
        obj = cls(name, age, gender)
        return obj
    
    @classmethod
    def create_student_using_file(cls, filename):
        f = open(filename, "r",)
        student_data = f.read()
        name, age, gender = student_data.split()
        f.close()
        obj = cls(name, age, gender)
        return obj

obj1 = Student.create_student_using_parms("Gips", 34, "M")
obj1.display()
obj2 = Student.create_student_using_file("student.txt",)
obj2.display()