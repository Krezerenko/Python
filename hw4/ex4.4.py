from functools import reduce


def main(n):
    return reduce(lambda x, _: x**3 + 4*x**2, range(n), 0.24)
