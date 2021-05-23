class Solution:
    def solve(self, nums):
        res = 0
        t = sorted(nums)
        for i in range(len(nums)):
            if nums[i] == t[i]:
                res += 1
        return res
