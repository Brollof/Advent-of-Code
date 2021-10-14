from collections import defaultdict


def generate(mol, rep, base):
    out = set()
    i = -1
    while (i := base.find(mol, i + 1)) != -1:
        new = base[:i] + base[i:].replace(mol, rep, 1)
        out.add(new)
    return out


with open("inp19.txt") as file:
    data = file.read()


rest, base = data.split("\n\n")
repl = defaultdict(list)
back_repl = []

for line in rest.splitlines():
    mol, out = line.split(" => ")
    repl[mol].append(out)
    back_repl.append((out, mol))


combinations = set()

for mol, to_rep in repl.items():
    for rep in to_rep:
        new = generate(mol, rep, base)
        combinations.update(new)

p1 = len(combinations)
print(f"Part 1: {p1}")
assert 535 == p1


###############################################################
#############  PART 2 not working on every input! #############
###############################################################

steps = 0
visited = set([base])
queue = [base]
steps = 0

back_repl = sorted(back_repl, key=lambda x: len(x[0]))

while queue:
    base = queue.pop()

    if base == "e":
        break

    steps += 1
    for mol, rep in back_repl:
        new = base.replace(mol, rep, 1)
        if new not in visited:
            visited.add(new)
            queue.append(new)

print(f"Part 2: {steps}")
assert 212 == steps
