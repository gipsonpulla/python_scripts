""" def print_num(N, n):
    for i in range(0, n):
        print (N)
print_num(15, 5)
 """

def print_num1(N, n):
    if n == 0:
        return
    print(N)
    print_num1(N, n-1)

print_num1(15, 5)