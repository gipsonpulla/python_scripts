nums = [5, 3, 1, 9, 2, 4, 4, 1, 8, 0]
n = len(nums)
for i in range(0, n):
    min_index = i
    for j in range(i+1, n):
        if nums[j] < nums[min_index]:
            min_index = j
    nums[i], nums[min_index] = nums[min_index], nums[i]
print (nums)
