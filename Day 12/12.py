import re
from itertools import combinations
from math import gcd


class V:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_energy(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

    def __add__(self, o):
        return V(self.x + o.x, self.y + o.y, self.z + o.z)

    def __repr__(self):
        return f"({self.x},{self.y},{self.z})"


class Moon:
    def __init__(self, x, y, z):
        self.pos = V(x, y, z)
        self.vel = V(0, 0, 0)

    def get_energy(self):
        pot = self.pos.get_energy()
        kin = self.vel.get_energy()
        return pot * kin


with open("input.txt") as file:
    data = file.read()

data = re.findall(r"x=(-?\d+).*y=(-?\d+).*z=(-?\d+)", data)
data = [[int(v) for v in pos] for pos in data]
moons = [Moon(x, y, z) for x, y, z in data]


def tick(moons):
    for m1, m2 in combinations(moons, 2):
        if m1.pos.x < m2.pos.x:
            m1.vel.x += 1
            m2.vel.x -= 1
        elif m1.pos.x > m2.pos.x:
            m1.vel.x -= 1
            m2.vel.x += 1

        if m1.pos.y < m2.pos.y:
            m1.vel.y += 1
            m2.vel.y -= 1
        elif m1.pos.y > m2.pos.y:
            m1.vel.y -= 1
            m2.vel.y += 1

        if m1.pos.z < m2.pos.z:
            m1.vel.z += 1
            m2.vel.z -= 1
        elif m1.pos.z > m2.pos.z:
            m1.vel.z -= 1
            m2.vel.z += 1

    for m in moons:
        m.pos += m.vel


def lcm(x, y, z):
    gcd2 = gcd(y, z)
    gcd3 = gcd(x, gcd2)

    lcm2 = y * z // gcd2
    lcm3 = x * lcm2 // gcd(x, lcm2)
    return lcm3


steps = 0

# part 1
for i in range(1000):
    steps += 1
    tick(moons)

total_energy = sum(m.get_energy() for m in moons)
print(total_energy)


# part 2
x, y, z = 0, 0, 0
while not (x and y and z):
    steps += 1
    tick(moons)

    if not x and all(m.vel.x == 0 for m in moons):
        x = steps
    if not y and all(m.vel.y == 0 for m in moons):
        y = steps
    if not z and all(m.vel.z == 0 for m in moons):
        z = steps

print(lcm(x, y, z) * 2)