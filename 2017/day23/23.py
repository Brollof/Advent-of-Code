from collections import defaultdict
import math


class Program:
    def __init__(self, raw_cmds, debug=0):
        self.commands = [line.strip().split(' ') for line in raw_cmds.splitlines()]
        self.regs = defaultdict(int)
        self.regs['a'] = debug
        self.mul_cnt = 0

    def get_val(self, rv):
        return self.regs[rv] if rv.isalpha() else int(rv)

    def print_regs(self):
        print("Registers:")
        for i in range(ord('a'), ord('h') + 1):
            reg = chr(i)
            print(f"{reg}: {self.regs[reg]}")

    def run(self):
        idx = 0
        
        while idx < len(self.commands):
            cmd, *data = self.commands[idx]
            reg, val = data

            if cmd == "set":
                self.regs[reg] = self.get_val(val)
            elif cmd == "sub":
                self.regs[reg] -= self.get_val(val)
            elif cmd == "mul":
                self.mul_cnt += 1
                self.regs[reg] *= self.get_val(val)
            elif cmd == "jnz":
                if self.get_val(reg) != 0:
                    idx += self.get_val(val) - 1

            idx += 1


with open("input.txt") as file:
    data = file.read()


p1 = Program(data)
p1.run()

print(f"Part 1: {p1.mul_cnt}")
assert 6241 == p1.mul_cnt



def is_prime(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


cnt = sum(1 for x in range(108100, 125100 + 1,17) if not is_prime(x))
print(f"Part 2: {cnt}")
assert 909 == cnt