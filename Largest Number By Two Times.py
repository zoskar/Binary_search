class Solution:
    def solve(self, nums):
        big = -1
        bigger = -1
        for num in nums:
            if num > bigger:
                big = bigger
                bigger = num
            elif num > big:
                big = num

        return bigger > 2 * big