class Solution:
    def solve(self, prices):
        if len(prices) == 0:
            return 0
        lowest = prices[0]
        profit = 0
        for el in prices:
            if el < lowest:
                lowest = el
            if el - lowest > profit:
                profit = el - lowest
        return profit


