def main(z, i=0, res=0):
    if i == len(z) // 2:
        res += f(z[len(z) // 2]) * (len(z) % 2)
        return res
    return main(z, i + 1, res + 2 * f(z[i]))


def f(el):
    return (80 - el**3 - 16 * el)**4
