with open("inp7.txt") as file:
    crabs = [int(n) for n in file.read().split(",")]

fuel1 = float("inf")
fuel2 = float("inf")

for pos in range(min(crabs), max(crabs) + 1):
    f1, f2 = 0, 0
    for crab in crabs:
        steps = abs(pos - crab)
        f1 += steps
        f2 += steps * (1 + steps) // 2

    fuel1 = min(fuel1, f1)
    fuel2 = min(fuel2, f2)


print(f"Part 1: {fuel1}")
assert fuel1 == 364898

print(f"Part 2: {fuel2}")
assert fuel2 == 104149091
