def args(n1, n2, n3, *args1, **kargs2):
    print (f"{n1=}")
    print (f"{n3=}")
    print (f"{n3=}")
    print (f"{args1= }")
    print (f"{kargs2=}")
    for k, v in kargs2.items():
        print (k, kargs2[k])

args(1, 3, 5, 343, 34, 78, name="Gipson")