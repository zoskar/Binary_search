class Solution:
    def solve(self, n):
        res = 1
        for i in range(n):
            res *= i + 1
        return res
