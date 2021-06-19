class Solution:
    def solve(self, nums):
        if nums[0] > nums[1]:
            return False

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return False

        return True
