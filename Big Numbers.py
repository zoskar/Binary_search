import operator
class Solution:
    def solve(self, matrix):
        res = 0
        m = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
        for i, line in enumerate(matrix):
            index, value = max(enumerate(line), key=operator.itemgetter(1))
            counter = line.count(value)
            line[index] = -1
            if counter > 1:
                matrix.insert(i+1, line)
            if value == max(m[index]):
                res += 1
        return res



matrix = [
    [1, 1],
    [1, 4]
]
print(Solution.solve(Solution, matrix))
