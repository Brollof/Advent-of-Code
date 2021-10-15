import re


class Deer:
    def __init__(self, speed, fly, rest):
        self.speed = speed
        self.fly = fly
        self.rest = rest
        self.fly_temp = 0
        self.rest_temp = 0
        self.dist = 0
        self.points = 0

    def update(self):
        if self.fly_temp < self.fly:
            self.fly_temp += 1
            self.dist += self.speed
        elif self.rest_temp < self.rest:
            self.rest_temp += 1
            if self.rest_temp == self.rest:
                self.fly_temp = 0
                self.rest_temp = 0

    def reset(self):
        self.fly_temp = 0
        self.rest_temp = 0
        self.dist = 0
        self.points = 0


with open("inp14.txt") as file:
    data = file.read()


RACE_TIME = 2503
deers = {}

for name, speed, fly, rest in re.findall(r"(\w+) can fly (\d+) km/s for (\d+) .* (\d+) seconds.", data):
    deers[name] = Deer(int(speed), int(fly), int(rest))


for _ in range(RACE_TIME):
    for d in deers.values():
        d.update()

p1 = max(d.dist for d in deers.values())
print(f"Part 1: {p1}")
assert 2640 == p1


for d in deers.values():
    d.reset()

for _ in range(RACE_TIME):
    for d in deers.values():
        d.update()

    best = max(d.dist for d in deers.values())
    for d in deers.values():
        if d.dist == best:
            d.points += 1


p2 = max(d.points for d in deers.values())
print(f"Part 2: {p2}")
assert 1102 == p2
