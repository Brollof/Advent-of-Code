import re
import numpy as np
from collections import Counter


class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.start = (x1, y1)
        self.end = (x2, y2)

    def __repr__(self):
        return f"({self.x1},{self.y1})->({self.x2},{self.y2})"


with open("inp5.txt") as file:
    data = file.read()


lines = []
for line in data.splitlines():
    nums = [int(n) for n in re.findall(r"\d+", line)]
    lines.append(Line(*nums))


points = []
points_diag = []
for line in lines:
    size = max(abs(line.x1 - line.x2), abs(line.y1 - line.y2)) + 1
    nums = zip(np.linspace(line.x1, line.x2, size), np.linspace(line.y1, line.y2, size))
    if line.x1 == line.x2 or line.y1 == line.y2:
        points.extend(nums)
    else:
        points_diag.extend(nums)


points_counter = Counter(points)
points_diag_counter = Counter(points_diag)

p1 = sum(1 for cnt in points_counter.values() if cnt >= 2)
p2 = sum(1 for cnt in (points_counter + points_diag_counter).values() if cnt >= 2)

print(f"Part 1: {p1}")
assert 4826 == p1

print(f"Part 2: {p2}")
assert 16793 == p2
