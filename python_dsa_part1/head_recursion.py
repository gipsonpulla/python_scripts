def namep(count=0):
    #global count
    if count == 4:
        return
    else:
        print("Gips")
        count += 1
        namep(count)

namep()
