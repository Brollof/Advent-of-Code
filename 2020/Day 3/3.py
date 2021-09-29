with open("input.txt") as file:
    data = [line.strip() for line in file]


WIDTH = len(data[0])


def check_slope(slope):
    trees = 0
    px, py = 0, 0
    sx, sy = slope
    while py < len(data) - 1:
        px = (px + sx) % WIDTH
        py += sy
        if data[py][px] == '#':
            trees += 1
    return trees


# part1
print(check_slope((3, 1)))


# part2
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
trees = 1
for slope in slopes:
    trees *= check_slope(slope)
print(trees)