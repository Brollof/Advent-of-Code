with open("inp2.txt") as file:
    data = file.read()


total_area = 0
ribbon = 0
for line in data.splitlines():
    a, b, c = sorted(int(n) for n in line.split("x"))
    total_area += 2 * (a * b + b * c + a * c) + a * b
    ribbon += 2 * (a + b) + a * b * c


print(f"Part 1: {total_area}")
assert 1606483 == total_area

print(f"Part 2: {ribbon}")
assert 3842356 == ribbon
