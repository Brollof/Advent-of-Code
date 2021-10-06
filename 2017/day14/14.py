import sys
sys.path.append("..")

import struct
from knot import *


with open("input.txt") as file:
    data = file.read()


disk = []

used = 0
for i in range(128):
    knot = knot_hash(f"{data}-{i}")
    row = bin(int(knot, 16))[2:].zfill(128)
    disk.append(list(row.replace("1", "#").replace("0", ".")))
    used += row.count("1")

print(f"Part 1: {used}")
assert 8204 == used


def flood(disk, x, y, num):
    if x >= 0 and x < len(disk) and y >= 0 and y < len(disk):
        if disk[y][x] == '#':
            disk[y][x] = num
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                flood(disk, x + dx, y + dy, num)


region_num = 0
for y in range(len(disk)):
    for x in range(len(disk[0])):
        if disk[y][x] == '#':
            region_num += 1
            flood(disk, x, y, region_num)


print(f"Part 2: {region_num}")
assert 1089 == region_num
