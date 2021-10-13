import re
from collections import defaultdict
from itertools import permutations


def calc_happiness(hap_change):
    best_hap = 0
    for p in permutations(hap_change.keys()):
        hap = 0
        for i in range(len(p) - 1):
            hap += hap_change[p[i]][p[i + 1]]
            hap += hap_change[p[i + 1]][p[i]]
        hap += hap_change[p[0]][p[-1]]
        hap += hap_change[p[-1]][p[0]]
        best_hap = max(best_hap, hap)
    return best_hap


with open("inp13.txt") as file:
    data = file.read()


hap_change = defaultdict(dict)

for p1, change, val, p2 in re.findall(r"(\w+) would (\w+) (\d+) .* (\w+).", data):
    hap_change[p1][p2] = int(val) if change == "gain" else -int(val)

p1 = calc_happiness(hap_change)
print(f"Part 1: {p1}")
assert 733 == p1


# add yourself
for person in list(hap_change.keys()):
    hap_change[person]["me"] = 0
    hap_change["me"][person] = 0

p2 = calc_happiness(hap_change)
print(f"Part 2: {p2}")
assert 725 == p2
