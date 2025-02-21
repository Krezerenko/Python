from math import log, tan


def main(y, z):
    enum1 = 16 * (log(29 * y**3 + 75 * z**2))**7 - y
    denom1 = (y**2 - 55 * z)**5 - (74 * z**2 - 1 - z**3 / 83)**6
    enum2 = (80 - y**3 - 16 * z)**4
    denom2 = 26 * (tan(1 - 42 * z))**7 + 47 * y
    return enum1 / denom1 + enum2 / denom2
