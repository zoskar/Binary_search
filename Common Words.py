class Solution:
    def solve(self, s0, s1):
        s0 = set(list(s0.lower().split()))
        s1 = set(list(s1.lower().split()))
        return len({i for i in s0 if i in s1})
