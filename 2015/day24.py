from itertools import combinations
from functools import reduce
from operator import mul


with open("inp24.txt") as file:
    data = file.read()

weights = [int(x) for x in data.split()]
weights = list(reversed(weights))


target_weight = sum(weights) // 3

best_len = float('inf')
best_qe = float('inf')


def go(current=set(), sum_weights=0, current_len=0, current_qe=1):
    global best_len
    global best_qe

    if current_qe >= best_qe or current_len > best_len or sum_weights > target_weight:
        return

    if sum_weights == target_weight:
        if current_qe < best_qe:
            best_qe = current_qe
            best_len = current_len
            print(best_len, best_qe, current)
        return

    for w in weights:
        if w not in current:
            go(current | {w}, sum_weights + w, current_len + 1, current_qe * w)


def run(n):
    target_weight = sum(weights) // n
    for i in range(len(weights)):
        if qe := [reduce(mul, c) for c in combinations(weights, i) if sum(c) == target_weight]:
            return min(qe)



p1 = run(3)
print(f"Part 1: {p1}")
assert 11266889531 == p1

p2 = run(4)
print(f"Part 1: {p2}")
assert 77387711 == p2
