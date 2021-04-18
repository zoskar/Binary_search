class Solution:
    def solve(nums):
        flag = 0
        for el in nums:
            if el == 1 and flag == 0:
                flag = 1
            elif el != 1 and flag == 1:
                flag = 2
            elif el == 1 and flag == 2:
                return False
        return True
