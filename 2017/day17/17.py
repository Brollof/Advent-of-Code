import numba
from collections import deque


with open("input.txt") as file:
    STEP = int(file.read().strip())


def part1():
    buf = deque([0])
    for n in range(1, 2017 + 1):
        buf.rotate(-STEP)
        buf.append(n)

    return buf[0]


@numba.jit
def part2():
    idx = 0
    for v in range(1, 50_000_000 + 1):
        idx = (idx + STEP) % v + 1
        if idx == 1: # value after 0 is the answer
            out = v
    return out


p1 = part1()
print(f"Part 1: {p1}")
assert 1025 == p1


p2 = part2()
print(f"Part 1: {p2}")
assert 37803463 == p2
