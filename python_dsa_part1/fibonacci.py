# fibonacci numbers
def fib(num):
    a, b = 0, 1

    for i in range(num):
        print (a, end=" ")
        a, b = b, a + b
    return a

print (fib(5))

#using while loop
num = int(input("Enter the number: "))
a, b = 0, 1
while (a < num):
    print(a, end=" ")
    a, b = b, a + b