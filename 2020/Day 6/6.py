from functools import reduce

with open('input.txt') as file:
    data = file.read().split('\n\n')

part1 = 0
for group in data:
    part1 += len(set(group.replace('\n', '')))

print(part1)

part2 = 0
for group in data:
    part2 += len(reduce(set.intersection, map(set, group.splitlines())))

print(part2)
