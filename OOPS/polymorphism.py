class Animal:
    def sound(self):
        print ("Animal speaking")

class Dog(Animal):
    def sound(self):
        print("bhaw bhaw bhaw")

class Cat(Animal):
    def sound(self):
        print("meow meow meow")

obj = Dog()
obj.sound()
obj = Cat()
obj.sound()