import re
import numpy

with open("input.txt") as file:
    data = file.read()

def calc_pos(s0, v0, a, t):
    def c1():
        vtprev = v0 + a * (t + 1)
        return int(s0 + ((v0 + vtprev) * t) // 2)
    def c2():
        return int(s0 + t * v0 + (a * t * (t + 1)) // 2)
    def c3():
        return int(((t * t * a) / 2) + t * (a + 2 * v0)/2 + s0)

    assert c1() == c2() == c3(), f"{c1()=}, {c2()=}, {c3()=}"
    return c2()

def get_coefs(p):
    ax = p['a'][0] / 2
    bx = (p['a'][0] + 2 * p['v'][0]) / 2
    cx = p['p'][0]

    ay = p['a'][1] / 2
    by = (p['a'][1] + 2 * p['v'][1]) / 2
    cy = p['p'][1]

    az = p['a'][2] / 2
    bz = (p['a'][2] + 2 * p['v'][0]) / 2
    cz = p['p'][2]

    return [(ax, bx, cx), (ay, by, cy), (az, bz, cz)]


def check_roots(p1, p2):
    coefs1 = get_coefs(p1)
    coefs2 = get_coefs(p2)
    coefsx = [x - y for (x, y) in zip(coefs1[0], coefs2[0])]
    coefsy = [x - y for (x, y) in zip(coefs1[1], coefs2[1])]
    coefsz = [x - y for (x, y) in zip(coefs1[2], coefs2[2])]
    r_x = numpy.roots(coefsx)
    r_y = numpy.roots(coefsy)
    r_z = numpy.roots(coefsz)
    print(r_x)
    print(r_y)
    print(r_z)
    if "j" in str(r_x) or "j" in str(r_y) or "j" in str(r_z):
        return False
    s = set()
    s.update(r_x)
    s.update(r_y)
    s.update(r_z)

    # print(r_x[1] == r_y[0])

    return len(s) < 6

    # x_r = numpy.roots(coefs[0])
    # y_r = numpy.roots(coefs[1])
    # z_r = numpy.roots(coefs[2])
    # print("Particle 1 X Y Z")
    # print(x_r, y_r, z_r)

    # coefs = get_coefs(p2)
    # x_r = numpy.roots(coefs[0])
    # y_r = numpy.roots(coefs[1])
    # z_r = numpy.roots(coefs[2])
    # print("Particle 2 X Y Z")
    # print(x_r, y_r, z_r)


particles = []

for i, line in enumerate(data.splitlines()):
    r = re.findall(r"p=<(-?\d+),(-?\d+),(-?\d+)>, v=<(-?\d+),(-?\d+),(-?\d+)>, a=<(-?\d+),(-?\d+),(-?\d+)>",line)[0]
    r = tuple(map(int, r))
    particles += [{'p': r[:3], 'v': r[3:6], 'a': r[6:]}]


# collide = set()
# p_len = len(particles)

# for i in range(p_len):
#     for j in range(i + 1, p_len):
#         if i * j == 1000:
#             print(i, j)
#         if check_roots(particles[i], particles[j]):
#             # print(f'to delete {i=}, {j=}')
#             collide.add(i)
#             collide.add(j)
#     print(len(collide))

# for idx in collide:
#     print(f'deleting {idx}')
#     del particles[idx]

# print(particles[0])

# step=38, i=66, j=67, (-13, 25, -2)
# step=38, i=66, j=68, (-13, 25, -2)

# step=9, i=468, j=470, (-1, -18, -24)
# step=9, i=469, j=470, (-1, -18, -24)

P1_IDX = 66
P2_IDX = 67
STEP = 26
# {'p': (-48, 67, -33), 'v': (45, -81, 14), 'a': (2, -4, -5)} {'p': (248, -33, -142), 'v': (-233, 15, 116), 'a': (-16, 0, 2)}
x1 = calc_pos(particles[P1_IDX]['p'][0], particles[P1_IDX]['v'][0], particles[P1_IDX]['a'][0], STEP)
x2 = calc_pos(particles[P2_IDX]['p'][0], particles[P2_IDX]['v'][0], particles[P2_IDX]['a'][0], STEP)

y1 = calc_pos(particles[P1_IDX]['p'][1], particles[P1_IDX]['v'][1], particles[P1_IDX]['a'][1], STEP)
y2 = calc_pos(particles[P2_IDX]['p'][1], particles[P2_IDX]['v'][1], particles[P2_IDX]['a'][1], STEP)

z1 = calc_pos(particles[P1_IDX]['p'][2], particles[P1_IDX]['v'][2], particles[P1_IDX]['a'][2], STEP)
z2 = calc_pos(particles[P2_IDX]['p'][2], particles[P2_IDX]['v'][2], particles[P2_IDX]['a'][2], STEP)

print(f"{x1=}, {x2=}")
print(f"{y1=}, {y2=}")
print(f"{z1=}, {z2=}")

z = check_roots(particles[P1_IDX], particles[P2_IDX])



