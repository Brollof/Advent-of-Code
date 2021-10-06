with open('input.txt') as file:
    data = file.readlines()

regs = dict()

# determine register names
for line in data:
    name = line.split(' ')[0]    
    regs[name] = 0

def is_true(regs, regif, op, valif):
    val = regs[regif]
    valif = int(valif)
    if op == '==': return val == valif
    if op == '!=': return val != valif
    if op == '<':  return val < valif
    if op == '<=': return val <= valif
    if op == '>':  return val > valif
    if op == '>=': return val >= valif
    assert False

# execute instructions
best_ever = 0
for line in data:
    reg, cmd, val, _, regif, op, valif = line.split(' ')
    if is_true(regs, regif, op, valif):
        if cmd == 'inc':
            regs[reg] += int(val)
        elif cmd == 'dec':
            regs[reg] -= int(val)
        else:
            assert False
        best_ever = max(regs[reg], best_ever)

best = 0
for v in regs.values():
    best = max(v, best)

print("Part 1:", best)
assert 3745 == best

print("Part 2:", best_ever)
assert 4644 == best_ever

