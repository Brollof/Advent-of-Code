import math


with open('input.txt') as file:
    data = file.read()

instructions = []
for line in data.splitlines():
    line = line.strip()
    instructions.append((line[0], int(line[1:])))


class Waypoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def rotate(self, direction, angle_deg):
        # By default perform clock-wise rotation
        if direction == 'L':
            angle_deg *= -1
        angle_rad = math.radians(angle_deg)
        x = round(math.cos(angle_rad) * self.x + math.sin(angle_rad) * self.y)
        y = round(-math.sin(angle_rad) * self.x + math.cos(angle_rad) * self.y)
        self.x, self.y = x, y

    def move(self, direction, value):
        if direction == 'N':
            self.y += value
        elif direction == 'S':
            self.y -= value
        elif direction == 'E':
            self.x += value
        elif direction == 'W':
            self.x -= value

    def __str__(self):
        return f"WP({self.x}, {self.y})"


wp = Waypoint(10, 1) # 10E, 1N
sx, sy = 0, 0

for d, v in instructions:
    if d in 'LR':
        wp.rotate(d, v)
    elif d in 'NSWE':
        wp.move(d, v)
    elif d == 'F':
        sx = sx + (v * wp.x)
        sy = sy + (v * wp.y)

print(sx, sy, abs(sx) + abs(sy))

