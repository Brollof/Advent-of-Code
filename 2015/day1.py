with open("inp1.txt") as file:
    data = file.read()


floor = data.count("(") - data.count(")")

print(f"Part 1: {floor}")
assert 232 == floor


floor = 0
for i, c in enumerate(data, 1):
    floor += 1 if c == '(' else -1
    if floor < 0:
        break

print(f"Part 2: {i}")
assert 1783 == i
