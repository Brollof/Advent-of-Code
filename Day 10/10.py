from itertools import cycle
from collections import namedtuple
from math import sqrt, gcd, atan2


Pt = namedtuple("Pt", "x, y")


def dist(a, b):
    return sqrt((a.x - b.x)**2 + (a.y - b.y)**2)


def get_space_map(best):
    space_map = {}
    for obj in asteroids:
        if obj != best:
            x, y = obj.x - best.x, obj.y - best.y
            div = gcd(x, y)
            vector = Pt(x // div, y // div)
            if vector in space_map:
                space_map[vector].append(Pt(x, y))
            else:
                space_map[vector] = [Pt(x, y)]
    return space_map


def get_vaporized(n):
    cnt = 0
    for angle in space_map:
        objs = space_map[angle]
        space_map[angle] = list(sorted(objs, key=lambda v: dist(station, v)))

    angles = space_map.keys()
    angles = list(sorted(angles, key=lambda v: atan2(-v.x, v.y)))
    angles.insert(0, angles.pop(-1))

    for angle in cycle(angles):
        if not space_map[angle]:
            continue
        if cnt == n - 1:
            return space_map[angle][0]
        cnt += 1
    return None


with open("input.txt") as file:
    inp = file.read().split()

asteroids = [Pt(i, j) for j in range(len(inp)) for i in range(len(inp[j])) if inp[j][i] == "#"]

max_visible, space_map, station = 0, None, None
for obj in asteroids:
    total = get_space_map(obj)
    visible = len(total)
    if max_visible < visible:
        max_visible = visible
        space_map = total
        station = obj

# part 1
print(max_visible)

# part 2
obj = get_vaporized(200)
print((obj.x + station.x) * 100 + obj.y + station.y)

