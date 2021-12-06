from collections import deque


def shift(days):
    for day in range(days):
        cycles.rotate(-1)
        cycles[6] += cycles[-1]
        cycles[8] = cycles[-1]


with open("inp6.txt") as file:
    fishes = [int(n) for n in file.read().split(",")]

cycles = deque(fishes.count(i) for i in range(9))

shift(80)
p1 = sum(cycles)
print(f"Part 1: {p1}")
assert 380243 == p1

shift(256 - 80)
p2 = sum(cycles)
print(f"Part 2: {p2}")
assert 1708791884591 == p2
