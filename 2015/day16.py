import re


ticker_tape = """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1"""

test = {}

for line in ticker_tape.splitlines():
    it, v = line.split(": ")
    test[it] = int(v)


with open("inp16.txt") as file:
    data = file.read()


sues = {}
for line in data.splitlines():
    sue, it1, v1, it2, v2, it3, v3 = re.findall(r"Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)", line)[0]
    sues[int(sue)] = {it1: int(v1), it2: int(v2), it3: int(v3)}


sues2 = sues.copy()

for target_item, target_value in test.items():
    to_rem = set()
    for sue, items in sues.items():
        if target_item in items and items[target_item] != target_value:
            to_rem.add(sue)
    for i in to_rem:
        del sues[i]


p1 = next(iter(sues))
print(f"Part 1: {p1}")
assert 103 == p1


for target_item, target_value in test.items():
    to_rem = set()
    for sue, items in sues2.items():
        if target_item in items:
            if target_item in ('cats', 'trees') and items[target_item] > target_value:
                continue
            elif target_item in ('pomeranians', 'goldfish') and items[target_item] < target_value:
                continue
            if items[target_item] != target_value:
                to_rem.add(sue)
    for i in to_rem:
        del sues2[i]

del sues2[p1]


p2 = next(iter(sues2))
print(f"Part 2: {p2}")
assert 405 == p2
