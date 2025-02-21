def fast_mul(x, y):
    res = 0
    while x > 0:
        if x & 1:
            res += y
        x >>= 1
        y <<= 1
    return res

for x1 in range(0, 1000):
    for y1 in range(0, 1000):
        assert fast_mul(x1, y1) == x1 * y1