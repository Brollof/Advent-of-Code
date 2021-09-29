import re
from collections import defaultdict

class Rule:
    def __init__(self, name, r1, r2):
        self.name = name
        self.r1 = range(r1[0], r1[1] + 1)
        self.r2 = range(r2[0], r2[1] + 1)

    def in_range(self, value):
        if value in self.r1 or value in self.r2:
            return True
        return False

    def any_in_range(self, lst):
        return any(self.in_range(v) for v in lst)

    def all_in_range(self, lst):
        return all(self.in_range(v) for v in lst)

    def __repr__(self):
        return f"R({self.name}:[{self.r1}{self.r2}])"


with open('input.txt') as file:
    data = file.read()


# data = """class: 0-1 or 4-19
# row: 0-5 or 8-19
# seat: 0-13 or 16-19

# your ticket:
# 11,12,13

# nearby tickets:
# 3,9,18
# 15,1,5
# 5,14,9"""


rules = []

rules_str, my_ticket_str, tickets_str = data.split('\n\n')

for line in rules_str.splitlines():
    if m := re.match(r'(.*): (\d+)-(\d+) or (\d+)-(\d+)', line):
        name = m[1]
        r1_b, r1_e = int(m[2]), int(m[3])
        r2_b, r2_e = int(m[4]), int(m[5])
        rule = Rule(name, (r1_b, r1_e), (r2_b, r2_e))
        rules.append(rule)
    else:
        assert False, f"O KURWA: {line}"


error_rate = 0
discarded = 0
tickets_str = tickets_str.splitlines()
tickets = []

# filter tickets
for line in tickets_str[1:]:
    vals = [int(v) for v in line.split(',')]
    if all(any(rule.in_range(v) for rule in rules) for v in vals):
        tickets.append(vals)
    else:
        discarded += 1

# guess
idx = 0
possibilities = defaultdict(lambda: [r.name for r in rules])
b = 1000
rem = 0
while True:
    removed = False
    # b -= 1
    # if not b: break
    tidx = [ticket[idx] for ticket in tickets]
    # print(tidx, len(tickets[0]))
    for rule in rules:
        if not rule.all_in_range(tidx):
            if rule.name in possibilities[idx]:
                rem += 1
                removed = True
                possibilities[idx].remove(rule.name)

    idx = (idx + 1) % len(tickets[0])
    if not removed and idx == 0:
        break

# print(possibilities)
print(rem)
# for pos in possibilities.values():
#     print(len(pos))

idx = 0
b = 10000
removed = 0
while True:
    b -= 1
    if not b: break
    if len(possibilities[idx]) == 1:
        to_remove = possibilities[idx][0]
        # print(to_remove)
        for pos in possibilities.values():
            if to_remove in pos and len(pos) > 1:
                removed += 1
                pos.remove(to_remove)
        # break

    idx = (idx + 1) % len(tickets[0])

print(possibilities)
print(removed)


my_ticket = [int(v) for v in my_ticket_str.splitlines()[1].split(',')]
result = 1
for idx, pos in possibilities.items():
    name = pos[0]
    if 'departure' in name:
        result *= my_ticket[idx]
print(result)