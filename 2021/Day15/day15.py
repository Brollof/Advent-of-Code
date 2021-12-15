from queue import PriorityQueue


def dijkstra(grid, x, y):
    max_x = len(grid[0])
    max_y = len(grid)
    D = [[float('inf')] * max_x for _ in range(max_y)]
    D[y][x] = 0

    pq = PriorityQueue()
    pq.put((0, x, y))
    # visited = set()

    while not pq.empty():
        _, x, y = pq.get()
        # visited.add((x, y))

        for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= nx < max_x and 0 <= ny < max_y:
                dist = grid[ny][nx]
                # if (nx, ny) not in visited:
                old_dist = D[ny][nx]
                new_dist = D[y][x] + dist
                if new_dist < old_dist:
                    pq.put((new_dist, nx, ny))
                    D[ny][nx] = new_dist
    return D


with open("inp15.txt") as file:
    data = file.read()


grid = [list(map(int, list(line))) for line in data.splitlines()]
MAX_X_SMALL, MAX_Y_SMALL = len(grid[0]), len(grid)
MAX_X_LARGE, MAX_Y_LARGE = MAX_X_SMALL * 5, MAX_Y_SMALL * 5

large_grid = [[None] * MAX_X_LARGE for _ in range(MAX_Y_LARGE)]
for y in range(MAX_Y_SMALL):
    for x in range(MAX_X_SMALL):
        for j in range(5):
            for i in range(5):
                large_grid[y + j * MAX_Y_SMALL][x + i * MAX_X_SMALL] = (grid[y][x] - 1 + i + j) % 9 + 1


path = dijkstra(grid, 0, 0)
p1 = path[-1][-1]
print(f"Part 1: {p1}")
assert p1 == 741


path = dijkstra(large_grid, 0, 0)
p2 = path[-1][-1]
print(f"Part 2: {p2}")
assert p2 == 2976
