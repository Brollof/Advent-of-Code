import re


with open('input.txt') as file:
    data = file.read()


def eval_simple(s):
    v = 0
    op = None
    for c in s.split(' '):
        if c.isdigit():
            if op:
                if op == '+':
                    v += int(c)
                elif op == '*':
                    v *= int(c)
            else:
                v = int(c)
        elif c in '*+':
            op = c
    return str(v)


def replace(s):
    v = 0
    op = None
    # print(s)
    return eval_simple(s[0][1:-1])


def eval_expression(exp):
    while '(' in exp:
        exp = re.sub(r'\([ 0-9+*]+\)', replace, exp, count=1)
    return int(eval_simple(exp))


s = sum(eval_expression(line) for line in data.splitlines())
print(s)

assert 15285807527593 == s

