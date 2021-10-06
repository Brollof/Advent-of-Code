import cmath
import math
from collections import defaultdict


CLEAN = 0
WEAKENED = 1
INFECTED = 2
FLAGGED = 3


# doesn't work anyway...
def print_grid(grid, pos=None):
    max_x = max(x for x, y in grid.keys()) + 1
    # min_x = max(x for x, y in grid.keys()) + 1
    max_y = max(y for x, y in grid.keys()) + 1

    g = [[0] * max_x for _ in range(max_y)]
    for (x, y), v in grid.items():
        g[y][x] = '#' if v else '.'

    if pos:
        cx, cy = pos
        g[cy][cx] = 'O'

    for line in g:
        print(''.join(line))


def part1(grid):
    cx, cy = len(data[0]) // 2, len(data) // 2
    infections = 0
    z = 0+1j # up
    states = {CLEAN: INFECTED, INFECTED: CLEAN}

    for step in range(10000):
        state = grid[(cx, cy)]
        if state == INFECTED:
            z = right(z)
        elif state == CLEAN:
            infections += 1
            z = left(z)

        # change state
        grid[(cx, cy)] = states[state]

        # move forward
        cx, cy = cx + int(z.real), cy + int(-z.imag)

    return infections


def part2(grid):
    cx, cy = len(data[0]) // 2, len(data) // 2
    infections = 0
    z = 0+1j # up
    states = {
            CLEAN: WEAKENED,
            WEAKENED: INFECTED,
            INFECTED: FLAGGED,
            FLAGGED: CLEAN
    }

    for step in range(10_000_000):
        state = grid[(cx, cy)]
        if state == INFECTED:
            z = right(z)
        elif state == CLEAN:
            z = left(z)
        elif state == WEAKENED:
            infections += 1
        elif state == FLAGGED:
            z = rev(z)

        # change state
        grid[(cx, cy)] = states[state]

        # move forward
        cx, cy = cx + int(z.real), cy + int(-z.imag)

    return infections


with open("input.txt") as file:
    data = file.read()

data = [list(line) for line in data.splitlines()]
grid = defaultdict(int)

left = lambda z: z * 1j
right = lambda z: z * -1j
rev = lambda z: z * 1j * 1j

# convert 2D grid into map of coordinates
for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] == '#':
            grid[(x, y)] = INFECTED
        else:
            grid[(x, y)] = CLEAN


inf = part1(grid.copy())
print(f"Part 1: {inf}")
assert 5565 == inf

inf = part2(grid)
print(f"Part 2: {inf}")
assert 2511978 == inf
