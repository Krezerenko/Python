vals = [0.24]


def main(n):
    global vals
    for i in range(len(vals), n):
        vals.append(vals[i - 1]**3 + 4 * vals[i - 1]**2)
    return vals[n - 1]**3 + 4 * vals[n - 1]**2
