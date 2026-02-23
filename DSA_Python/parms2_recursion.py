# sample recursion to print the m to n times
def func1(m, n):
    if m == n:
        return
    print ("Gips")
    func1(m+1, n)

func1(1, 5) 