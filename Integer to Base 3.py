class Solution:
   def solve(self, n):
        if n < 3:
            return str(n)
        s = ''
        while n != 0:
            s = str(n%3) + s
            n = n//3
        return s
Solution.solve(Solution, 10)