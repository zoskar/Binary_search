class Solution:
    def solve(self, x, y):
        res = 0
        a = str((bin(x)))[2::]
        b = str((bin(y)))[2::]

        for i in range(32 - len(a)):
            a = '0' + a
        for i in range(32 - len(b)):
            b = '0' + b
        for i in range(32):
            if a[i] != b[i]:
                res += 1
        return res


