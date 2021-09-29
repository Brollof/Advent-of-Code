import re
from collections import defaultdict


with open('input.txt') as file:
    data = file.read()


ALLERGENS = defaultdict(list)
FOOD = []
KNOWN = []


for line in data.splitlines():
    if m := re.search(r'(.+) \(contains (.+)\)', line):
        food = m[1].split(' ')
        allergens = m[2].split(', ')
        FOOD.append(food)
        for a in allergens:
            ALLERGENS[a].append(food)
    else:
        assert False, "chujowy regex?"


def learn(alg):
    # generate common ingredients
    common = set.intersection(*map(set, ALLERGENS[alg]))
    
    # remove known ingredients
    for known_ing, _ in KNOWN:
        try:
            common.remove(known_ing)
        except:
            pass

    # if 1 left, add to known
    if len(common) == 1:
        KNOWN.append((*common, alg))


while len(KNOWN) < len(ALLERGENS):
    for alg in ALLERGENS:
        learn(alg)

cnt = 0
known_ing = set(ing for ing, alg in KNOWN)
cnt = sum(len(set(food) - known_ing) for food in FOOD)
print(f"Part 1: {cnt}")

result = ','.join(ing for ing, _ in sorted(KNOWN, key=lambda x: x[1]))
print(f"Part 2: {result}")