def main(x):
    if x[0] == 1982:
        return branch1(x)
    elif x[0] == 1986:
        return branch2(x)
    elif x[0] == 2010:
        return branch3(x)
    return None


def branch1(x):
    if x[1] == 1983:
        return branch1_1(x)
    elif x[1] == 1985:
        return branch1_2(x)
    elif x[1] == 2018:
        return branch1_3(x)


def branch1_1(x):
    if x[2] == "XTEND":
        return 0
    elif x[2] == "NIT":
        return 1
    elif x[2] == "KICAD":
        return 2


def branch1_2(x):
    if x[3] == "XS":
        return 3
    elif x[3] == "PERL6":
        return 4


def branch1_3(x):
    if x[3] == "XS":
        return 5
    elif x[3] == "PERL6":
        return 6


def branch2(x):
    if x[3] == 'XS':
        if x[2] == "XTEND":
            return 7
        elif x[2] == "NIT":
            return 8
        elif x[2] == "KICAD":
            return 9
    else:
        return 10


def branch3(x):
    return 11
