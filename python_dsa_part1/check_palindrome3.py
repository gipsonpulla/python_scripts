# without recursion
string = str(input("Enter the string to check the palindrom"))

print (string)

right = len(string) - 1
left = 0

while left < right:
    if string[left] != string[right]:
        print ("not palindrome")
        break
    left += 1
    right -= 1
else:
    print ("Palindrome")




