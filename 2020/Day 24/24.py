from collections import defaultdict
import re


with open('input.txt') as file:
    data = file.read()


# data = """sesenwnenenewseeswwswswwnenewsewsw
# neeenesenwnwwswnenewnwwsewnenwseswesw
# seswneswswsenwwnwse
# nwnwneseeswswnenewneswwnewseswneseene
# swweswneswnenwsewnwneneseenw
# eesenwseswswnenwswnwnwsewwnwsene
# sewnenenenesenwsewnenwwwse
# wenwwweseeeweswwwnwwe
# wsweesenenewnwwnwsenewsenwwsesesenwne
# neeswseenwwswnwswswnw
# nenwswwsewswnenenewsenwsenwnesesenew
# enewnwewneswsewnwswenweswnenwsenwsw
# sweneswneswneneenwnewenewwneswswnese
# swwesenesewenwneswnwwneseswwne
# enesenwswwswneneswsenwnewswseenwsese
# wnwnesenesenenwwnenwsewesewsesesew
# nenewswnwewswnenesenwnesewesw
# eneswnwswnwsenenwnwnwwseeswneewsenese
# neswnwewnwnwseenwseesewsenwsweewe
# wseweeenwnesenwwwswnew"""

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


flipped = defaultdict(lambda: 1) # 1 means white, 0 black :-)

for tile in tiles_instructions:
    cur = (0, 0, 0)
    for d in tile: 
        x, y, z = cur
        xo, yo, zo = convert_dir(d)
        cur = x + xo, y + yo, z + zo
    flipped[cur] ^= 1 # flip tile

print(list(flipped.values()).count(0))