﻿def main(a, p, b, n, y):
    return (
            a**10 / 10 + a**9 / 2 + (9 * a**8) / 8 + (1 / 7) * a**7 * b * n
            + (3 * a**7) / 2 + (1 / 2) * a**6 * b * n + (31 * a**6) / 20
            + (78 / 5) * a**5 * b * n * y**3 + (1 / 2) * a**5 * b * n
            + (3 * a**5) / 2 + 39 * a**4 * b * n * y**3 + (9 * a**4) / 8
            + 676 * a**3 * b * n * y**6 + 26 * a**3 * b * n * y**3
            - (1 / 6) * a**3 * b * n + a**3 / 2 + 1014 * a**2 * b * n * y**6
            + a**2 / 10 + 1058 * a * b**3 * n + 1587 * a * b**2 * n
            - (207 / 2) * a * b * n**2 + 17576 * a * b * n * y**9
            + 338 * a * b * n * y**6 - (13 / 5) * a * b * n * y**3
            + (8936 * a * b * n) / 21 - a * p**7
    )
