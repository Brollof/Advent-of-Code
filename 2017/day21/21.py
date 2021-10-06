import numpy as np
import math
import time
import numba

start = time.time()

# Grid permutations generator
def gperm(t):
    yield t
    t = np.rot90(t)
    yield t
    t = np.rot90(t)
    yield t
    t = np.rot90(t)
    yield t

    t = np.fliplr(t)
    yield t
    t = np.rot90(t)
    yield t
    t = np.rot90(t)
    yield t
    t = np.rot90(t)
    yield t


def str_to_grid(s):
    return np.array([list(row) for row in s.split("/")])

def grid_to_str(g):
    return '/'.join(''.join(row) for row in g)
    
def split(arr, size):
    p, q = arr.shape
    for i in range(0, p, size):
        for j in range(0, q, size):
            yield arr[i:i + size:1, j:j + size:1]

def merge(arrs):
    size = int(math.sqrt(arrs.shape[0]))
    rows = []
    for i in range(size):
        rows.append(np.concatenate(arrs[i*size:i * size + size], axis=1))
    return np.concatenate(rows)

def tests():
    # helper functions
    arr_eq = lambda a1, a2: np.array_equal(a1, a2)
    make_arr = lambda t: np.array(t)

    assert arr_eq(str_to_grid('##/..'), [['#', '#'], ['.', '.']])
    assert arr_eq(str_to_grid('.#./#.#/#..'), [['.', '#', '.'], ['#', '.', '#'], ['#', '.', '.']])

    assert arr_eq(grid_to_str(np.array([['#', '#'], ['.', '.']])), '##/..')
    assert arr_eq(grid_to_str(np.array([['.', '#', '.'], ['#', '.', '#'], ['#', '.', '.']])), '.#./#.#/#..')

    grid = make_arr([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    s = {str(grid) for grid in gperm(grid)}
    assert len(s) == 8, f"Permutations: {len(s)}"

    t = np.arange(16).reshape(4, 4)
    subs = list(split(t, 2))
    assert len(subs) == 4
    assert arr_eq(subs[0], [[0, 1], [4, 5]])
    assert arr_eq(subs[1], [[2, 3], [6, 7]])
    assert arr_eq(subs[2], [[8, 9], [12, 13]])
    assert arr_eq(subs[3], [[10, 11], [14, 15]])

    t = np.arange(4).reshape(2, 2)
    subs = list(split(t, 2))
    assert len(subs) == 1
    assert arr_eq(subs[0], [[0, 1], [2, 3]])
    print("All tests passed.")

tests()


#############################################################


with open(r"input.txt") as file:
    data = file.read()

# data = """../.# => ##./#../...
# .#./..#/### => #..#/..../..../#..#"""

grid = str_to_grid(".#./..#/###")
rules2 = {}
rules3 = {}

for line in data.splitlines():
    l, r = line.split(" => ")
    cnt = l.count("/")
    if cnt == 1:
        for g in gperm(str_to_grid(l)):
            ll = grid_to_str(g)
            rules2[ll] = r
    elif cnt == 2:
        for g in gperm(str_to_grid(l)):
            ll = grid_to_str(g)
            rules3[ll] = r
    else:
        raise Exception(f"ODBYT")


STEPS = 18

for step in range(STEPS):
    print(step)
    new_grid = []

    if step == 5:
        part1 = np.count_nonzero(grid == '#')

    l = len(grid)
    if l % 2 == 0:
        size = 2
        rules = rules2
    elif l % 3 == 0:
        size = 3
        rules = rules3

    for sub in split(grid, size):
        sub_str = grid_to_str(sub)
        if s := rules.get(sub_str, None):
            new_grid.append(str_to_grid(s))

    grid = merge(np.array(new_grid))


print(f"Part1: {part1}")
assert 123 == part1 

part2 = np.count_nonzero(grid == '#')
print(f"Part2: {part2}")
assert 1984683 == part2

print(time.time() - start)
# correct answer: 1984683, in 325 seconds
