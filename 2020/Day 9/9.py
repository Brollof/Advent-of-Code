with open('input.txt') as file:
    data = [int(line.strip()) for line in file]

WL = 25

def add_up_to(t, n):
    t = sorted(t)
    for i in range(len(t)):
        for j in range(i + 1, len(t)):
            if t[i] != t[j] and t[i] + t[j] == n:
                return True
    return False

part1 = 0
for i in range(WL, len(data)):
    if not add_up_to(data[i - WL: i], data[i]):
        part1 = data[i]
        break

print(f"part1: {part1}")


############################################################################
############################################################################
############################################################################

def part2():
    for begin in range(len(data)):
        for end in range(begin + 2, len(data)):
            if sum(data[begin: end]) == part1:
                # print(data[begin: end])
                print(f"part2: {min(data[begin: end]) + max(data[begin: end])}")
                return

part2()