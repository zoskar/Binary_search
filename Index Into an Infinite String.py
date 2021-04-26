class Solution:
    def solve(self, s, i, j):
        res = ''
        diff = j-i
        start = i%len(s)
        for num in range(diff):
            res += s[(start+num)%len(s)]
        return res
Solution.solve(Solution, 'zvcM', 653, 663)