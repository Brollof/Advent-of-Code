import re
import numpy as np
from copy import deepcopy as dc, copy


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

from math import sqrt
N = int(sqrt(len(tiles)))
# LEFT = (1 << 0)
# RIGHT = (1 << 1)
# UP = (1 << 2)
# DOWN = (1 << 3)

# IDX = {0: RIGHT | DOWN, 11: LEFT | DOWN, 32: UP | RIGHT, 43: LEFT | UP}
# IDX |= {i: LEFT | RIGHT for i in range(1, 11)}
# IDX |= {i: LEFT | RIGHT for i in range(33, 43)}
# IDX |= {i: UP | DOWN for i in range(12, 33, 2)}
# IDX |= {i: UP | DOWN for i in range(13, 32, 2)}

# for i in range(N * 4 - 4):
#     if i < N - 1:
#         print(f"{i} checking right")
#     elif N - 1 <= i < N * 2 - 2:
#         print(f"{i} checking down")
#     elif N * 2 - 2 <= i < N * 3 - 3:
#         print(f"{i} checking left")
#     else:
#         print(f"{i} checking up")


def check(t1, t2, i):
    if i < N - 1:
        return t1.check(t2, 'right')
    elif N - 1 <= i < N * 2 - 2:
        return t1.check(t2, 'bot')
    elif N * 2 - 2 <= i < N * 3 - 3:
        return t1.check(t2, 'left')
    else:
        return t1.check(t2, 'top')


all_tiles = []
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






# T = {tile.id: tile for tile in tiles}
# r = T[1951].check(T[2729], 'bot')
# print(r)
# tiles[1].rotateLeft()
# tiles[1].rotateLeft()
# tiles[1].flipx()
# tiles[1].print_grid()
# print()
# print()

# tiles[0].rotateLeft()
# tiles[0].rotateLeft()
# tiles[0].flipx()
# tiles[0].print_grid()

def traverse(start=None, ci=0, path=[]):
    if start:
        path.append(start)
    # print(ci, path)
    if len(path) == N * 4 - 4:
        return path
    for tile in all_tiles:
        if tile not in path and check(path[-1], tile, ci):
            # print('-----------------------')
            # print(tile.print_grid())
            # print('-----------------------')
            path.append(tile)
            return traverse(ci=(ci+1), path=path)

for i in range(len(all_tiles)):
    # print(i)
    p = traverse(start=all_tiles[i], ci=0, path=[])
    if p:
        print(f"FINAL ANSWER (i={i}):")
        print(p)
