from math import sin, cos, tan, atan


def main(y):
    conditions = [
        y < 102,
        (102 <= y) and (y < 162),
        (162 <= y) and (y < 246),
        (246 <= y) and (y < 273),
        y >= 273
    ]
    functions = [
        lambda x: 59 * x**2 - 90 - 7 * cos(19 * x**2)**4,
        lambda x: 1 - (76 * x**2)**5 / 90 - 8 * tan(x)**4,
        lambda x: sin(x)**5,
        lambda x: x**7 / 80 - 68 * (x + 13 * x**2)**6 - 1,
        lambda x: 58 * atan(58 + x**2 + x / 25) + 78 + (int(x))**6 / 33
    ]

    return functions[conditions.index(True)](y)
