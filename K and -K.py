def solve(n):
        sequence = []
        sequence.append(n)
        while sequence[-1] != 1:
            if sequence[-1] % 2 == 0:
                sequence.append(n / 2)
            else:
                sequence.append(3 * n + 1)
        return len(sequence)





