import os
if os.path.exists("hello2.txt"):
    os.rename("hello2.txt", "hello3.txt")
    print ("File renamed")
else:
    print ("File not found")