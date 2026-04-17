count = 0
def func1():
    global count
    if count == 4:
        return
    count += 1
    func1()
    print ("Gips")

func1()