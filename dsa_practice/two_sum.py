#find the sum of two integers in the array are 
#equal to the target

def twosum(arr, target):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == target:
                return [i, j]
    return False

if __name__ == "__main__":
    arr = [0, -1, 2, -3, 1]
    target = -2
    indices = twosum(arr, target)
    if indices:
        print (indices)
    else:
        print("false")