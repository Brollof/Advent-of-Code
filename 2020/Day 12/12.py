
data = """F10
N3
F7
R90
F11"""

with open('input.txt') as file:
    data = file.read()

instructions = []
for line in data.splitlines():
    line = line.strip()
    d, v = line[0], int(line[1:])
    instructions.append((d, v))


dirs = ['E', 'S', 'W', 'N']

ship_dir = 'E'
x, y = 0, 0

def turn(d, v):
    global ship_dir

    turns = v // 90
    ci = dirs.index(ship_dir)
    if d == 'R':
        ship_dir = dirs[(ci + turns) % len(dirs)]
    else: # should be left, right?
        ship_dir = dirs[(ci - turns) % len(dirs)]


def swim(d, v):
    global x, y

    if d == 'N':
        y += v
    elif d == 'S':
        y -= v
    elif d == 'E':
        x += v
    elif d == 'W':
        x -= v
    else:
        assert False


for d, v in instructions:
    if d in 'LR':
        turn(d, v)
    elif d in 'NSWE':
        swim(d, v)
    elif d == 'F':
        swim(ship_dir, v)

print(x, y, abs(x) + abs(y))

