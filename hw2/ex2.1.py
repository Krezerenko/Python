from math import sin, cos, tan, atan


def main(y):
    if y < 102:
        return 59 * y**2 - 90 - 7 * cos(19 * y**2)**4
    if y < 162:
        return 1 - (76 * y**2)**5 / 90 - 8 * tan(y)**4
    if y < 246:
        return sin(y)**5
    if y < 273:
        return y**7 / 80 - 68 * (y + 13 * y**2)**6 - 1
    return 58 * atan(58 + y**2 + y / 25) + 78 + (int(y))**6 / 33
