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
MAX_X = len(SEATS[0])
MAX_Y = len(SEATS)


def print_seats():
    s = '\n'.join(''.join(row) for row in SEATS)
    print('=' * 20)
    print(s)
    print('=' * 20)
    return s


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


def round(count_method):
    global SEATS
    changes = 0
    new_seats = deepcopy(SEATS)
    for y in range(MAX_Y):
        for x in range(MAX_X):
            seat = SEATS[y][x]
            # print(seat, end='')
            if seat == FLOOR:
                continue

            adj_taken_cnt = count_method(x, y)
            if seat == EMPTY and adj_taken_cnt == 0:
                changes += 1
                new_seats[y][x] = TAKEN
            elif seat == TAKEN and adj_taken_cnt >= 5:
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


r1 = """#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##"""

r2 = """#.LL.LL.L#
#LLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLLL.L
#.LLLLL.L#"""

r3 = """#.L#.##.L#
#L#####.LL
L.#.#..#..
##L#.##.##
#.##.#L.##
#.#####.#L
..#.#.....
LLL####LL#
#.L#####.L
#.L####.L#"""


round_cnt = 0
while changes := round(cnt_in_sight):
    round_cnt += 1

# z = cnt_in_sight(3, 0)
# print(z)

# a = round(cnt_in_sight)
# print(print_seats() == r1)

# round(cnt_in_sight)
# print(print_seats() == r2)

# round(cnt_in_sight)
# print(print_seats() == r3)



print(round_cnt, cnt_taken_all())


#