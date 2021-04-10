class Solution:
    def solve(heights):
        res = []
        if len(heights) == 0:
            return res
        maxx = heights[-1]

        res.append(len(heights) - 1)
        for i, height in enumerate(heights[::-1]):
            if maxx < height:
                maxx = height
                res.append(i)
        res = sorted(res)
        return res



    print(solve([2,1]))