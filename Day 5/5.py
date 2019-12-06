C_ADD =  1; C_MUL =   2; C_INP =   3;
C_OUT =  4; C_JMP_T = 5; C_JMP_F = 6;
C_LESS = 7; C_EQU =   8; C_HALT =  99

cmd_len = {C_ADD: 3, C_MUL: 3, C_INP: 1, C_OUT: 1, C_JMP_T: 2, C_JMP_F: 2, C_LESS: 3, C_EQU: 3, C_HALT: 0}

def parse_instruction(intcode, index):
    modes, op = divmod(intcode[index], 100)
    modes = int(str(modes), base=2)
    vals = [intcode[index + i] if not modes & (1 << (i - 1)) else index + i for i in range(1, cmd_len[op] + 1)]
    return op, vals, cmd_len[op]


def calc(intcode, inp1):
    index, out, intcode = 0, [], list(intcode)
    while index < len(intcode):
        opcode, vals, offset = parse_instruction(intcode, index)
        if opcode == C_ADD:
            v1, v2, v3 = vals
            intcode[v3] = intcode[v1] + intcode[v2]
        elif opcode == C_MUL:
            v1, v2, v3 = vals
            intcode[v3] = intcode[v1] * intcode[v2]
        elif opcode == C_INP:
            intcode[vals[0]] = inp1
        elif opcode == C_OUT:
            out.append(intcode[vals[0]])
        elif opcode == C_JMP_T:
            v1, v2 = vals
            index = intcode[v2] if intcode[v1] else index + 3
        elif opcode == C_JMP_F:
            v1, v2 = vals
            index = intcode[v2] if intcode[v1] == 0 else index + 3
        elif opcode == C_LESS:
            v1, v2, v3 = vals
            intcode[v3] = 2 if intcode[v1] < intcode[v2] else 0
        elif opcode == C_EQU:
            v1, v2, v3 = vals
            intcode[v3] = 1 if intcode[v1] == intcode[v2] else 0
        elif opcode == C_HALT:
            return out

        if opcode not in [C_JMP_T, C_JMP_F]:
            index += offset + 1

    return out


with open("input.txt") as file:
    intcode = [int(val) for val in file.read().split(",")]

# part 1
print(calc(intcode, 1)[-1])

# part 2
print(calc(intcode, 5)[-1])
