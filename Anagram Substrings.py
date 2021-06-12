class Solution:
    def solve(self, s0, s1):
        l = len(s0)
        res = 0
        subs = []
        s0 = sorted(s0)
        for i in range(len(s1) - l + 1):
            subs.append(s1[i:i + l])
        for sub in subs:
            if len(sub) != l:
                continue
            if sorted(sub) == s0:
                res += 1

        return res