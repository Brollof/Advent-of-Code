import re

with open('input.txt') as file:
    data = file.read()

G = {}

# parse input
for line in data.splitlines():
    m = re.search(r'(\w+ \w+) bags contain (.*) bag', line)
    bags = [(int(n), color) for n, color in re.findall(r'(\d+) (\w+ \w+)', m[2])]
    G[m[1]] = bags


visited_bags = []
check_bags = ['shiny gold']

while len(check_bags):
    if (to_check := check_bags.pop()) in visited_bags:
        continue
    visited_bags.append(to_check)
    for parent_color, bags in G.items():
        for n, color in bags:
            if color == to_check:
                check_bags.append(parent_color)

# part 1
print(len(visited_bags) - 1) # don't count the shiny gold bag


def count_bags(bag):
    if not (bags := G[bag]):
        return 1
    total = 1
    for cnt, bag in bags:
        total += cnt * count_bags(bag)
    return total

# part 2
print(count_bags('shiny gold') - 1)