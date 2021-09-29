from collections import defaultdict
from copy import copy
import re
from time import time


WHITE, BLACK = 1, 0

with open('input.txt') as file:
    data = file.read()


tiles_instructions = []

for line in data.splitlines():
    line = line.replace('se', 'se,')
    line = line.replace('sw', 'sw,')
    line = line.replace('nw', 'nw,')
    line = line.replace('ne', 'ne,')
    line = re.sub(r'[ew]\w', lambda m: f"{m[0][0]},{m[0][1]}", line)
    line = re.sub(r'[ew]\w', lambda m: f"{m[0][0]},{m[0][1]}", line)
    line = line.rstrip(',')
    tiles_instructions.append(line.split(','))

# print(tiles_instructions)

def convert_dir(d):
    if d == 'ne': return (+1,  0, -1)
    if d == 'e':  return (+1, -1,  0)
    if d == 'se': return ( 0, -1, +1)
    if d == 'sw': return (-1,  0, +1)
    if d == 'w':  return (-1, +1,  0)
    if d == 'nw': return ( 0, +1, -1)
    print(f"wtf? '{d}'")
    assert False


floor = defaultdict(lambda: WHITE)

# generate floor
for tile in tiles_instructions:
    cur = (0, 0, 0)
    for d in tile: 
        x, y, z = cur
        xo, yo, zo = convert_dir(d)
        cur = x + xo, y + yo, z + zo
    floor[cur] ^= 1 # flip tile


def count_black():
    return list(floor.values()).count(BLACK)


def nejbs(coord):
    x, y, z = coord
    for xo, yo, zo in ((1,0,-1), (1,-1,0), (0,-1,1), (-1,0,1), (-1,1,0), (0,1,-1)):
        yield x + xo, y + yo, z + zo


def count_black_nejbs(coord):
    cnt = 0
    for nejb in nejbs(coord):
        if nejb in floor and floor[nejb] == BLACK:
            cnt += 1
    return cnt


def switch():
    global floor
    seen = set()
    new_floor = copy(floor)

    for tile, color in floor.items():
        seen.add(tile)
        blacks = count_black_nejbs(tile)
        if color == BLACK and (blacks == 0 or blacks > 2):
            new_floor[tile] = WHITE
        elif color == WHITE and blacks == 2:
            new_floor[tile] = BLACK
    
        for nejb in nejbs(tile):
            if nejb in seen:
                continue
            
            seen.add(nejb)
            blacks = count_black_nejbs(nejb)
            if blacks == 1:
                continue
            if new_floor[nejb] == BLACK and (blacks == 0 or blacks > 2):
                new_floor[nejb] = WHITE
            elif new_floor[nejb] == WHITE and blacks == 2:
                new_floor[nejb] = BLACK
            elif blacks == 0 and new_floor[nejb] == WHITE:
                del new_floor[nejb]

    floor = copy(new_floor)
        
start = time()
for i in range(100):
    switch()

print(f"Black tiles: {count_black()}")
print(f"Done in {time() - start:.1f} s")