class Solution:
    def solve(self, n):
        past = []
        while True:

            if n == 1:
                return True
            if n in past:
                return False

            past.append(n)
            summ = 0
            for digit in str(n):
                summ += int(digit)**2
            n = summ