class Solution:
    def solve(self, s):
        letter = s[0]
        res = ''
        i = 0
        while len(s) > 0:
            if letter == s[0]:
                i += 1
                s = s[1::]
                if len(s) == 0:
                    res += str(i) + letter
            else:
                res += str(i) + letter
                i = 0
                letter = s[0]
        return res
s = "aaaabbbccdaa"
print(Solution.solve(Solution, s))