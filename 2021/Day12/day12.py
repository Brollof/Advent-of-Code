from collections import defaultdict


def dfs(graph, currentVertex, part, path=[]):
    results = []
    new_path = path + [currentVertex]

    if currentVertex == 'end':
        return [new_path]

    for vertex in graph[currentVertex]:
        if vertex == 'start' and vertex in path:
            continue
        small = set()
        limit = part
        for v in new_path:
            if v.islower():
                if v in small:
                    limit = 1
                    break
                else:
                    small.add(v)
        if path.count(vertex) < limit or vertex.isupper():
            new_results = dfs(graph, vertex, part, new_path)
            results.extend(new_results)
    return results


with open("inp12.txt") as file:
    data = file.read()


caves = defaultdict(list)

for line in data.splitlines():
    c1, c2 = line.split("-")
    caves[c1].append(c2)
    caves[c2].append(c1)


paths = dfs(caves, 'start', 1)
p1 = sum(1 for p in paths if 'end' in p)
print(f"Part 1: {p1}")
assert p1 == 3856

paths = dfs(caves, 'start', 2)
p2 = sum(1 for p in paths if 'end' in p)
print(f"Part 2: {p2}")
assert p2 == 116692
