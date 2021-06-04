class Solution:
    def solve(self, nums):
        if len(nums) > 2:
            a = min(nums)
            m = max(nums)

            nums.remove(m)
            nums.remove(a)
            b = min(nums)
            n = max(nums)
        else:
            return nums[0] * nums[1]
        return max(a * b, a * m, a * n, b * m, b * n, m * n)
