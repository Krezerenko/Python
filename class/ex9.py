class HTML:
    def __init__(self):
        self.code = []
        self.tags = []

    def __enter__(self):
        self.code.append(f"<{self.tags[-1]}>")

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.code.append(f"</{self.tags[-1]}>")
        self.tags.pop()

    def body(self):
        self.tags.append("body")
        return self

    def div(self):
        self.tags.append("div")
        return self

    def p(self, value):
        self.code.append(f"<p>{value}</p>")

    def get_code(self):
        return "\n".join(self.code)


html = HTML()
with html.body():
    with html.div():
        with html.div():
            html.p('Первая строка.')
            html.p('Вторая строка.')
        with html.div():
            html.p('Третья строка.')

print(html.get_code())