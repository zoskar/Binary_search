class Solution:
    def solve(s, c):
        indexes = []
        res = []
        flag = 0
        for i, char in enumerate(s):
            if char == c:
                indexes.append(i)
        k = 0
        for i, char in enumerate(s):
            prev = abs(indexes[k] - i)
            if k < len(indexes) -1:
                next = abs(indexes[k+1] - i)
                res.append(min(prev, next))
            else:
                res.append(prev)

            if res[-1] == 0:
                if flag == 1:
                    k += 1
                flag = 1




