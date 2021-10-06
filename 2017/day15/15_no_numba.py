def part1(genA, genB):
    match = 0
    for _ in range(40_000_000):
        genA = genA * 16807 % 2147483647
        genB = genB * 48271 % 2147483647
        if (genA & 0xffff) == (genB & 0xffff):
            match += 1
    return match


def part2(genA, genB):
    match = 0
    for _ in range(5_000_000):
        while True:
            genA = genA * 16807 % 2147483647
            if genA % 4 == 0: break
        while True:
            genB = genB * 48271 % 2147483647
            if genB % 8 == 0: break
        if (genA & 0xffff) == (genB & 0xffff):
            match += 1
    return match


with open("input.txt") as file:
    genA, genB = [int(line.strip().split(' ')[-1]) for line in file.readlines()]


p1 = part1(genA, genB)
print(f"Part 1: {p1}")
assert 631 == p1


p2 = part2(genA, genB)
print(f"Part 2: {p2}")
assert 279 == p2
