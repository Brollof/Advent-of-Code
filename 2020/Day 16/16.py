import re

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

    def __repr__(self):
        return f"R({self.name}:[{self.r1}{self.r2}])"


with open('input.txt') as file:
    data = file.read()


# data = """class: 1-3 or 5-7
# row: 6-11 or 33-44
# seat: 13-40 or 45-50

# your ticket:
# 7,1,14

# nearby tickets:
# 7,3,47
# 40,4,50
# 55,2,20
# 38,6,12"""


rules = []

rules_str, my_ticket, tickets = data.split('\n\n')

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
tickets = tickets.splitlines()
discarded = 0
for line in tickets[1:]:
    vals = [int(v) for v in line.split(',')]
    to_d = False
    for v in vals:
        valid = False
        for rule in rules:
            if rule.in_range(v):
                valid = True
                break
        if not valid:
            to_d = True
            error_rate += v
    if to_d:
        discarded += 1

print(error_rate, discarded)
