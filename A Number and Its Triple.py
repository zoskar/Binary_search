class Solution:
    def solve(self, nums):
        zeros = nums.count(0)
        if zeros > 1:
            return True
        secik = set(nums)
        for el in secik:
            if el * 3 in secik and el != 0:
                return True
        return False



