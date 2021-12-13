import numpy as np
import re


def fold(arr, axis, idx):
    if axis == 'x':
        return arr[:, :idx] + np.fliplr(arr[:, idx + 1:])
    elif axis == 'y':
        return arr[:idx] + np.flipud(arr[idx + 1:])
    else:
        assert False, f"Wrong axis! {axis}"


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
    grid = fold(grid, axis, int(value))
    if i == 0:
        p1 = np.count_nonzero(grid)


print(f"Part 1: {p1}")
assert p1 == 781

# Part 2
for row in grid:
    print(''.join('#' if v > 0 else '.' for v in row))
