from itertools import groupby


def lookandsay(n):
    return ''.join(str(len(list(g))) + k for k, g in groupby(n))


with open("inp10.txt") as file:
    n = file.read()


for i in range(50):
    n = lookandsay(n)
    if i == 39:
        p1 = len(n)


print(f"Part 1: {p1}")
assert 360154 == p1

p2 = len(n)
print(f"Part 2: {p2}")
assert 5103798 == p2
