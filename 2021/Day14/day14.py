from collections import Counter


def run_polymer(template, rules, steps):
    elements = Counter(template)
    pairs_count = Counter(template[i: i + 2] for i in range(len(template) - 1))

    for _ in range(steps):
        new_pairs = Counter()
        for pair, cnt in pairs_count.items():
            b = rules[pair]
            a, c = pair
            new_pairs[a + b] += cnt
            new_pairs[b + c] += cnt
            elements[b] += cnt
        pairs_count = new_pairs

    return max(elements.values()) - min(elements.values())


with open("inp14.txt") as file:
    data = file.read()


template, rules_raw = data.split("\n\n")
rules = dict(line.split(" -> ") for line in rules_raw.splitlines())


p1 = run_polymer(template, rules, 10)
print(f"Part 2: {p1}")
assert p1 == 2891

p2 = run_polymer(template, rules, 40)
print(f"Part 2: {p2}")
assert p2 == 4607749009683
