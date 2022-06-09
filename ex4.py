import math


def main(x):
    f = 0
    for i in range(len(x)):
        f += (math.cos(x[-1 - i // 2])) ** 2
    return 32 * f


print(main(9))
