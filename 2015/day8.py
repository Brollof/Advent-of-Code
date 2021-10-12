import ast
import json


with open("inp8.txt") as file:
    data = file.read()


total, escaped, reduced = 0, 0, 0
for s in data.splitlines():
    total += len(s)
    reduced += len(ast.literal_eval(s))
    escaped += len(json.dumps(s))


p1 = total - reduced
print(f"Part 1: {p1}")
assert 1333 == p1


p2 = escaped - total
print(f"Part 2: {p2}")
assert 2046 == p2
