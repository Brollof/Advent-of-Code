with open("inp23.txt") as file:
    data = file.read()


instructions = []


for line in data.splitlines():
    if "jio" in line or "jie" in line:
        rest, offset = line.split(", ")
        cmd, reg = rest.split(" ")
        instructions.append((cmd, reg, offset))
    else:
        cmd, x = line.split(" ")
        instructions.append((cmd, x))


def run(regs, instructions):
    idx = 0
    while idx < len(instructions):
        cmd, *rest = instructions[idx]
        if cmd == "inc":
            regs[rest[0]] += 1
        elif cmd == "hlf":
            regs[rest[0]] //= 2
        elif cmd == "tpl":
            regs[rest[0]] *= 3
        elif cmd == "jmp":
            idx += int(rest[0])
            idx -= 1
        elif cmd == "jie":
            reg, offset = rest
            if regs[reg] % 2 == 0:
                idx += int(offset)
                idx -= 1
        elif cmd == "jio":
            reg, offset = rest
            if regs[reg] == 1:
                idx += int(offset)
                idx -= 1

        idx += 1
    return regs


p1 = run({"a": 0, "b": 0}, instructions)["b"]
print(f"Part 1: {p1}")
assert 255 == p1

p2 = run({"a": 1, "b": 0}, instructions)["b"]
print(f"Part 1: {p2}")
assert 334 == p2
