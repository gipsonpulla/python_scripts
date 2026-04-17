#recursion using factorial
num = int(input("Enter the factorial number"))
def func(num):
    if num == 1:
        return 1
    return num * func(num-1)

print (func(num))