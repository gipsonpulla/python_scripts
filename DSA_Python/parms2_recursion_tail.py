def func2(m , n):
    if m > n:
        return
    func2(m+1, n)
    print("Gipson")

func2(1, 5)

#fun to print n to 1
def func3(n):
    if n == 0:
        return
    print ("Pulla")
    func3(n-1)

func3(5)