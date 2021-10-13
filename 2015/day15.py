import re
from itertools import permutations, combinations_with_replacement


class Ingredient:
    def __init__(self, props, cal):
        self.props = [int(p) for p in props]
        self.cal = int(cal)

    def __repr__(self):
        return f"({self.props}, {self.cal})"


def calc_score(rec, spoons):
    out = 1
    calories = 0
    for amount in zip(*(r.props for r in rec.values())):
        out *= max(0, sum(v * m for v, m in zip(amount, spoons)))

    for amt, cal in zip((r.cal for r in rec.values()), spoons):
        calories += amt * cal
    return out, calories


with open("inp15.txt") as file:
    data = file.read()


rec = {}

for d in re.findall(r"(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)", data):
    name, *props, cal = d
    rec[name] = Ingredient(props, cal)


best_score_p1 = 0
best_score_p2 = 0
combs = (vals for vals in combinations_with_replacement(range(1, 100), len(rec)) if sum(vals) == 100)

for comb in combs:
    for vals in permutations(comb, len(rec)):
        score, calories = calc_score(rec, vals)
        if calories == 500:
            best_score_p2 = max(score, best_score_p2)
        best_score_p1 = max(score, best_score_p1)


print(f"Part 1: {best_score_p1}")
assert 13882464 == best_score_p1

print(f"Part 2: {best_score_p2}")
assert 11171160 == best_score_p2
