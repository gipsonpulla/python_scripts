def check_palindrome(string, left, right):
    if left >= right:
        return True
    if string[left] != string[right]:
        return False
    return check_palindrome(string, left + 1, right - 1)

string = input("Enter the string: ")

if check_palindrome(string, 0, len(string)-1):
    print("Palindrome")
else:
    print("Not a palindrome")