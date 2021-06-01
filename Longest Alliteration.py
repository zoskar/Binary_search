class Solution:
    def solve(self, words):
        res = 0
        current = 1
        prev = ''
        for word in words:
            if word[0] == prev:
                current += 1
            else:
                current = 1

            if current > res:
                res = current

            prev = word[0]
        return res