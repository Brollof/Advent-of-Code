import re

class TreeNode:
    def __init__(self, name, w):
        self.name = name
        self.w = w
        self.parent = None
        self.children = []
        self.level = None

    def add_child(self, child):
        self.children.append(child)

    def __repr__(self):
        return f"N({self.name},{self.w})"

    def print(self):
        print(f"Name: {self.name}, parent: {self.parent if self.parent else '-'}, children: {self.children}")

    def print_tree(self):
        level = self.get_level()
        print(f"{'   ' * level}|__{self.name}, {self.calc_weight()}")
        for child in self.children:
            child.print_tree()

    def get_level(self):
        if self.level is None:
            level = 0
            p = self.parent
            while p:
                level += 1
                p = p.parent
            self.level = level
        return self.level

    def calc_weight(self):
        w = self.w
        for child in self.children:
            w += child.calc_weight()
        return w


def find_root(nodes):
    for node in nodes.values():
        if node.get_level() == 0:
            return node
    raise Exception("No root? WTF?")


with open('input.txt') as file:
    data = file.read()

nodes = dict()

# create nodes without parents and children
for line in data.splitlines():
    d = line.split("->")
    m = re.match(r"(\w+) \((\d+)\)", d[0])
    name = m[1]
    weight = int(m[2])
    node = TreeNode(name, weight)
    nodes[name] = node


# fill parents and children
for line in data.splitlines():
    d = line.split("->")
    m = re.match(r"(\w+) \((\d+)\)", d[0])
    name = m[1]
    weight = int(m[2])
    if len(d) > 1:
        children = re.findall(r"\w+", d[1])
        node = nodes[name]
        for child in children:
            c = nodes[child]
            c.parent = node
            node.add_child(c)

root = find_root(nodes)
root.print_tree()
print(f"Part1: {root}")


n = nodes['ptshtrn']

# part 2, 521
print(n.w - (1122 - 1117))
assert n.w - (1122 - 1117) == 521

