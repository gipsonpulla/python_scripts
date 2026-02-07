""" def add(*args, **kwargs):
    for k, v in kwargs.items():
        print (k, v)

add("a", 5, b=5, d=4)
 """
""" def display(n, m):
    print (f"{n=}")
    print (f"{m=}")

display(5, 2)
 """

check_even = lambda num: num % 2 == 0

print (check_even(100))
if check_even(100):
    print ("True")
else:
    print ("False")

