def add (n1, n2):
    total = n1 + n2
    return total

a = int(input("Enter the number 1"))
b = int(input("Enter the number 2"))
c = add (a, b)

def check(n):
    if n%2 == 0:
        print ("even")
    else:
        print ("odd")

check (c)