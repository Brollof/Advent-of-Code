from collections import defaultdict


with open("inp3.txt") as file:
    data = file.read()


DIRS = {'^': (0, 1), 'v': (0, -1), '>': (1, 0), '<': (-1, 0)}

x, y = 0, 0
houses = defaultdict(int, {(0, 0): 1})

for dire in data:
    dx, dy = DIRS[dire]
    x, y = x + dx, y + dy
    houses[(x, y)] = 1

p1 = len(houses)
print(f"Part 1: {p1}")
assert 2592 == p1


sx, sy = 0, 0
rx, ry = 0, 0
houses = defaultdict(int, {(0, 0): 1})

for i, dire in enumerate(data):
    dx, dy = DIRS[dire]
    if i % 2 == 0:
        sx, sy = sx + dx, sy + dy
        houses[(sx, sy)] = 1
    else:
        rx, ry = rx + dx, ry + dy
        houses[(rx, ry)] = 1

p2 = len(houses)
print(f"Part 2: {p2}")
assert 2360 == p2
