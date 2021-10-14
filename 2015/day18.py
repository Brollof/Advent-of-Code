from copy import deepcopy


def lights_on(grid):
    return sum(sum(row) for row in grid)


def count_nejb(x, y):
    on_cnt = 0
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            if i == j == 0:
                continue
            nx, ny = x + j, y + i
            if 0 <= nx < 100 and 0 <= ny < 100:
                if grid[ny][nx] == 1:
                    on_cnt += 1
    return on_cnt


STEPS = 100

with open("inp18.txt") as file:
    data = file.read()

original_grid = []
for line in data.splitlines():
    row = [1 if c == '#' else 0 for c in line]
    original_grid.append(row)


grid = deepcopy(original_grid)

for _ in range(STEPS):
    g = deepcopy(grid)
    for y in range(100):
        for x in range(100):
            nejb_on = count_nejb(x, y)
            if grid[y][x] == 1 and nejb_on not in (2, 3):
                    g[y][x] = 0
            elif nejb_on == 3:
                    g[y][x] = 1
    grid = deepcopy(g)

p1 = lights_on(grid)
print(f"Part 1: {p1}")
assert 768 == p1



grid = deepcopy(original_grid)

for _ in range(STEPS):
    g = deepcopy(grid)

    for y in range(100):
        for x in range(100):
            nejb_on = count_nejb(x, y)
            if grid[y][x] == 1 and nejb_on not in (2, 3) and (x, y) not in ((0, 0), (0, 99), (99, 0), (99, 99)):
                    g[y][x] = 0
            elif nejb_on == 3:
                    g[y][x] = 1

    grid = deepcopy(g)

p2 = lights_on(grid)
print(f"Part 2: {p2}")
assert 781 == p2
