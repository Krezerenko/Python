def main(d):
    f = get_f(d)
    y = get_y(f)
    x = get_x(d)
    n = get_n(x)

    return len(y) * len(n) - sum(n)


def get_f(d):
    return {3 * d_ for d_ in d if (d_ >= -75) != (d_ < 55)}


def get_y(f):
    return {dceil(f_, 6) - f_ for f_ in f if (f_ <= -82) or (f_ > 69)}


def get_x(d):
    return {d_**2 - d_**3 for d_ in d if (d_ < -84) or (d_ >= 0)}


def get_n(x):
    return {x_ - x_ // 5 for x_ in x if (x_ < 45) != (x_ > -75)}


def dceil(n, divisor):
    return (n % divisor != 0) + n // divisor
