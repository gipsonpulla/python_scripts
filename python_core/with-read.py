#With Keyword
# with open('hello.txt', 'r') as f:
#     #print (f.read())
#     x = f.read()
#     #letters = [ch for ch is x.isupper():
#     for ch in x:
#         if ch.isupper():
#             print (ch)

with open("hello.txt", "r") as f:
    for line in f:
        print (line.strip())