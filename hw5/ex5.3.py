from functools import reduce


def main(z):
    res = 2 * f(z[0])
    res += reduce(lambda _, el: 2 * f(el), z[:len(z)//2])
    res += f(z[len(z) // 2]) * (len(z) % 2)
    return res


def f(el):
    return (80 - el**3 - 16 * el)**4
