def sum_with_distance(nums, dist):
    s, n_len = 0, len(nums)
    for i in range(n_len):
        ni = (i + dist) % n_len
        if nums[i] == nums[ni]:
            s += nums[i]
    return s


with open("input.txt") as file:
    data = file.read()

nums = [int(c) for c in data]

p1 = sum_with_distance(nums, 1)
print(f"Part 1: {p1}")
assert 1343 == p1

p2 = sum_with_distance(nums, len(nums) // 2)
print(f"Part 2: {p2}")
assert 1274 == p2
