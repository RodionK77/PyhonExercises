import math


def main(x):
    x = math.sqrt(((1 - ((x ** 2) / 21) - x ** 3) ** 7 +
                   (68 * x ** 2 - 1) ** 2) /
                  (49 * (math.asin(x) ** 4))) - \
        ((5 * (abs(62 * x)) ** 5) / (50 * x ** 5))
    return x


print(main(0.57))
