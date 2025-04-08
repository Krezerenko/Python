def main(x):
    starts = (0, 4, 14, 23, 28, 32)
    return [(f"H{i + 1}", hex(
        extract_part(x, starts[i], starts[i + 1])))
            for i in range(len(starts) - 1)]


def extract_part(x, start, end):
    mask = ~((-1) << (end - start))
    return (x >> start) & mask
