class Solution:
    def solve(self, nums):
        nums = sorted(nums)
        res = 0
        m = min(nums)
        for num in nums[1::]:
            res += num - m
        return res