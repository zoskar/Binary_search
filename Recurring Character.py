class Solution:
    def solve(self, s):
        secik = set()
        for i, el in enumerate(s):
            if el in secik:
                return i
            secik.add(el)
        return -1
