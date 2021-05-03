class Solution:
    def solve(self, matrix):
        for i, line in enumerate(matrix):
            line = line[::-1]
            for j, el in enumerate(line):
                matrix[i][j] = 1 - el
        return matrix
