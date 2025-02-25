def main(n):
    result = 0.24
    for _ in range(n):
        result = result**3 + 4 * result**2
    return result
