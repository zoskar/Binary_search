class Solution:
    def solve(self, nums):
        even = []
        odd = []
        res = []
        for el in nums:
            if el % 2 == 0:
                even.append(el)
            else:
                odd.append(el)
        even = sorted(even)
        odd = sorted(odd, reverse=True)
        for el in nums:
            if el % 2 == 0:
                res.append(even.pop(0))
            else:
                res.append(odd.pop(0))
        return res
