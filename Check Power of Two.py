class Solution:
    def solve(self, n):
        res = 0
        while (True):
            if 2 ** res > n:
                return False
            if 2 ** res == n:
                return True
            res += 1
