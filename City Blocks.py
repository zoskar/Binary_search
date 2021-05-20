class Solution:
    def solve(self, matrix, blocks):
        res = 0
        l = 0
        r = 0
        for block in blocks:
            for i, line in enumerate(matrix):
                try:
                    tmp = line.index(block)
                    res += abs(tmp - l)
                    l = tmp
                    res += abs(i - r)
                    r = i
                    break
                except:
                    continue
        return res

