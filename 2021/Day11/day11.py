import numpy as np


def nejbs(x, y):
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            if dy == dx == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
                yield nx, ny


def flash(x, y, ex):
    global flashes
    if (x, y) in ex:
        return
    grid[y][x] += 1
    if grid[y][x] > 9:
        flashes += 1
        grid[y][x] = 0
        ex.add((x, y))
        for nx, ny in nejbs(x, y):
            flash(nx, ny, ex)


with open("inp11.txt") as file:
    data = file.read()


grid = np.array([list(map(int, list(line))) for line in data.splitlines()])
flashes = 0
STEPS = 1000

for step in range(1, STEPS + 1):
    ex = set()

    for y, x in np.ndindex(grid.shape):
        flash(x, y, ex)

    if step == 100:
        p1 = flashes

    if np.all(grid == 0):
        p2 = step
        break


print(f"Part 1: {p1}")
assert p1 == 1627

print(f"Part 2: {p2}")
assert p2 == 329
