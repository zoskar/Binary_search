class Solution:
    def solve(self, nums):

        if len(nums) < 2:
            return True

        prev = nums[0]
        flag = nums[-1] - nums[0]
        if flag == 0:
            return False
        for el in nums[1::]:
            if el == prev:
                return False
            if flag > 0:
                if el < prev:
                    return False
            else:
                if el > prev:
                    return False
            prev = el
        return True