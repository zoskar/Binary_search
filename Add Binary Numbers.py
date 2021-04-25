class Solution:
    def solve(self, a, b):
        res = ''
        carry = 0
        diff = abs(len(a)-len(b))

        if len(a) > len(b):
            for i in range(diff):
                b = '0' + b
        if len(b) > len(a):
            for i in range(diff):
                a = '0' + a

        for i in range(1, len(a)+1):
            if int(a[-i]) == 0 and int(b[-i]) == 0:
                if carry == 0:
                    res = '0' + res
                elif carry == 1:
                    res = '1' + res
                    carry = 0
            elif int(a[-i]) + int(b[-i]) == 1:
                if carry == 0:
                    res = '1' + res
                elif carry == 1:
                    res = '0' + res
            elif int(a[-i]) + int(b[-i]) == 2:
                if carry == 0:
                    carry = 1
                    res = '0' + res
                elif carry == 1:
                    res = '1' + res

        if carry == 1:
            res = '1' + res

        return res



print(Solution.solve(Solution,'11','1'))