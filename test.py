from math import sin

from main import evaluate

assert evaluate("1+2*3") == 1+2*3
assert evaluate("(1+2)*3") == (1+2)*3
assert evaluate("1-2-3") == 1-2-3
assert evaluate("((8/4))") == ((8/4))
assert evaluate("-(1+2)*3") == -(1+2)*3
assert evaluate("sin(0.5)")==sin(0.5)
assert evaluate("5+sin(1)")==5+sin(1)
assert evaluate("(5>=1)*5")==(5>=1)*5
