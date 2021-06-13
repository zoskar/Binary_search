class Solution:
    def solve(self, s):
        res = ''
        number = 0
        for i, el in enumerate(s):
            if el.isdigit():
                if not s[i+1].isdigit():
                    number *= 10
                    number += int(el)
                    res += s[i + 1] * number
                    number = 0
                else:
                    number *= 10
                    number += int(el)

        return res

print(Solution.solve(Solution, '1a2b'))