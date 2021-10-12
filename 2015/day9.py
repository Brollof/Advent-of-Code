
import re
from itertools import permutations
from collections import defaultdict
import math


with open("inp9.txt") as file:
    data = file.read()


dists = defaultdict(dict)
for line in data.splitlines():
    c1, c2, dist = re.findall(r"(\w+) to (\w+) = (\d+)", line)[0]
    dists[c1][c2] = int(dist)
    dists[c2][c1] = int(dist)


shortest = math.inf
longest = 0
cnt = 0
for path in permutations(dists.keys()):
    cnt += 1
    dist = sum(dists[path[i]][path[i+1]] for i in range(len(path) - 1))
    shortest = min(shortest, dist)
    longest = max(longest, dist)


print(f"Part 1: {shortest}")
assert 207 == shortest

print(f"Part 2: {longest}")
assert 804 == longest
