WIDTH, HEIGHT = 25, 6
SIZE = WIDTH * HEIGHT

with open("input.txt") as file:
    data = file.read()

layers = [data[i:i+SIZE] for i in range(0, len(data), SIZE)]

# part 1
min_layer = min(layers, key=lambda layer: layer.count("0"))
print(min_layer.count("1") * min_layer.count("2"))

# part 2
image = [[c for c in layer if c != "2"][0] for layer in zip(*layers)]
for i in range(SIZE):
    if i % WIDTH == 0:
        print(''.join(image[i:i+WIDTH]).replace('0',' '))