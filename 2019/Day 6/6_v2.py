from collections import defaultdict

def bfs(root):
    levels = {root: 0}
    visited = defaultdict(bool, {root: True})
    q = [root]

    while len(q) > 0:
        planet = q.pop()
        for p in space[planet]:
            if not visited[p]:
                visited[p] = True
                levels[p] = levels[planet] + 1
                q.append(p)
    return levels


with open("input.txt") as file:
    data = file.read()


space = defaultdict(list)
for line in data.splitlines():
    l, r = line.split(")")
    space[r].append(l)
    space[l].append(r)


levels = bfs("COM")
p1 = sum(levels.values())
print(f"Part 1: {p1}")
assert 194721 == p1


levels = bfs("YOU")
p2 = levels['SAN'] - 2
assert 316 == p2
print(f"Part 2: {p2}")
