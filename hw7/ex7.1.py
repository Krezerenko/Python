def main(x):
    tree = {1982: (1, {1983: (2, {"XTEND": 0, "NIT": 1, "KICAD": 2}),
                       1985: (3, {"XS": 3, "PERL6": 4}),
                       2018: (3, {"XS": 5, "PERL6": 6})}),
            1986: (3, {"XS": (2, {"XTEND": 7, "NIT": 8, "KICAD": 9}),
                       "PERL6": 10}),
            2010: 11}
    choice = (0, tree)
    while type(choice) is tuple:
        choice = choice[1][x[choice[0]]]
    return choice
