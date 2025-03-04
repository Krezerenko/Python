import math


def main(z):
    i = 0
    res = 0
    for el in z:
        i += 1
        res += (80 - z[math.ceil(i/2) - 1]**3 - 16 * z[math.ceil(i/2) - 1])**4

    return res
