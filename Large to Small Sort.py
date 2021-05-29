class Solution:
    def solve(self, nums):
        nums = sorted(nums, reverse=True)
        res = []
        while len(nums) > 1:
            res.append(nums[0])
            res.append(nums[-1])
            del(nums[0])
            del(nums[-1])
        if len(nums) == 1:
            res.append(nums[0])
        return res