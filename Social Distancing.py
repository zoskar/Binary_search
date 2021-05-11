class Solution:
    def solve(self, s, k):
        if s.count('x') != 0:

            if s.index('x') == k:
                return True
        else:
            return True
        previous = 0
        for el in s:
            if el == 'x':
                previous = 0
            elif el == '.':
                previous += 1
            if previous == 2 * k - 1:
                return True
        if previous == k:
            return True
        return False

