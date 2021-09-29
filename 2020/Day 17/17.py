from copy import deepcopy as dp
from pprint import pprint

with open('input.txt') as file:
    data = file.read()

# data = """.#.
# ..#
# ###"""

data = data.splitlines()

active = []

# parse input, z = 0
for y in range(len(data)):
    for x in range(len(data[0])):
        v = data[y][x]
        if v == '#':
            active.append((x, y, 0))


def get_max():
    max_x = max(x for x, y, z in active)
    max_y = max(y for x, y, z in active)
    limit = max(max_x, max_y) + 1
    return limit


def print_layer(zz):
    limit = get_max()
    grid = [["."] * limit for _ in range(limit)]

    for x, y, z in active:
        if z == zz:
            grid[y][x] = '#'

    s = '\n'.join(''.join(line) for line in grid)
    print((len(grid) + 4) * '=')
    print(s)
    print((len(grid) + 4) * '=')


def count_active_nejb(xyz):
    cnt_act = 0
    cx, cy, cz = xyz
    for x in (-1, 0, 1):
        for y in (-1, 0, 1):
            for z in (-1, 0, 1):
                if x == y == z == 0:
                    continue
                if (cx + x, cy + y, cz + z) in active:
                    cnt_act += 1
    return cnt_act


def nejbs(xyz):
    cx, cy, cz = xyz
    for x in (-1, 0, 1):
        for y in (-1, 0, 1):
            for z in (-1, 0, 1):
                if x == y == z == 0:
                    continue
                yield (cx + x, cy + y, cz + z)


def count_active_nejb(xyz):
    return sum(nejb in active for nejb in nejbs(xyz))


cyc = 0
def cycle():
    global active
    global cyc

    cyc += 1
    print(f'cycle {cyc} started...')

    temp_active = dp(active)

    # check active only (1 -> 0)
    for xyz in active:
        cnt = count_active_nejb(xyz)
        if cnt not in (2, 3): # cubes becomes inactive
            temp_active.remove(xyz)

    # check inactive neighbours of active ones (0 -> 1)
    seen = set()
    for xyz in active:
        # loop through inactive ones
        for nejb in nejbs(xyz):
            if nejb not in seen:
                seen.add(nejb)
                cnt = count_active_nejb(nejb)
                if cnt == 3 and nejb not in active:
                    temp_active.append(nejb)


    active = dp(temp_active)
    print(f'end.')


for _ in range(6):
    cycle()

# part 1
print(len(active))