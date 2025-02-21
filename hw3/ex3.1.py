def main(a, p, b, n, y):
    res = 0
    for c in range(1, a + 1):
        res += (c + c**3)**3 - p**7
    for k in range(1, n + 1):
        for i in range(1, a + 1):
            for c in range(1, b + 1):
                res += (26 * y**3 + i**2)**3 + 69 * (46 * c**2 - 3 * k)
    return res

print(main(6, 0.63, 8, 5, 0.53))