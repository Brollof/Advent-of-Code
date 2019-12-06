def calc_fuel(mass):
    return mass // 3 - 2


def calc_fuel_2(mass):
    mass = mass // 3 - 2
    if mass <= 0:
        return 0
    return mass + calc_fuel_2(mass)


with open("input.txt", "r") as file:
    data = file.readlines()

total_fuel_1 = 0
total_fuel_2 = 0

for line in data:
    total_fuel_1 += calc_fuel(int(line))
    total_fuel_2 += calc_fuel_2(int(line))

# part 1
print(total_fuel_1)
# part 2
print(total_fuel_2)
