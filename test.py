from math import sqrt


def find_roots(a, b, c):
    delta = b**2 - 4 * a * c
    delta_sqrt = sqrt(delta)
    print()
    return (-b - delta_sqrt) / 2 / a, (-b + delta_sqrt) / 2 / a
print(find_roots(2, 10, 8));