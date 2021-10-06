from collections import defaultdict


LEFT = -1
RIGHT = 1


class Action:
    def __init__(self, write, move, next_state):
        self.write = write
        self.move = move
        self.next_state = next_state


STATES = {
    "A": [Action(1, RIGHT, 'B'), Action(1, LEFT, 'E')],
    "B": [Action(1, RIGHT, 'C'), Action(1, RIGHT, 'F')],
    "C": [Action(1, LEFT, 'D'), Action(0, RIGHT, 'B')],
    "D": [Action(1, RIGHT, 'E'), Action(0, LEFT, 'C')],
    "E": [Action(1, LEFT, 'A'), Action(0, RIGHT, 'D')],
    "F": [Action(1, RIGHT, 'A'), Action(1, RIGHT, 'C')]
}

current_state = "A"
steps = 12459852
tape = defaultdict(int)
cursor = 0

for _ in range(steps):
    val = tape[cursor]
    tape[cursor] = STATES[current_state][val].write
    cursor += STATES[current_state][val].move
    current_state = STATES[current_state][val].next_state


p1 = list(tape.values()).count(1)
print(f"Part 1: {p1}")
assert 4217 == p1
