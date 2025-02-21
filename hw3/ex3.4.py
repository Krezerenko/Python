def main(a, p, b, n, y):
    return f1(0, a, p) + f2(0, b, a, n, y)


def f1(res, c, p):
    if c == 0:
        return res
    return f1(res + (c + c**3)**3 - p**7, c - 1, p)


def f2(res, b, i, n, y):
    if i == 0:
        return res

    return f2(res + a2(b, i, n, y), b, i - 1, n, y)


def a2(b, i, n, y):
    return b * n * (26 * y**3 + i**2)**3 + \
        69 * (n * 46 * square_sum(b) - 3 * b * lin_sum(n))


def square_sum(n):
    return n * (n + 1) * (2 * n + 1) // 6


def lin_sum(n):
    return n * (n + 1) // 2
