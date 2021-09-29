class Node:
    def __init__(self, v=None):
        self.v = v
        self.next = None

def build_cups(n):
    global cups, CUP_MAP
    CUP_MAP = {}
    ns = [int(c) for c in str(n)]
    node = Node(ns.pop(0))
    root = node
    CUP_MAP[root.v] = root
    for i in range(len(ns)):
        node.next = Node(ns[i])
        node = node.next
        CUP_MAP[node.v] = node
    node.next = root
    cups = root


inp = 792845136
# training data
inp = 389125467

CUP_MAP = None
cups = None
build_cups(inp)

min_cup_v, max_cup_v = min(CUP_MAP), max(CUP_MAP)
current = cups
dest_v = None
picked_v = []


def get_cups_str():
    global cups
    first = cups.v
    vals = [first]
    while cups.next.v != first:
        vals.append(cups.next.v)
        cups = cups.next
    cups = cups.next
    return ' '.join(map(str, vals))


def pick_up():
    picked_v.append(current.next.v)
    picked_v.append(current.next.next.v)
    picked_v.append(current.next.next.next.v)
    current.next = current.next.next.next.next

def select_destination():
    global min_cup_v, max_cup_v, dest_v
    dest_v = current.v
    while True:
        dest_v -= 1
        if dest_v < min_cup_v:
            dest_v = max_cup_v
        if dest_v not in picked_v:
            break 
    print(f"Dest: {dest_v}")


def place_cups():
    global picked_v
    # print(dest_v, picked_v)

    n1 = CUP_MAP[picked_v[0]]
    n3 = CUP_MAP[picked_v[2]]
    dest = CUP_MAP[dest_v]
    # print(f"dest next: {dest.next.v}")
    n3.next = dest.next
    dest.next = n1
    # print(dest.v, dest.next.v, dest.next.next.v, dest.next.next.next.v, dest.next.next.next.next.v)
    # print(get_cups_str())
    picked_v = []

def new_current():
    global current
    current = current.next

def get_answer():
    cur = CUP_MAP[1]
    vals = []
    while cur.next.v != 1:
        vals.append(cur.next.v)
        cur = cur.next
    return ''.join(map(str, vals))

for i in range(100):
    print(f"Cups: {get_cups_str()}, current: {current.v}")
    pick_up()
    print(f"Picked: {picked_v}")
    select_destination()
    place_cups()
    new_current()
    print("=" * 20)

part1 = get_answer()
print(f"Part 1: {part1}")
