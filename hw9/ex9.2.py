import re


def main(text):
    text = text.replace("\n", " ")
    sections = re.split(r"<sect>\s*opt (.*?)\s*</sect>,?",
                        re.sub(r"\s*\|\|\s*(.*)\s*\|\|\s*",
                               r"\1", text))[1::2]
    pairs = [tuple(re.split(r"\s*:=\s*#\(\s*(.*)\s*\);", section)[:-1])
             for section in sections]
    pairs = [(a.strip(), b.strip().replace('`', '').split(" . "))
             for a, b in pairs]
    return pairs
