def main(x):
    shifts = (4, 10, 9, 5, 4)
    ans = []
    for num, shift in enumerate(shifts):
        x, part = extract_part(x, shift)
        ans.append((f"H{num + 1}", hex(part)))
    return ans


def extract_part(x, shift):
    mask = ~((-1) << shift)
    return x >> shift, x & mask
