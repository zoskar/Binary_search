class Solution:
    def solve(self, n):
        result = 1
        while n != 1:
            if n % 2 == 0:
                n = n / 2
            else:
                n = 3 * n + 1
            result += 1

        return result