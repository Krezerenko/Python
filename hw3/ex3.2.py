def main(a, p, b, n, y):
    res = 0
    res += sum((c + c**3)**3 - p**7 for c in range(1, a + 1))
    res += sum((26 * y**3 + i**2)**3 + 69 * (46 * c**2 - 3 * k)
               for c in range(1, b + 1)
               for i in range(1, a + 1)
               for k in range(1, n + 1))

    return res
