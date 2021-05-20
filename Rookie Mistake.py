class Solution:
    def solve(self, s):
        flag = 1
        for el in s:
            if el == 'B':
                flag = 0
            if el == 'R' and flag == 1:
                return True
            if el == 'R':
                flag = 1
        if flag == 1:
            return True
        return False

