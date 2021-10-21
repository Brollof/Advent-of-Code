import re
import numba

with open("inp25.txt") as file:
    data = file.read()

row, col = [int(x) for x in re.findall(r"\d+", data)]

@numba.jit
def gen(row, col):
    n = 20151125
    x, y = 1, 1

    while True:
        n = (n * 252533) % 33554393
        x, y = x + 1, y - 1

        if y == 0:
            x, y = 1, x

        if x == col and y == row:
            return n

n = gen(row, col)
print(f"Part 1: {n}")
assert 8997277 == n
