class Solution:
    def solve(self, nums):
        if len(nums) == 0:
            return 0
        res = 0
        if nums[0] == 1:
            res += 1
        current = nums[0]
        for num in nums:
            if current != num:
                res += 1
                current = 1 - current
        return res