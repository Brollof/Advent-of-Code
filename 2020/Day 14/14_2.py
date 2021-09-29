from collections import defaultdict
from itertools import product
import re


with open('input.txt') as file:
    data = file.read()


mem = defaultdict(int)
mask = ''


def apply_mask(value, mask):
    value = list(f"{value:036b}")
    for i in range(len(mask)):
        c = mask[i]
        if c in 'X1':
            value[i] = c
        elif c == '0':
            continue
    return ''.join(value)


def get_regs(value):
    x_ids = [i for i, c in enumerate(value) if c == 'X']
    vals = []
    for comb in product('01', repeat=len(x_ids)):
        temp = list(value)
        for i, v in zip(x_ids, comb):
            temp[i] = v
        vals.append(int(''.join(temp), base=2))
    return vals


for line in data.splitlines():
    if m := re.match(r'mask = (\w{36})', line):
        mask = m[1]
    elif m := re.match(r'mem\[(\d+)\] = (\d+)', line):
        idx, value = int(m[1]), int(m[2])
        regs = apply_mask(idx, mask)
        for reg in get_regs(regs):
            mem[reg] = value
    else:
        assert 0


part2 = sum(mem.values())
print(part2)


