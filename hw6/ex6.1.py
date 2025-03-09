def main(d):
    f = get_f(d)
    y = get_y(f)
    x = get_x(d)
    n = get_n(x)

    return len(y) * len(n) - sum(n)


def get_f(d):
    f = set()
    for d_ in d:
        if not ((d_ >= -75) != (d_ < 55)):
            continue
        f.add(3 * d_)
    return f


def get_y(f):
    y = set()
    for f_ in f:
        if not ((f_ <= -82) or (f_ > 69)):
            continue
        y.add(dceil(f_, 6) - f_)
    return y


def get_x(d):
    x = set()
    for d_ in d:
        if not ((d_ < -84) or (d_ >= 0)):
            continue
        x.add(d_**2 - d_**3)
    return x


def get_n(x):
    n = set()
    for x_ in x:
        if not ((x_ < 45) != (x_ > -75)):
            continue
        n.add(x_ - x_ // 5)
    return n


def dceil(n, divisor):
    return (n % divisor != 0) + n // divisor
