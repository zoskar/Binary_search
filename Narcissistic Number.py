class Solution:
    def solve(self, n):
        summ = 0
        for digit in str(n):
            summ += int(digit) ** len(str(n))
        return n == summ
