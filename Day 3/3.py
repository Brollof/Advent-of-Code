def get_data():
    with open("input.txt") as file:
        return map(str.strip, file.readlines())


def get_wire_points(wire):
    x = y = steps = 0
    points = []
    wire = [(val[0], int(val[1:])) for val in wire.split(",")]

    for dire, length in wire:
        if dire == "R":
            points.extend((x + i, y, steps + i) for i in range(1, length + 1))
            x += length
        elif dire == "L":
            points.extend((x - i, y, steps + i) for i in range(1, length + 1))
            x -= length
        elif dire == "U":
            points.extend((x, y + i, steps + i) for i in range(1, length + 1))
            y += length
        elif dire == "D":
            points.extend((x, y - i, steps + i) for i in range(1, length + 1))
            y -= length
        steps += length

    return points


# get raw data
w1_raw, w2_raw = get_data()

# list of wire points (x, y, steps)
w1 = get_wire_points(w1_raw)
w2 = get_wire_points(w2_raw)

# dict where key is tuple (x, y) and the value is steps count
w1_d = {data[:2]: data[2] for data in w1}
w2_d = {data[:2]: data[2] for data in w2}

# get locations where wires cross
inter = set(w1_d.keys()).intersection(w2_d.keys())

# calculate distance for every intersection
dists = [abs(pos[0]) + abs(pos[1]) for pos in inter]

# part1
print(min(dists))

# part 2
# calculate wires length for every intersection
steps = [w1_d[pos] + w2_d[pos] for pos in inter]
print(min(steps))