with open("inp2.txt") as file:
    data = file.read()


horizontal_pos = 0
depth_1, depth_2 = 0, 0
aim = 0

for line in data.splitlines():
    cmd, value = line.split()
    value = int(value)
    match cmd:
        case 'forward':
            horizontal_pos += value
            depth_2 += aim * value
        case 'up':
            depth_1 -= value
            aim -= value
        case 'down':
            depth_1 += value
            aim += value


p1 = depth_1 * horizontal_pos
print(f"Part 1: {p1}")
assert 1694130 == p1

p2 = depth_2 * horizontal_pos
print(f"Part 2: {p2}")
assert 1698850445 == p2
