import re
from itertools import combinations


with open("inp17.txt") as file:
    data = file.read()


cont = [int(x) for x in re.findall(r"\d+", data)]


total = 0
for i in range(1, len(cont)+1):
    for x in combinations(cont, i):
        if sum(x) == 150:
            total += 1

print(f"Part 1: {total}")
assert 1304 == total


total = 0
for i in range(1, len(cont)+1):
    total += len([x for x in combinations(cont, i) if sum(x) == 150])
    if total:
        break

print(f"Part 2: {total}")
assert 18 == total
