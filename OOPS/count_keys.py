list1 = [5, 3, 6, 2, 5, 5, 7, 9, 3, 2, 0, 1, 6, 1, 1, 1]
n = len(list1)
dict1 = dict()
for i in range(0, n):
    dict1[list1[i]] = dict1.get(list1[i], 0) + 1
print (dict1)

dict2 = dict()
for i in range(0, n):
    if list1[i] in dict2:
        dict2[list1[i]] += 1
    else:
        dict2[list1[i]] = 1

dict2 = {key: dict2[key] for key in sorted(dict2)}
print(dict2)
print (sorted(dict2))