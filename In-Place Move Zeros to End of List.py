class Solution:
    def solve(self, nums):
        i = 0
        res = []
        for num in nums:
            if num != 0:
                res.append(num)
            else:
                i += 1
        for i in range(i):
            res.append(0)
        return res
