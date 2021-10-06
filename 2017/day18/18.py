from collections import defaultdict


with open("input.txt") as file:
    commands = file.read().splitlines()


regs = defaultdict(int)
last_played = -1
idx = 0
get_val = lambda rv: regs[rv] if rv in regs else int(rv)

while idx < len(commands):
    cmd, *data = commands[idx].split(' ')

    if cmd == "snd":
        last_played = regs[data[0]]
    elif cmd == "set":
        reg, val = data
        regs[reg] = get_val(val)
    elif cmd == "add":
        reg, val = data
        regs[reg] += get_val(val)
    elif cmd == "mul":
        reg, val = data
        regs[reg] *= get_val(val)
    elif cmd == "mod":
        reg, val = data
        regs[reg] %= get_val(val)
    elif cmd == "rcv":
        reg_or_val = data[0]
        if get_val(reg_or_val) > 0:
            break
    elif cmd == "jgz":
        reg_or_val, offset = data
        if get_val(reg_or_val) > 0:
            idx += int(offset) - 1

    idx += 1


print(f"Recovered: {last_played}")
assert 8600 == last_played

