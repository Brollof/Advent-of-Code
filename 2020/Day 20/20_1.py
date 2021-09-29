import re
import numpy as np
from copy import deepcopy as dc, copy
from math import sqrt


LEFT = (1 << 0)
RIGHT = (1 << 1)
UP = (1 << 2)
DOWN = (1 << 3)


class Tile:
    def __init__(self, raw_data=None):
        self.raw_data = raw_data
        tile_str = raw_data.splitlines()
        self.id = int(tile_str[0].split(' ')[1][:-1])
        self.grid = np.array([list(row) for row in tile_str[1:]])

    def __eq__(self, o):
        return self.id == o.id

    def __repr__(self):
        return f"{self.id}"


    def print_all(self):
        print("Original:")
        self.print_grid()

        print("\nLeft 1")
        self.rotateLeft()
        self.print_grid()

        print("\nLeft 2")
        self.rotateLeft()
        self.print_grid()

        print("\nLeft 3")
        self.rotateLeft()
        self.print_grid()

        # back to original
        self.rotateLeft()

        print('\nFlipped X')
        self.flipx()
        self.print_grid()

        print('\nFlipped X, left 1')
        self.rotateLeft()
        self.print_grid()

        print('\nFlipped X, left 2')
        self.rotateLeft()
        self.print_grid()

        print('\nFlipped X, left 3')
        self.rotateLeft()
        self.print_grid()

        # back to original
        self.rotateLeft()
        self.flipx()

        print('\nFlipped Y')
        self.flipy()
        self.print_grid()

        print('\nFlipped Y, left 1')
        self.rotateLeft()
        self.print_grid()

        print('\nFlipped Y, left 2')
        self.rotateLeft()
        self.print_grid()

        print('\nFlipped Y, left 3')
        self.rotateLeft()
        self.print_grid()

    def print_grid(self):
        print('\n'.join(''.join(row) for row in self.grid))

    def rotateLeft(self, k=1):
        self.grid = np.rot90(self.grid, k=k)

    def flipx(self):
        self.grid = np.fliplr(self.grid)

    def flipy(self):
        self.grid = np.flipud(self.grid)

    def check(self, o, d):
        if d == 'top': # check my top edge against other bottom
            return list(self.grid[0]) == list(o.grid[-1])
        if d == 'bot':
            return list(self.grid[-1]) == list(o.grid[0])
        if d == 'left':
            return [row[0] for row in self.grid] == [row[-1] for row in o.grid]
        if d == 'right':
            return [row[-1] for row in self.grid] == [row[0] for row in o.grid]


tiles = []

with open('input.txt') as file:
    data = file.read()


for tile_str in data.split('\n\n'):
    tiles.append(Tile(tile_str))

N = int(sqrt(len(tiles)))

all_tiles = []
# generate all possibilities
for tile in tiles:
    # ORIGINAL
    t = dc(tile)
    all_tiles.append(t)

    # ROTATE 1
    t = dc(tile)
    t.rotateLeft()
    all_tiles.append(t)

    # ROTATE 2
    t = dc(tile)
    t.rotateLeft()
    t.rotateLeft()
    all_tiles.append(t)

    # ROTATE 3
    t = dc(tile)
    t.rotateLeft()
    t.rotateLeft()
    t.rotateLeft()
    all_tiles.append(t)

    # FLIP X
    t = dc(tile)
    t.flipx()
    all_tiles.append(t)

    # FLIP X, ROTATE 1
    t = dc(tile)
    t.flipx()
    t.rotateLeft()
    all_tiles.append(t)

    # FLIP X, ROTATE 2
    t = dc(tile)
    t.flipx()
    t.rotateLeft()
    t.rotateLeft()
    all_tiles.append(t)

    # FLIP X, ROTATE 3
    t = dc(tile)
    t.flipx()
    t.rotateLeft()
    t.rotateLeft()
    t.rotateLeft()
    all_tiles.append(t)

def can_use(tile, grid):
    for row in grid:
        for el in row:
            if el and tile == el:
                return False
    return True

def find(x, y, grid):
    new = []
    for tile in all_tiles:
        if not can_use(tile, grid):
            continue
        if x - 1 >= 0 and grid[y][x - 1] is not None:
            if not tile.check(grid[y][x - 1], 'left'):
                continue
        if x + 1 < N and grid[y][x + 1] is not None:
            if not tile.check(grid[y][x + 1], 'right'):
                continue
        if y - 1 >= 0 and grid[y - 1][x] is not None:
            if not tile.check(grid[y - 1][x], 'top'):
                continue
        if y + 1 < N and grid[y + 1][x] is not None:
            if not tile.check(grid[y + 1][x], 'bot'):
                continue
        new.append(tile)
    return new


def is_full(grid):
    for row in grid:
        for el in row:
            if el is None:
                return False
    return True


def find_nejbs(x, y, start=None, grid=None):
    if not grid:
        grid = [[None] * N for _ in range(N)]

    if is_full(grid):
        return grid

    if start:
        grid[y][x] = start
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    to_find = []
    for i in range(len(dx)):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and grid[ny][nx] is None:
            to_find.append((nx, ny))

    for nx, ny in to_find:
        fits = find(nx, ny, grid)
        # assert len(fits) == 1, f"{fits}"
        if fits:
            grid[ny][nx] = fits[0]
            return find_nejbs(nx, ny, grid=grid)


for i in range(len(all_tiles)):
    print(i)
    g = find_nejbs(0, 0, start=all_tiles[i])
    if g:
        # print(g)
        part1 = g[0][0].id * g[0][N-1].id * g[N-1][0].id * g[N-1][N-1].id
        print(part1)
        # break
