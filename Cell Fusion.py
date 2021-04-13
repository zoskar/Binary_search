import  bisect
class Solution:
    def solve(cells):
        cells = sorted(cells)
        while len(cells) > 1:
            if cells[-2] == cells[-1]:
                del (cells[-1])
                del (cells[-1])
            else:
                tmp = int((cells[-1] + cells[-2]) / 3)
                del (cells[-1])
                del (cells[-1])
                if len(cells) == 0:
                    cells.append(tmp)
                    break
                bisect.insort(cells, tmp)
        if len(cells) == 1:
            return cells[-1]
        else:
            return -1

    cells = [1, 1, 2, 4]
    solve(cells)





