class Solution:
    def solve(self, nums):
        i = 0
        while i < len(nums):
            try:
                nums[i], nums[i + 2] = nums[i + 2], nums[i]
                nums[i + 1], nums[i + 3] = nums[i + 3], nums[i + 1]
                i += 4
            except IndexError:
                break
        return nums

