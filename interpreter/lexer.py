import re

class Token:
    def __init__(self, type, value):
        self.type=type
        self.value=value
class Lexer:
    def tokenize(self):
        for mo in self.REGULAR_EXPR.finditer(self.text):
            kind = mo.lastgroup
            value = mo.group()
            if kind == "SPACE":
                continue
            if kind == "OTHER":
                raise SyntaxError(f"Неожиданный символ({value})")
            yield Token(kind, value)


    def __init__(self, text):
        self.text = text
        TOKENS = [
            ('NUMBER', r'\d+(\.\d*)?'),
            ('SUM', r'\+'),
            ('DIV', r'\/'),
            ('MUL', r'\*'),
            ('MINUS', r'\-'),
            ('BRACKET_START', r'\('),
            ('BRACKET_END',r'\)'),
            ('SIN', r'sin\('),
            ("BIGEQ",r'\>\='),
            ('SPACE',r' '),
            ("OTHER",r'.')
        ]
        self.REGULAR_EXPR = re.compile('|'.join(f'(?P<{n}>{p})' for n, p in TOKENS))


