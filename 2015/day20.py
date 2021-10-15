import numba


with open("inp20.txt") as file:
    data = file.read()


target = int(data)


@numba.jit
def calc_house1(n):
    s = 0
    for x in range(1, int(n**0.5)+1):
        if n % x == 0:
            if x != x/n:
                s = s + x + n//x
            else:
                s = s + x
    return s * 10


@numba.jit
def calc_house2(n):
    s = 0
    for x in range(1, n + 1):
        if n % x == 0 and n <= 50 * x:
            s += x
    return s * 11


@numba.jit
def part1(start):
    n = 0
    while True:
        n += 10
        if calc_house1(n) >= target:
            return n


@numba.jit
def part2(start):
    n = start
    while True:
        n += 10
        if calc_house2(n) >= target:
            return n


p1 = part1(0)
print(f"Part 1: {p1}")
assert 831600 == p1

p2 = part2(p1)
print(f"Part 2: {p2}")
assert 884520 == p2
