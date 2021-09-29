from copy import deepcopy as dp
from time import time


with open('input.txt') as file:
    data = file.read()

# data = """.#.
# ..#
# ###"""

data = data.splitlines()

active = []

# parse input
for y in range(len(data)):
    for x in range(len(data[0])):
        v = data[y][x]
        if v == '#':
            active.append((x, y, 0, 0))


def nejbs(xyzw):
    cx, cy, cz, cw = xyzw
    for x in (-1, 0, 1):
        for y in (-1, 0, 1):
            for z in (-1, 0, 1):
                for w in (-1, 0, 1):
                    if x == y == z == w == 0:
                        continue
                    yield (cx + x, cy + y, cz + z, cw + w)


def count_active_nejb(xyzw):
    return sum(nejb in active for nejb in nejbs(xyzw))


cyc = 0
def cycle():
    global active
    global cyc

    cyc += 1
    start = time()
    print(f'cycle {cyc} started...')

    temp_active = dp(active)

    seen = set()

    # check active only (1 -> 0)
    for xyz in active:
        cnt = count_active_nejb(xyz)
        if cnt not in (2, 3): # cubes becomes inactive
            temp_active.remove(xyz)

            # check inactive neighbours of active ones (0 -> 1)
            for nejb in nejbs(xyz):
                if nejb not in seen:
                    seen.add(nejb)
                    cnt = count_active_nejb(nejb)
                    if cnt == 3 and nejb not in active:
                        temp_active.append(nejb)

    active = dp(temp_active)
    print(f'end ({time() - start}).')


for _ in range(6):
    cycle()

# part 2
print(len(active))