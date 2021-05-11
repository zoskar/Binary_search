class Solution:
    def solve(self, moves, x, y):
        yy = 0
        xx = 0
        for move in moves:
            if move == 'NORTH':
                yy += 1
            elif move == 'EAST':
                xx += 1
            elif move == 'WEST':
                xx -= 1
            elif move == 'SOUTH':
                yy -= 1
        return (x, y) == (xx, yy)
