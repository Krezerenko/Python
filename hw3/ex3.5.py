def f(a, p, b, n, y):
    cache = {}

    def get_cached_value(key, func):
        if key not in cache:
            cache[key] = func()
        return cache[key]

    first_sum = sum(get_cached_value(c, lambda: (c + c**3)**3 - p**7)
                    for c in range(1, a + 1))

    second_sum = 0
    for k in range(1, n + 1):
        for i in range(1, a + 1):
            for c in range(1, b + 1):
                key = (k, i, c)
                second_sum += get_cached_value(key,
                                               lambda:
                                               (26 * y**3 + i**2)**3 +
                                               69 * (46 * c**2 - 3 * k))

    return first_sum + second_sum
