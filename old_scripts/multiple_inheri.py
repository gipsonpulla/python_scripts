# Base class 1
class Mother:
    mothername = "Mary"

    def __init__(self):
        print(self.mothername)

# Base class 2
class Father:
    fathername = "Joseph"

    def __init__(self):
        print(self.fathername)

# Derived class
class Son(Mother, Father):
    def __init__(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)
        Father.__init__(self)

# Driver code
s1 = Son()
s1.fathername = "RAM"
s1.mothername = "SITA"
#s1.parents()