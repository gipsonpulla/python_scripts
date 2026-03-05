class Solution:
    def func(self, num):
        if num == 0 or num == 1:
            return num
        return self.func(num - 1) + self.func(num - 2)

    def fibonacci(self, num: int) -> int:
        return self.func(num)

num = int(input("Enter the number: "))
number = Solution()
print (number.fibonacci(num))