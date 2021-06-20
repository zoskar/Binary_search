class Solution:
    def solve(self, a):
        product = 1
        i = 1
        while product <= a:
            i += 1
            product *= i

            if product == a:
                return i

        return -1