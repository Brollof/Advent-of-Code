import regex as re # pip install regex
from math import sqrt
from tile import Tile
from helper import *
from copy import deepcopy as deepcopy


tiles = []

with open('input2.txt') as file:
    data = file.read()


for tile_str in data.split('\n\n'):
    id_str, grid_str = tile_str.split(":")
    idd = int(id_str.split(' ')[1])
    grid_str = grid_str.strip()
    tiles.append(Tile(idd, grid_str))

N = int(sqrt(len(tiles)))

all_tiles = []
for tile in tiles:
    all_tiles.extend(generate(tile))


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


def run():
    for i in range(96, len(all_tiles)):
    # for i in (315, 318, 603, 606, 632, 637, 729, 732):
        g = find_nejbs(0, 0, start=all_tiles[i])
        if g:
            # print(g)
            part1 = g[0][0].id * g[0][N-1].id * g[N-1][0].id * g[N-1][N-1].id
            # assert part1 == 20899048083289
            print(f"Part 1: {part1}")
            return g

###################################################################
###################################################################
###################################################################

def find_monsters(image):
    img_lines = image.get_str().splitlines()
    img_copy = deepcopy(img_lines)
    monsters_count = 0

    for i in range(1, len(img_copy) - 1):
        line = img_copy[i]
        if m_mid := re.findall(r"#....##....##....###", line):

            for match_index in range(len(m_mid)):

                start = img_copy[i].find(m_mid[match_index])

                # check above
                if img_copy[i - 1][19 + start - 1] != '#':
                    continue

                # check below
                if m_below := re.search(r".#..#..#..#..#..#...", img_copy[i + 1][start:start + 20]):
                    # print('ok!')
                    monsters_count += 1

                    # replace above
                    temp = list(img_copy[i - 1])
                    temp[19 + start - 1] = 'O'
                    img_copy[i - 1] = ''.join(temp)

                    # replace mid
                    temp = list(img_copy[i])
                    temp[start] = 'O'
                    temp[start + 5] = 'O'
                    temp[start + 6] = 'O'
                    temp[start + 11] = 'O'
                    temp[start + 12] = 'O'
                    temp[start + 17] = 'O'
                    temp[start + 18] = 'O'
                    temp[start + 19] = 'O'
                    img_copy[i] = ''.join(temp)

                    # replace below
                    temp = list(img_copy[i + 1])
                    temp[start + m_below.start() + 1] = 'O'
                    temp[start + m_below.start() + 4] = 'O'
                    temp[start + m_below.start() + 7] = 'O'
                    temp[start + m_below.start() + 10] = 'O'
                    temp[start + m_below.start() + 13] = 'O'
                    temp[start + m_below.start() + 16] = 'O'
                    img_copy[i + 1] = ''.join(temp)

    return ('\n'.join(row for row in img_copy), monsters_count)


image_tiles = run()

image = Tile(99, squash_to_str(image_tiles))

all_images = generate(image)

for i, image in enumerate(all_images):
    img, monsters_count = find_monsters(all_images[7])
    if monsters_count:
        print(f"Monsters: {monsters_count}, safewaters: {img.count('#')}")
        # print(img)
        break