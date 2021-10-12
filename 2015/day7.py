import operator as op
from functools import cache


with open("inp7.txt") as file:
    data = file.read()


ops = {
    'NOT': op.inv,
    'AND': op.and_,
    'OR': op.or_,
    'LSHIFT': op.lshift,
    'RSHIFT': op.rshift
}

class Expr:
    def __init__(self, op, v):
        self.op = op
        self.v = v
        assert type(self.v) == list

    def __repr__(self):
        return f"({self.op}; {self.v})"


wiring = {}

for line in data.splitlines():
    expr, sig = line.split(" -> ")
    vss = expr.split(" ")
    if len(vss) == 3: # some expression
        wiring[sig] = Expr(ops[vss[1]], [vss[0], vss[2]])
    elif len(vss) == 2: # operator NOT
        wiring[sig] = Expr(ops[vss[0]], [vss[1]])
    elif len(vss) == 1: # signal assigning
        wiring[sig] = Expr(None, [vss[0]])
    else:
        raise Exception(f"vss: {vss}")


@cache
def go(wire):
    expr = wiring[wire]
    if expr.op == ops['NOT']:
        v = int(expr.v[0]) if expr.v[0].isnumeric() else go(expr.v[0])
        return expr.op(v)
    elif expr.op:
        v1 = int(expr.v[0]) if expr.v[0].isnumeric() else go(expr.v[0])
        v2 = int(expr.v[1]) if expr.v[1].isnumeric() else go(expr.v[1])
        return expr.op(v1, v2)
    return int(expr.v[0]) if expr.v[0].isnumeric() else go(expr.v[0])


p1 = go('a')
print(f"Part 1: {p1}")
assert 46065 == p1


go.cache_clear()
wiring['b'].v[0] = str(p1)

p2 = go('a')
print(f"Part 2: {p2}")
assert 14134 == p2
