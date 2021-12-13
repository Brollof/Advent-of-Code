import numpy as np
import re


def fold_y(arr, y):
    return arr[:y] + arr[y + 1:][::-1]


def fold_x(arr, x):
    return arr[:, :x] + np.fliplr(arr[:, x + 1:])


with open("inp13.txt") as file:
    data = file.read()


points_raw, folds_raw = data.split("\n\n")
points = []

for line in points_raw.splitlines():
    x, y = line.split(",")
    points.append((int(x), int(y)))


folds = re.findall(r"([xy])=(\d+)", folds_raw)

ax1, v1 = folds[0]
ax2, v2 = folds[1]
if ax1 == 'x':
    max_x = int(v1) * 2 + 1
    max_y = int(v2) * 2 + 1
elif ax2 == 'x':
    max_x = int(v2) * 2 + 1
    max_y = int(v1) * 2 + 1

grid = np.zeros((max_y, max_x), dtype=int)

for x, y in points:
    grid[y][x] = 1


for i, (axis, value) in enumerate(folds):
    if axis == 'x':
        grid = fold_x(grid, int(value))
    elif axis == 'y':
        grid = fold_y(grid, int(value))
    else:
        assert False, f"Wrong axis! {axis}"
    if i == 0:
        p1 = np.count_nonzero(grid)


print(f"Part 1: {p1}")
assert p1 == 781

# Part 2
for row in grid:
    print(''.join('#' if v > 0 else '.' for v in row))
