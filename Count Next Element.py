class Solution:
    def solve(self, nums):
        numbers = set(nums)
        res = 0
        for el in nums:
            if el + 1 in numbers:
                res += 1
        return res
