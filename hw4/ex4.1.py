def main(n):
    if n == 0:
        return 0.24
    return main(n - 1)**3 + 4 * main(n - 1)**2
