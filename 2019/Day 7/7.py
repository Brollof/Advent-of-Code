from itertools import permutations, cycle

C_ADD =  1; C_MUL =   2; C_INP =   3;
C_OUT =  4; C_JMP_T = 5; C_JMP_F = 6;
C_LESS = 7; C_EQU =   8; C_HALT =  99

cmd_len = {C_ADD: 3, C_MUL: 3, C_INP: 1, C_OUT: 1, C_JMP_T: 2, C_JMP_F: 2, C_LESS: 3, C_EQU: 3, C_HALT: 0}


def parse_instruction(intcode, index):
    modes, op = divmod(intcode[index], 100)
    modes = int(str(modes), base=2)
    vals = [intcode[index + i + 1] if not modes & (1 << i) else index + i + 1 for i in range(cmd_len[op])]
    return op, vals, cmd_len[op]


class Amp:
    def __init__(self, memory, phase):
        self.index = 0
        self.mem = memory[:]
        self.phase = phase
        self.init = False

    def calc(self, inp):
        while self.index < len(self.mem):
            opcode, vals, offset = parse_instruction(self.mem, self.index)
            if opcode == C_ADD:
                v1, v2, v3 = vals
                self.mem[v3] = self.mem[v1] + self.mem[v2]
            elif opcode == C_MUL:
                v1, v2, v3 = vals
                self.mem[v3] = self.mem[v1] * self.mem[v2]
            elif opcode == C_INP:
                self.mem[vals[0]] = inp if self.init else self.phase
                self.init = True
            elif opcode == C_OUT:
                self.index += 2
                return self.mem[vals[0]]
            elif opcode == C_JMP_T:
                v1, v2 = vals
                self.index = self.mem[v2] if self.mem[v1] != 0 else self.index + 3
            elif opcode == C_JMP_F:
                v1, v2 = vals
                self.index = self.mem[v2] if self.mem[v1] == 0 else self.index + 3
            elif opcode == C_LESS:
                v1, v2, v3 = vals
                self.mem[v3] = int(self.mem[v1] < self.mem[v2])
            elif opcode == C_EQU:
                v1, v2, v3 = vals
                self.mem[v3] = int(self.mem[v1] == self.mem[v2])
            elif opcode == C_HALT:
                return None

            if opcode not in [C_JMP_T, C_JMP_F]:
                self.index += offset + 1


def part1(intcode):
    max_out = 0
    for phases in permutations(range(5)):
        out = 0
        for phase in phases:
            out = Amp(intcode, phase).calc(out)
        max_out = max(max_out, out)
    return max_out


def part2(intcode):
    max_out = 0
    for p1, p2, p3, p4, p5 in permutations(range(5, 10)):
        amps = [Amp(intcode, p1), Amp(intcode, p2), Amp(intcode, p3), Amp(intcode, p4), Amp(intcode, p5)]
        out = last = 0
        for amp in cycle(amps):
            out = amp.calc(out)
            if not out:
                max_out = max(max_out, last)
                break
            last = out
    return max_out


with open("input.txt") as file:
    intcode = [int(val) for val in file.read().split(",")]


print(part1(intcode))
print(part2(intcode))