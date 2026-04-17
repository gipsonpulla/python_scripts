def check_palindrome(string, left, right):
    if left >= right:
        print ("Palindrome")
        return
    if string[left] == string[right]:
        check_palindrome(string, left +1 , right -1)
    else:
        print ("Not a palindrome")
        return

string: str = input("Enter the string: ")

def func(string):
    right = len(string) - 1
    left = 0
    check_palindrome(string, left, right)

func(string)