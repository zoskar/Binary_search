import math


class Solution:
    def solve(self, s):
        n = 2
        lenghts = []
        tmp = s
        flag = False
        numbers = []
        pointer = 0
        if len(s) < 2:
            return False
        while n != len(s)+1:

            for i in range(n):
                lenghts.append(math.ceil(len(tmp) / n))
                tmp = tmp[lenghts[-1] - 1::]
            for i, l in enumerate(lenghts):
                numbers.append(int(s[pointer:pointer + l]))
                pointer += l
            for i in range(len(numbers) - 1):
                if numbers[i] != numbers[i + 1] + 1:
                    flag = False
                    break
                flag = True
            if flag is True:
                return True
            tmp = s
            numbers = []
            pointer = 0
            lenghts = []
            n += 1

        return False


print(Solution.solve(Solution,"12"))





