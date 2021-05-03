class Solution:
    def solve(self, matrix):
        matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
        # for line in matrix:
        #     line = sorted(line)
        #     print(line)
        for i,line in enumerate(matrix):
            matrix[i] = sorted(line)
        matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
        return matrix