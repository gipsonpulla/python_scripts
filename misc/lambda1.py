length = int(input("Enter the integer"))

make_list = lambda n: [i for i in range(0, n+1)]
list1 = make_list(length)
list2 = make_list(55)

print (f"{list1= }")
print (f"{list2= }")

check_even = lambda n: n %2 ==0

check_even(100)

check_even2 = lambda n : print("Even") if n %2 == 0 else print("Odd")

check_even2(100)