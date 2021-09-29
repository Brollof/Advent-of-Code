with open('input.txt') as file:
    data = file.readlines()


part1, part2 = 0, 0
for line in data:
    policy, password = line.split(":")
    limits, char = policy.split(' ')
    lo, hi = [int(v) for v in limits.split('-')]
    password = password.strip()

    if lo <= password.count(char) <= hi:
        part1 += 1

    if (password[lo - 1] == char) ^ (password[hi - 1] == char):
        part2 += 1


print(part1)
print(part2)
