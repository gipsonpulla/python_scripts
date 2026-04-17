nums = [5, 3, 1, 9, 2, 4, 4, 1, 8, 0]
n = len(nums)
for i in range(n):
    max_index = i
    for j in range(i+1, n):
        if nums[j] > nums[max_index]:
            max_index = j
    nums[i], nums[max_index] = nums[max_index], nums[i]
print (nums)