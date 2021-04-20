class Solution:
    def solve(nums):
        nums = sorted(nums)
        l = len(nums)
        diff = abs(int((nums[-1] - nums[0]) / l))
        if diff == 0:
            return nums[0]
        for i, num in enumerate(nums[:-1:]):
            if nums[i + 1] - nums[i] != diff:
                return num + diff
