import math


def main(z):
    if z < 96:
        return z
    elif 96 <= z < 194:
        return 78 * z ** 2 + 1 + z ** 5
    elif 194 <= z < 253:
        return math.log2(z ** 3) ** 6
    elif z >= 253:
        return 73 * math.cos(z) ** 4


print(main(250))
