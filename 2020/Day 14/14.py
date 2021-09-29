from collections import defaultdict
import re


with open('input.txt') as file:
    data = file.read()

# data = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
# mem[8] = 11
# mem[7] = 101
# mem[8] = 0"""


mem = defaultdict(int)
mask = ''


def apply_mask(value, mask):
    for i in range(len(mask)):
        c = mask[len(mask) - i - 1]
        if c == '0':
            value &= ~(1 << i)
        elif c == '1':
            value |= (1 << i)
    return value


for line in data.splitlines():
    if m := re.match(r'mask = (\w{36})', line):
        mask = m[1]
    elif m := re.match(r'mem\[(\d+)\] = (\d+)', line):
        idx, value = int(m[1]), int(m[2])
        mem[idx] = apply_mask(value, mask)
    else:
        assert False


part1 = sum(mem.values())
print(part1)


