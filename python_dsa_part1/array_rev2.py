def func(arr, left, right):
    if left >= right:
        return
    arr[left], arr[right] = arr[right], arr[left]
    func(arr, left+1, right-1)

def revArray(arr):
    right = len(arr)
    left = 0
    func(arr, left, right-1)
    print (arr)

arr = [4, 3, 6, 0, 1, 3, 7, 8, 9, 12, 15]
revArray(arr)    