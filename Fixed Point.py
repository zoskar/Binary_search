class Solution:
    def solve(self, nums):
        for i, num in enumerate(nums):
            if num == i:
                return i
        return -1

