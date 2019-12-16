from icc import ICC
import matplotlib.pyplot as plt


BLACK, WHITE = 0, 1
LEFT = {(0, 1): (-1, 0), (-1, 0): (0, -1), (0, -1): (1, 0), (1, 0): (0, 1)}
RIGHT = {v: k for k, v in LEFT.items()}


def move(pos, cur_dir, turn):
    x, y = pos
    if turn:
        cur_dir = RIGHT[cur_dir]
    else:
        cur_dir = LEFT[cur_dir]
    return (x + cur_dir[0], y + cur_dir[1]), cur_dir


def compute(icc, inp):
    new_color = icc.run(inp)
    if new_color is None:
        return None
    dire = icc.run(inp)
    if dire is None:
        return None
    return new_color, dire


def paint(icc, start_color):
    area = {(0, 0): start_color}
    pos = (0, 0)
    cur_dir = (0, 1)
    while True:
        if pos in area:
            color = area[pos]
        else:
            color = BLACK
        data = compute(icc, color)
        if data:
            color, turn = data
            area[pos] = color
            pos, cur_dir = move(pos, cur_dir, turn)
        else:
            break
    return area


with open("input.txt") as file:
    intcode = file.read()

icc = ICC(intcode)

# part 1
painted = paint(icc, BLACK)
print(len(painted)) # 2322

# part 2
icc.restart()
painted = paint(icc, WHITE)
painted = [k for k, v in painted.items() if v == WHITE]

for x, y in painted:
    plt.scatter(x, y, s=50, c=[[0,0,0]])
plt.show()