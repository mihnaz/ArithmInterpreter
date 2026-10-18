from interpreter.lexer import Lexer, Token
from interpreter.parser import Parser


def lexical(text):
    lexer = Lexer(text)
    tokenized = []
    for i in lexer.tokenize():
        tokenized.append(i)
    tokenized.append(Token("EOF",'Конец файла'))
    return tokenized


def syntax(tokens):
    parser = Parser(tokens)
    tree = parser.parse()
    return tree

def evaluate(text):
    tokenized = lexical(text)
    tree = syntax(tokenized)
    return tree.interpret()



if __name__ == '__main__':
    input_text = input()
    try:
        print(evaluate(input_text))
    except SyntaxError as e:
        print(*e.args)
    except ZeroDivisionError:
        print("Невозможно делить на ноль")


