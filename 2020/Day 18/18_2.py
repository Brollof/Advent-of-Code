import re
from helper import compute


with open('input.txt') as file:
    data = file.read()


def eval_simple(s):
    return str(compute(s))


def replace(s):
    v = 0
    op = None
    return eval_simple(s[0][1:-1])


def eval_expression(exp):
    while '(' in exp:
        exp = re.sub(r'\([ 0-9+*]+\)', replace, exp, count=1)
    return int(eval_simple(exp))


s = sum(eval_expression(line) for line in data.splitlines())
print(s)

assert s == 461295257566346