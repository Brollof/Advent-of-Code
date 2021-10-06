with open(r"input.txt") as file:
    grid = [list(line) for line in file.read().splitlines() if len(line.strip()) > 0]


def change_dir(grid, x, y):
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
            if grid[ny][nx] in "|-" or grid[ny][nx].isalpha():
                return (dx, dy)
    raise Exception(f"New direction not found! {x=}, {y=}")


x, y = grid[0].index('|'), 0
dx, dy = 0, 1
letters = ''
steps = 0

while 0 <= x < len(grid[0]) and 0 <= y < len(grid):
    c = grid[y][x]
    grid[y][x] = '#'

    if c == ' ':
        break

    steps += 1
    if c == '+':
        dx, dy = change_dir(grid, x, y)
    elif c.isalpha():
        letters += c

    x, y = x + dx, y + dy


print(f"Part 1: {letters}")
assert "RUEDAHWKSM" == letters


print(f"Part 2: {steps}")
assert 17264 == steps