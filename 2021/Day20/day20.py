from copy import deepcopy


def resize(image, step=0):
    c, n = '.', 50
    for row in image:
        for _ in range(n):
            row.insert(0, c)
        row.extend([c] * n)

    cols = len(image[0])

    for _ in range(n):
        image.insert(0, [c] * cols)
        image.append([c] * cols)


def print_grid(grid):
    for row in grid:
        print(''.join(row))


def get_pixel(x, y, image, step):
    if 0 <= x < len(image[0]) and 0 <= y < len(image):
        return image[y][x]
    return '.' if step % 2 == 0 else '#'


def run(steps, image):
    new_image = deepcopy(image)

    for step in range(steps):
        old_image = deepcopy(new_image)
        for y in range(len(old_image)):
            for x in range(len(old_image[0])):
                line = ''
                line += get_pixel(x - 1, y - 1, old_image, step)
                line += get_pixel(x + 0, y - 1, old_image, step)
                line += get_pixel(x + 1, y - 1, old_image, step)

                line += get_pixel(x - 1, y + 0, old_image, step)
                line += get_pixel(x + 0, y + 0, old_image, step)
                line += get_pixel(x + 1, y + 0, old_image, step)

                line += get_pixel(x - 1, y + 1, old_image, step)
                line += get_pixel(x + 0, y + 1, old_image, step)
                line += get_pixel(x + 1, y + 1, old_image, step)

                binary = line.replace('#', '1').replace('.', '0')
                new_image[y][x] = enhancement[int(binary, base=2)]

    return sum(1 for y in range(len(new_image)) for x in range(len(new_image[0])) if new_image[y][x] == '#')


with open("inp20.txt") as file:
    data = file.read()


enhancement, image = data.split("\n\n")
image = [list(line) for line in image.splitlines()]
resize(image)


p1 = run(2, image)
print(f"Part 1: {p1}")
assert p1 == 5884


p2 = run(50, image)
print(f"Part 2: {p2}")
assert p2 == 19043
