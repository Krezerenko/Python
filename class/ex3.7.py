def mul_bits(x, y, bits):
    x &= ((1 << bits) - 1)
    y &= ((1 << bits) - 1)
    return x * y

def mul16(x, y):
    return mul_bits(x, y, 8) + \
        (mul_bits(x >> 8, y, 8) << 8) + \
        (mul_bits(x, y >> 8, 8) << 8) + \
        (mul_bits(x >> 8, y >> 8, 8) << 16)

for x1 in range(0, 2**8):
    for y1 in range(0, 2**8):
        assert mul16(x1, y1) == x1 * y1