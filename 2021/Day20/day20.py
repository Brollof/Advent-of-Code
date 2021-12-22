def run(steps, pixels):
    for step in range(steps):
        min_x, max_x = min(p[0] for p in pixels), max(p[0] for p in pixels)
        min_y, max_y = min(p[1] for p in pixels), max(p[1] for p in pixels)
        inf_pixel = step & enhancement[0]
        new_pixels = set()

        for y in range(min_y - 1, max_y + 2):
            for x in range(min_x - 1, max_x + 2):
                idx = 0
                for dy in (-1, 0, 1):
                    for dx in (-1, 0, 1):
                        idx <<= 1
                        if min_x <= x + dx <= max_x and min_y <= y + dy <= max_y:
                            idx |= int((x + dx, y + dy) in pixels)
                        else:
                            idx |= inf_pixel

                if enhancement[idx]:
                    new_pixels.add((x, y))
        pixels = new_pixels

    return len(pixels)


with open('inp20.txt') as file:
    data = file.read()


enhancement, image = data.split("\n\n")
enhancement = [int(ch == '#') for ch in enhancement]
pixels = set((x, y) for y, row in enumerate(image.splitlines()) for x, c in enumerate(row) if c == '#')


p1 = run(2, pixels)
print(f"Part 1: {p1}")
assert p1 == 5884

p2 = run(50, pixels)
print(f"Part 2: {p2}")
assert p2 == 19043
