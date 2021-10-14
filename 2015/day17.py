import re
from itertools import combinations
from collections import defaultdict

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


################################################################
# Part 1 only
################################################################

from functools import cache

@cache
def go(n, target):
    if target == 0:
        return 1

    if n < 0 or target < 0:
        return 0

    return go(n - 1, target) + go(n - 1, target - cont[n])

print(go(len(cont) - 1, 150))
