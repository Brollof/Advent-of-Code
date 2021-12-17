import re
from itertools import product


def fire_probe(init_velocity, target_area):
    x, y = 0, 0
    vx, vy = init_velocity
    tx1, tx2, ty1, ty2 = target_area
    path = [(x, y)]
    max_height = 0

    while True:
        x, y = x + vx, y + vy
        if x > tx2 or y < ty1:
            break

        max_height = max(max_height, y)
        path.append((x, y))

        vy -= 1
        if vx > 0:
            vx -= 1
        elif vx < 0:
            vx += 1

        if tx1 <= x <= tx2 and ty1 <= y <= ty2:
            return max_height, path

    return None, path


def print_path(path, target):
    tx1, tx2, ty1, ty2 = target
    y_off = max(x[1] for x in path)
    grid = [['.'] * (tx2 + 1) for _ in range(abs(ty1) + abs(y_off) + 1)]

    for y in range(ty1, ty2 + 1):
        for x in range(tx1, tx2 + 1):
            grid[abs(y - y_off)][x] = 'T'

    for x, y in path:
        grid[abs(y - y_off)][x] = '#'

    for row in grid:
        print(''.join(row))


with open("inp17.txt") as file:
    data = file.read()

r = re.search(r"x=(\d+)..(\d+), y=(-\d+)..(-\d+)", data)
target = [int(x) for x in r.groups()]
tx1, tx2, ty1, ty2 = target
max_x = tx2
max_y = max(abs(ty1), abs(ty2))
heights = []

for vx, vy in product(range(max_x + 1), range(-max_y, max_y + 1)):
    height, _ = fire_probe((vx, vy), target)
    if height is not None:
        heights.append(height)


p1 = max(heights)
print(f"Part 1: {p1}")
assert p1 == 7875

p2 = len(heights)
print(f"Part 2: {p2}")
assert p2 == 2321
