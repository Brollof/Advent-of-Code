from collections import defaultdict

with open("inp3.txt") as file:
    data = file.read()


BIT_LEN = data.find('\n')
bits = defaultdict(lambda: {0: 0, 1: 0})
numbers = data.splitlines()

for num in numbers:
    for i, c in enumerate(num):
        bits[i][int(c)] += 1

gamma = 0
for bit, data in bits.items():
    if data[1] > data[0]:
        gamma |= 1 << (BIT_LEN - bit - 1)

epsilon = ~gamma & int('1' * BIT_LEN, 2)

p1 = epsilon * gamma
print(f"Part 1: {p1}")
assert 4160394 == p1

####################################################################################
####################################################################################

def filter_nums(nums, func, bit=0):
    if len(nums) == 1:
        return int(nums[0], 2)
    cnt0 = sum(1 for num in nums if num[bit] == '0')
    cnt1 = len(nums) - cnt0
    return filter_nums([num for num in nums if num[bit] == func(cnt0, cnt1)], func, bit + 1)

oxygen_generator_rating = filter_nums(numbers, lambda cnt0, cnt1: '1' if cnt1 >= cnt0 else '0')
co2_scrubber_rating     = filter_nums(numbers, lambda cnt0, cnt1: '0' if cnt0 <= cnt1 else '1')
p2 = oxygen_generator_rating * co2_scrubber_rating
print(f"Part 2: {p2}")
assert 4125600 == p2
