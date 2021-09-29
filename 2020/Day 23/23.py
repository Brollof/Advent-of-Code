from collections import deque

inp = 792845136
# training data
inp = 389125467


cups = deque(map(int, list(str(inp))))
min_cup, max_cup = min(cups), max(cups)
current = cups[0]

picked = []

def pick_up():
    cups.rotate(-1)
    picked.append(cups.popleft())
    picked.append(cups.popleft())
    picked.append(cups.popleft())
    cups.rotate(1)

def select_destination():
    global min_cup, max_cup
    dest = cups[0]
    while True:
        dest -= 1
        if dest < min_cup:
            dest = max_cup
        if dest in cups:
            break 
    print(f"Dest: {dest}")
    cups.rotate(-cups.index(dest))

def place_cups():
    cups.insert(1, picked.pop(0))
    cups.insert(2, picked.pop(0))
    cups.insert(3, picked.pop(0))

def new_current():
    global current
    cups.rotate(-cups.index(current) - 1)
    current = cups[0]

def get_answer():
    cups.rotate(-cups.index(1))
    return ''.join(map(str, list(cups)[1:]))

for i in range(100):
    print(f"Cups: {cups}, current: {current}")
    pick_up()
    print(f"Picked: {picked}")
    select_destination()
    place_cups()
    new_current()
    print("=" * 20)

part1 = get_answer()
print(f"Part 1: {part1}")


