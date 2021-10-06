class Planet:
    def __init__(self, idx):
        self.idx = idx
        self.next = None
        self.prevs = []

    def __repr__(self):
        return f"{self.idx}"


def build_orbit_map(data):
    planets = {"COM": Planet("COM")}
    for rel in data:
        idx1, idx2 = rel.split(")")
        if idx1 not in planets:
            planets[idx1] = Planet(idx1)

        if idx2 not in planets:
            planets[idx2] = Planet(idx2)

        p1, p2 = planets[idx1], planets[idx2]
        p2.next = p1
        p1.prevs.append(p2)
    return planets


def counter(planet, cnt=0):
    if planet.next:
        return counter(planet.next, cnt + 1)
    return cnt


def traverse(start, end, cnt=0, checked=[]):
    to_check = [p for p in start.prevs + [start.next] if p not in checked]
    if end in to_check:
        return cnt - 1
    else:
        checked.extend(to_check)
        for p in to_check:
            if val := traverse(p, end, cnt + 1, checked):
                return val
            # if val:


with open("input.txt") as file:
    data = file.read().split()

planets = build_orbit_map(data)

total_orbits = 0
for planet in planets.values():
    total_orbits += counter(planet)

# part 1
print(total_orbits)
assert 194721 == total_orbits

# part 2
p2 = traverse(planets["YOU"], planets["SAN"])
print(p2)
assert 316 == p2