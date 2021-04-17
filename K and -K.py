class Solution:
    def solve(nums):
        nums = sorted(nums)
        i = 0
        j = 1
        while i < len(nums) - j + 1:
            if abs(nums[i]) == 0 or nums[-j] == 0:
                return 0

            if nums[i] > 0:
                break
            if nums[-j] < 0:
                break

            if abs(nums[i]) > nums[-j]:
                i += 1
            elif abs(nums[i]) < nums[-j]:
                j += 1
            else:
                return nums[-j]
        return -1
