class Solution:
    def solve(self, n):
        res = []
        flag = 1
        for i in range(2,n+1):
            for j in range(2,i):
                if i % j == 0:
                    flag = 0
                    break
            if flag == 1:
                res.append(i)
            flag = 1
        return res

print(Solution.solve(Solution, 3))