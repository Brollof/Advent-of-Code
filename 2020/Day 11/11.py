from copy import deepcopy

seats = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""

TAKEN = "#"
EMPTY = "L"
FLOOR = "."

with open("input.txt") as file:
    seats = file.read()

SEATS = [list(line) for line in seats.splitlines()]
O_SEATS = deepcopy(SEATS)
MAX_X = len(SEATS[0])
MAX_Y = len(SEATS)


def print_seats():
    print('=' * 20)
    for y in range(MAX_Y):
        for x in range(MAX_X):
            print(SEATS[y][x], end='')
        print()
    print('=' * 20)


# Count number of adjacent seats which are occupied
def cnt_adj(x, y):
    taken_cnt = 0
    for j in (-1, 0, 1):
        for i in (-1, 0, 1):
            if j == i == 0:
                continue
            cx, cy = x + i, y + j
            if cx >= 0 and cy >= 0 and cx < MAX_X and cy < MAX_Y and SEATS[cy][cx] == TAKEN:
                taken_cnt += 1
    return taken_cnt


def cnt_in_sight(x, y):
    ox, oy = x, y
    in_sight = 0

    # up
    x, y = ox, oy
    while y > 0:
        y -= 1
        if SEATS[y][ox] == EMPTY:
            break
        if SEATS[y][ox] == TAKEN:
            in_sight += 1
            break

    # down
    x, y = ox, oy
    while y < MAX_Y - 1:
        y += 1
        if SEATS[y][ox] == EMPTY:
            break
        if SEATS[y][ox] == TAKEN:
            in_sight += 1
            break

    # right
    x, y = ox, oy
    while x < MAX_X - 1:
        x += 1
        if SEATS[oy][x] == EMPTY:
            break
        if SEATS[oy][x] == TAKEN:
            in_sight += 1
            break

    # left
    x, y = ox, oy
    while x > 0:
        x -= 1
        if SEATS[oy][x] == EMPTY:
            break
        if SEATS[oy][x] == TAKEN:
            in_sight += 1
            break

    # left, up
    x, y = ox, oy
    while x > 0 and y > 0:
        x, y = x - 1, y - 1
        if SEATS[y][x] == EMPTY:
            break
        if SEATS[y][x] == TAKEN:
            in_sight += 1
            break

    # right, up
    x, y = ox, oy
    while x < MAX_X - 1 and y > 0:
        x, y = x + 1, y - 1
        if SEATS[y][x] == EMPTY:
            break
        if SEATS[y][x] == TAKEN:
            in_sight += 1
            break

    # left, down
    x, y = ox, oy
    while x > 0 and y < MAX_Y - 1:
        x, y = x - 1, y + 1
        if SEATS[y][x] == EMPTY:
            break
        if SEATS[y][x] == TAKEN:
            in_sight += 1
            break

    # right, down
    x, y = ox, oy
    while x < MAX_X - 1 and y < MAX_Y - 1:
        x, y = x + 1, y + 1
        if SEATS[y][x] == EMPTY:
            break
        if SEATS[y][x] == TAKEN:
            in_sight += 1
            break

    return in_sight


def round(count_method, tolerance):
    global SEATS
    changes = 0
    new_seats = deepcopy(SEATS)
    for y in range(MAX_Y):
        for x in range(MAX_X):
            seat = SEATS[y][x]
            if seat == FLOOR:
                continue

            adj_taken_cnt = count_method(x, y)
            if seat == EMPTY and adj_taken_cnt == 0:
                changes += 1
                new_seats[y][x] = TAKEN
            elif seat == TAKEN and adj_taken_cnt >= tolerance:
                changes += 1
                new_seats[y][x] = EMPTY
    SEATS = new_seats
    return changes


def cnt_taken_all():
    taken = 0
    for y in range(MAX_Y):
        for x in range(MAX_X):
            if SEATS[y][x] == TAKEN:
                taken += 1
    return taken


round_cnt = 0
while changes := round(cnt_adj, 4):
    round_cnt += 1

# part 1
print(round_cnt, cnt_taken_all())


# restore original placement
SEATS = O_SEATS

round_cnt = 0
while changes := round(cnt_in_sight, 5):
    round_cnt += 1

# part 2
print(round_cnt, cnt_taken_all())
