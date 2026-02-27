#print the factorial of the given number
def fact1(num):
    if num == 0:
        return
    fact1(num - 1)
    print (num * (num-1))

fact1(5)