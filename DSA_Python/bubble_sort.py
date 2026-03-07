nums = [5, 3, 1, 9, 2, 4, 4, 1, 8, 0]
n = len(nums)
for i in range(n-2, -1, -1):
    print (nums)
    for j in range(0, i+1):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
print (nums)