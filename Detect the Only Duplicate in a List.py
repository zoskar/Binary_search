class Solution:
    def solve(nums):
        secik = set()
        for i,num in enumerate(nums):
            secik.add(num)
            if len(secik) != i - 1:
                return num
