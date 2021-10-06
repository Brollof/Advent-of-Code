def dir_to_offset(dire):
	if dire == 'n':  return (0, 1, -1)
	if dire == 'ne': return (1, 0, -1)
	if dire == 'se': return (1, -1, 0)
	if dire == 's':  return (0, -1, 1)
	if dire == 'sw': return (-1, 0, 1)
	if dire == 'nw': return (-1, 1, 0)
	raise Exception(f"Unknown direction: {dire}")


def distance_from_zero(x, y, z):
	return max(abs(x), abs(y), abs(z))


with open('input.txt') as file:
	dirs = file.read().split(',')


x, y, z = 0, 0, 0
longest = 0

for dire in dirs:
	dx, dy, dz = dir_to_offset(dire)
	x, y, z = x + dx, y + dy, z + dz
	longest = max(longest, distance_from_zero(x, y, z))


dist = distance_from_zero(x, y, z)
print(f"Part 1: {dist}")
assert 761 == dist

print(f"Part 2: {longest}")
assert 1542 == longest