def fast_pow(x, y):
    res = 1
    while y > 0:
        if y & 1:
            res *= x
        y >>= 1
        x *= x
    return res

for x1 in range(0, 1000):
    for y1 in range(0, 1000):
        assert fast_pow(x1, y1) == x1 ** y1