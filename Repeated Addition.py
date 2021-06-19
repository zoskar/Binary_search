class Solution:
    def solve(self, n):
        summ = 0
        while True:
            for digit in str(n):
                summ += int(digit)
            if summ < 10:
                return summ
            n = summ
            summ = 0