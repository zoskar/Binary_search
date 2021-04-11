class Solution:
    def solve(self, s):
        prev = ''
        res = ''
        for char in s:
            if char != prev:
                res += char
            prev = char
        return res
