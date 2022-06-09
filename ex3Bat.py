import math


def main(b, m, a):
    x = 0
    y1 = 0
    y2 = 1
    for j in range(1, b + 1):
        x += 31 * math.atan(j) + (1 + 13 * j ** 2 + 17 * j ** 3) ** 3
    for i in range(1, a + 1):
        for c in range(1, m + 1):
            for j in range(1, b + 1):
                y1 += 99 * c + 48 * (math.tan(c)) ** 4 + \
                      83 * (i ** 3 + 14 + 89 * j ** 2) ** 7
        y2 *= y1
        y1 = 0

    return x + y2
