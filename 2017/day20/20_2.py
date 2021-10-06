import re

with open("input.txt") as file:
    data = file.read()


particles = []

for i, line in enumerate(data.splitlines()):
    r = re.findall(r"p=<(-?\d+),(-?\d+),(-?\d+)>, v=<(-?\d+),(-?\d+),(-?\d+)>, a=<(-?\d+),(-?\d+),(-?\d+)>",line)[0]
    r = list(map(int, r))
    particles += [{'p': r[:3], 'v': r[3:6], 'a': r[6:]}]


STEPS = 40
p_len = len(particles)

for step in range(STEPS):
    for p in particles:
        if p:
            for i in range(3):
                p['v'][i] += p['a'][i]
                p['p'][i] += p['v'][i]

    collide = set()
    for i in range(p_len):
        for j in range(i + 1, p_len):
            if particles[i] and particles[j] and particles[i]['p'] == particles[j]['p']:
                collide.update((i, j))

    for i in collide:
        particles[i] = None


p2 = sum(1 for p in particles if p)
print(f"Part 2: {p2}")
assert 448 == p2
