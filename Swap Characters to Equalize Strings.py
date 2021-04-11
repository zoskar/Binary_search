import string


class Solution:
    def solve(self, s, t):
        d = dict.fromkeys(string.ascii_lowercase, 0)
        for char in s:
            d[char] += 1
        for char in t:
            d[char] += 1

        for letter in d:
            if d[letter] % 2 != 0:
                return False
        return True


