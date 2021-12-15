from queue import PriorityQueue


def dijkstra(grid, start_vertex):
    max_x = len(grid[0])
    max_y = len(grid)
    D = {(x, y): float('inf') for y in range(max_y) for x in range(max_x)}
    D[start_vertex] = 0
    x, y = start_vertex

    pq = PriorityQueue()
    pq.put((grid[y][x], start_vertex))
    visited = set()

    while not pq.empty():
        _, current_vertex = pq.get()
        visited.add(current_vertex)
        x, y = current_vertex

        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            if 0 <= x + dx < max_x and 0 <= y + dy < max_y:
                dist = grid[y + dy][x + dx]
                neighour = (x + dx, y + dy)
                if neighour not in visited:
                    old_dist = D[neighour]
                    new_dist = D[(current_vertex)] + dist
                    if new_dist < old_dist:
                        pq.put((new_dist, neighour))
                        D[neighour] = new_dist
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


path = dijkstra(grid, (0, 0))
p1 = path[(MAX_X_SMALL - 1, MAX_Y_SMALL - 1)]
print(p1)
assert p1 == 741


path = dijkstra(large_grid, (0, 0))
p2 = path[(MAX_X_LARGE - 1, MAX_Y_LARGE - 1)]
print(p2)
assert p2 == 2976
