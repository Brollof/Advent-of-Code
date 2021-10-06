from collections import defaultdict
import threading
import queue


class Program(threading.Thread):
    def __init__(self, raw_cmds, idd):
        super().__init__()
        self.idd = idd
        self.rcv_q = queue.Queue()
        self.send_q = None
        self.commands = [line.strip().split(' ') for line in raw_cmds.splitlines()]
        self.regs = defaultdict(int)
        self.regs['p'] = idd
        self.sent_cnt = 0

    def get_val(self, rv):
        return self.regs[rv] if rv in self.regs else int(rv)

    def run(self):
        idx = 0
        while idx < len(self.commands):
            cmd, *data = self.commands[idx]

            if cmd == "snd":
                self.send_q.put(self.regs[data[0]])
                self.sent_cnt += 1
            elif cmd == "set":
                reg, val = data
                self.regs[reg] = self.get_val(val)
            elif cmd == "add":
                reg, val = data
                self.regs[reg] += self.get_val(val)
            elif cmd == "mul":
                reg, val = data
                self.regs[reg] *= self.get_val(val)
            elif cmd == "mod":
                reg, val = data
                self.regs[reg] %= self.get_val(val)
            elif cmd == "rcv":
                reg = data[0]
                try:
                    val = self.rcv_q.get(timeout=0.2)
                except queue.Empty: # deadlock
                    print(f"Program {self.idd} ended.")
                    break
                self.regs[reg] = val
            elif cmd == "jgz":
                reg_or_val, offset = data
                if self.get_val(reg_or_val) > 0:
                    idx += self.get_val(offset) - 1

            idx += 1


with open("input.txt") as file:
    data = file.read()


p1 = Program(data, 0)
p2 = Program(data, 1)

p1.send_q = p2.rcv_q
p2.send_q = p1.rcv_q

p1.start()
p2.start()

p1.join()
p2.join()

print(f"Sent messages count: {p2.sent_cnt}")
assert 7239 == p2.sent_cnt