import math
from collections import Counter


class Solution:
    def solve(self, nums):
        c = Counter(nums)
        res = 0
        for _, val in c.items():
            res += math.comb(val, 2)
        return res


print(Solution.solve(Solution, [3, 2, 3, 2, 2]))