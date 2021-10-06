from collections import deque

with open("input.txt") as file:
    step = int(file.read().strip())


def calc():
    buf = deque([0])
    for n in range(1, 2017 + 1):
        buf.rotate(-step)
        buf.append(n)

    return buf[0]


p2 = calc()
print(p2)

