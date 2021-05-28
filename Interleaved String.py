class Solution:
    def solve(self, s0, s1):
        res = []
        j = min(len(s0), len(s1))
        for i in range(j):
            res.append(s0[i])
            res.append(s1[i])

        res.append(s0[j:])
        res.append(s1[j:])

        return ''.join(res)
