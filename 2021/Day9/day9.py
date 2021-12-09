from operator import mul
from functools import reduce


def calc_basin(grid, x, y):
    if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid) or grid[y][x] == 9:
        return 0

    s = 1
    grid[y][x] = 9
    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        s += calc_basin(grid, x + dx, y + dy)
    return s


with open("inp9.txt") as file:
    grid = [list(map(int, list(line))) for line in file.read().splitlines()]


risk_level = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if all(grid[y][x] < grid[y + dy][x + dx] for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0))
               if 0 <= x + dx < len(grid[0]) and 0 <= y + dy < len(grid)):
            risk_level += int(grid[y][x]) + 1

print(f"Part 1: {risk_level}")
assert risk_level == 518


basins = [calc_basin(grid, x, y) for y in range(len(grid)) for x in range(len(grid[0]))]
result = reduce(mul, sorted(basins, reverse=True)[:3])
print(f"Part 2: {result}")
assert result == 949905
