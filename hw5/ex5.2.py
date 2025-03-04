import math


def main(z):
    return sum([(80 - z[math.ceil(i/2) - 1]**3 - 16 * z[math.ceil(i/2) - 1])**4
                for i in range(1, len(z) + 1)])
