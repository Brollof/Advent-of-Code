C_ADD  = 1; C_MUL   = 2; C_INP   = 3;
C_OUT  = 4; C_JMP_T = 5; C_JMP_F = 6;
C_LESS = 7; C_EQU   = 8; C_HALT  = 99
C_REL  = 9

M_POS = 0; M_IMM = 1; M_REL = 2

cmd_len = {C_ADD: 3, C_MUL: 3, C_INP: 1, C_OUT: 1, C_JMP_T: 2, C_JMP_F: 2, C_LESS: 3, C_EQU: 3, C_HALT: 0, C_REL: 1}


class Memory(list):
  def __setitem__(self, index, value):
    if index >= len(self):
        self += [0] * (index - len(self) + 1)
    super().__setitem__(index, value)


def parse_instruction(intcode, index, rel_index):
    vals = []
    modes, op = divmod(intcode[index], 100)
    for i in range(1, cmd_len[op] + 1):
        modes, m = divmod(modes, 10)
        if m == M_POS:
            vals.append(intcode[index + i])
        elif m == M_IMM:
            vals.append(index + i)
        elif m == M_REL:
            vals.append(rel_index + intcode[index + i])

    return op, vals, cmd_len[op]


def calc(intcode, inp):
    index = rel_index = 0
    intcode = Memory(intcode)
    while index < len(intcode):
        opcode, vals, offset = parse_instruction(intcode, index, rel_index)
        if opcode == C_ADD:
            v1, v2, v3 = vals
            intcode[v3] = intcode[v1] + intcode[v2]
        elif opcode == C_MUL:
            v1, v2, v3 = vals
            intcode[v3] = intcode[v1] * intcode[v2]
        elif opcode == C_INP:
            intcode[vals[0]] = inp
        elif opcode == C_OUT:
            return intcode[vals[0]]
        elif opcode == C_JMP_T:
            v1, v2 = vals
            index = intcode[v2] if intcode[v1] != 0 else index + 3
        elif opcode == C_JMP_F:
            v1, v2 = vals
            index = intcode[v2] if intcode[v1] == 0 else index + 3
        elif opcode == C_LESS:
            v1, v2, v3 = vals
            intcode[v3] = int(intcode[v1] < intcode[v2])
        elif opcode == C_EQU:
            v1, v2, v3 = vals
            intcode[v3] = int(intcode[v1] == intcode[v2])
        elif opcode == C_REL:
            rel_index += intcode[vals[0]]
        elif opcode == C_HALT:
            return out

        if opcode not in [C_JMP_T, C_JMP_F]:
            index += offset + 1

    return out


with open("input.txt") as file:
    intcode = [int(v) for v in file.read().split(",")]


# part 1
print(calc(intcode, 1))

# part 2
print(calc(intcode, 2))