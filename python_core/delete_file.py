import os
import shutil

if os.path.exists("hello.txt"):
    os.remove("hello.txt")
    print ("File removed")
else:
    print ("File not found")

# deleting empty dir
if os.path.exists("test1"):
    os.rmdir("test1")
    print ("Directory deleted")
else:
    print ("Dir not found")

#deleting dir and its contents
if os.path.exists("testdir2"):
    shutil.rmtree("testdir2")
    print("Directory and its contents deleted")
else:
    print ("Directory doesn't exists")
