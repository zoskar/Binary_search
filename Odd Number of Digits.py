class Solution:
    def solve(self, nums):
        res = 0
        for number in nums:
            if len(str(number)) % 2 == 1:
                res += 1
        return res
