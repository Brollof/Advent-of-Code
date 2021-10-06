def go(ports, bridge, tail=None):
    long_strong.add((len(bridge), sum(a + b for a, b in bridge)))

    if tail is None:
        tail = bridge[-1][-1]

    for port in ports:
        if tail in port:
            a, b = port
            new_tail = b if a == tail else a
            go(ports - {port}, bridge[::] + [port], new_tail)


with open("input.txt") as file:
    data = file.read()

ports = set()
long_strong = set()
zero_pin = []

for line in data.splitlines():
    port = tuple(int(x) for x in line.split("/"))
    ports.add(port)
    if 0 in port:
        zero_pin.append(port)

for port in zero_pin:
    a, b = port
    if b == 0:
        a, b = b, a
    go(ports - {port}, [(a, b)])


p1 = sorted(long_strong, key=lambda v: v[1])[-1][1]
p2 = sorted(long_strong,)[-1][1]


print(f"Part 1: {p1}")
assert 1868 == p1


print(f"Part 2: {p2}")
assert 1841 == p2
