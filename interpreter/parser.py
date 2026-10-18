from interpreter.expressions import *


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current(self):
        return self.tokens[self.pos]

    def take(self):
        tok = self.tokens[self.pos]
        self.pos += 1
        return tok

    def take_if(self, *types):
        if self.current().type in types:
            return self.take()
        return None

    def require(self, type_required):
        tok = self.current()
        if tok.type != type_required:
            raise SyntaxError(
                f"Ожидался {type_required}, получен {tok.type} ({tok.value!r})"
            )
        return self.take()

    def parse_expression(self):
        node = self.parse_multiplication()
        while (op_tok := self.take_if('SUM', 'MINUS', 'BIGEQ')) is not None:
            right = self.parse_multiplication()
            if op_tok.type == "SUM":
                node = SumExpression(node, right)
            elif op_tok.type == "MINUS":
                node = SubExpression(node, right)
            elif op_tok.type == "BIGEQ":
                node = BigEqExpression(node, right)
        return node

    def parse_multiplication(self):
        node = self.parse_unary()
        while (op_tok := self.take_if('MUL', 'DIV')) is not None:
            right = self.parse_unary()
            if op_tok.type == "MUL":
                node = MulExpression(node, right)
            elif op_tok.type == "DIV":
                node = DivExpression(node, right)
        return node

    def parse_unary(self):
        if self.take_if('MINUS') is not None:
            return MulExpression(NumberExpression(-1), self.parse_unary())
        return self.parse_atom()

    def parse_atom(self):
        tok = self.current()

        if tok.type == 'NUMBER':
            self.take()
            value = float(tok.value) if '.' in tok.value else int(tok.value)
            return NumberExpression(value)

        if tok.type == 'BRACKET_START':
            self.take()
            node = self.parse_expression()
            self.require('BRACKET_END')
            return node
        if tok.type == 'SIN':
            self.take()
            node = self.parse_expression()
            self.require('BRACKET_END')
            return SinExpression(node)
        raise SyntaxError(f"Неожиданный токен {tok.type} ({tok.value})")

    def parse(self):
        tree = self.parse_expression()
        self.require('EOF')
        return tree
