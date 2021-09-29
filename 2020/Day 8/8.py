import re

with open('input.txt') as file:
    CMDS = []
    for line in file:
        cmd, v = line.strip().split(' ')
        CMDS.append((cmd, int(v)))

def go(cmds):
    visited = []
    acc = 0
    index = 0

    while True:
        if index in visited:
            return acc
        visited.append(index)
        try:
            cmd, v = cmds[index]
        except IndexError:
            print(f"Index out of range. Index: {index}, list length: {len(cmds)}, acc: {acc}")
            raise
        if cmd == 'acc':
            acc += v
        elif cmd == 'jmp':
            index += v - 1

        index += 1

v = go(CMDS)
print(v)

def brute_force():
    i = -1
    while True:
        ccc = CMDS.copy()

        # change one command
        while True:
            i += 1
            cmd, v = ccc[i]
            if cmd == 'nop':
                ccc[i] = ('jmp', v)
                break
            elif cmd == 'jmp':
                ccc[i] = ('nop', v)
                break

        go(ccc)

brute_force()