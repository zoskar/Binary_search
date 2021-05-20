class Solution:
    def solve(self, nums):
        coll = Counter(nums)
        for el in coll:
            if coll[el] % 2 != 0:
                return False
        return True
