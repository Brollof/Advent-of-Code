from itertools import combinations

with open("input.txt") as file:
    data = file.read()

s1, s2 = 0, 0
for line in data.splitlines():
    nums = sorted([int(n) for n in line.split()])
    
    s1 += nums[-1] - nums[0]
    s2 += sum(b // a for a, b in combinations(nums, 2) if b % a == 0)


print(f"Part 1: {s1}")
assert 46402 == s1

print(f"Part 2: {s2}")
assert 265 == s2
