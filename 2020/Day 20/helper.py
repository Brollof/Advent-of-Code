from copy import deepcopy as dc, copy

# generate all possibilities
def generate(tile):
    new_tiles = []

    # ORIGINAL
    t = dc(tile)
    new_tiles.append(t)

    # ROTATE 1
    t = dc(tile)
    t.rotateLeft()
    new_tiles.append(t)

    # ROTATE 2
    t = dc(tile)
    t.rotateLeft()
    t.rotateLeft()
    new_tiles.append(t)

    # ROTATE 3
    t = dc(tile)
    t.rotateLeft()
    t.rotateLeft()
    t.rotateLeft()
    new_tiles.append(t)

    # FLIP X
    t = dc(tile)
    t.flipx()
    new_tiles.append(t)

    # FLIP X, ROTATE 1
    t = dc(tile)
    t.flipx()
    t.rotateLeft()
    new_tiles.append(t)

    # FLIP X, ROTATE 2
    t = dc(tile)
    t.flipx()
    t.rotateLeft()
    t.rotateLeft()
    new_tiles.append(t)

    # FLIP X, ROTATE 3
    t = dc(tile)
    t.flipx()
    t.rotateLeft()
    t.rotateLeft()
    t.rotateLeft()
    new_tiles.append(t)

    return new_tiles


def squash_to_str(tiles):
    s = ''
    for row_tiles in tiles:
        for i in range(1, len(row_tiles[0].grid[0]) - 1):
            for tile in row_tiles:
                s += ''.join(tile.grid[i])[1:-1]
            s += '\n'
    return s.strip()