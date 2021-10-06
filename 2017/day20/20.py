import re
import math

with open("input.txt") as file:
    data = file.read()


particles = []

for i, line in enumerate(data.splitlines()):
    r = re.findall(r"p=<(-?\d+),(-?\d+),(-?\d+)>, v=<(-?\d+),(-?\d+),(-?\d+)>, a=<(-?\d+),(-?\d+),(-?\d+)>",line)[0]
    r = list(map(int, r))
    particles += [{'p': r[:3], 'v': r[3:6], 'a': r[6:]}]


# min steps: 324
STEPS = 500

for step in range(STEPS):
    for p in particles:
        for i in range(3):
            p['v'][i] += p['a'][i]
            p['p'][i] += p['v'][i]


min_dist = math.inf
idx = -1

for i, p in enumerate(particles):
    dist = sum(map(abs, p['p']))
    if dist < min_dist:
        min_dist = dist
        idx = i

print(f"Part 1: {idx}")
assert idx == 457