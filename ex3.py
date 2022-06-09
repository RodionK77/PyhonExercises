import math


def main(n, z, b, m):
    x = 0
    y = 0
    for i in range(1, n + 1):
        x += math.cos(i) + 16 * (math.sin(16 * z ** 3)) ** 2 + z ** 6
    for c in range(1, m + 1):
        for k in range(1, b + 1):
            y += k ** 6 + (52 * c + c ** 3 / 21) ** 3
    return x - y


print(main(7, -0.02, 2, 2))
