import re
from itertools import combinations


class Item:
    def __init__(self, cost, damage, armor):
        self.cost = int(cost)
        self.damage = int(damage)
        self.armor = int(armor)

    def __repr__(self):
        return f"Item({self.cost},{self.damage},{self.armor})"


class Player:
    def __init__(self, hp, damage, armor):
        self.hp = hp
        self.damage = damage
        self.armor = armor

    def attack(self, other):
        other.hp -= max(1, self.damage - other.armor)

    def __repr__(self):
        return f"Player(hp:{self.hp},dmg:{self.damage},arm:{self.armor})"


def calc(name, *items):
    return sum(getattr(item, name) for item in items if item)


def play(me, boss):
    turns = 0
    while True:
        if turns % 2 == 0:
            me.attack(boss)
        else:
            boss.attack(me)

        turns += 1

        if me.hp <= 0:
            return False
        elif boss.hp <= 0:
            return True


with open("inp21.txt") as file:
    data = file.read()


boss_hp, boss_damage, boss_armor = [int(x) for x in re.findall(r"\d+", data)]

weapons = []
armor = []
rings = []

weapons_str, armor_str, rings_str = """Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3""".split("\n\n")


for container, str_ in zip((weapons, armor, rings), (weapons_str, armor_str, rings_str)):
    for line in str_.splitlines()[1:]:
        r = re.search(r".*?\s+(\d+)\s+(\d+)\s+(\d+)", line)
        container.append(Item(r[1], r[2], r[3]))


minimal_cost = float('inf')
maximum_cost = 0

for w in weapons:
    for a in armor + [[]]:
        for r1, r2 in combinations(rings + [[], []], 2):
            items = (w, a, r1, r2)
            total_cost = calc("cost", *items)
            total_damage = calc("damage", *items)
            total_armor = calc("armor", *items)

            me, boss = Player(100, total_damage, total_armor), Player(boss_hp, boss_damage, boss_armor)

            if play(me, boss): # I won
                minimal_cost = min(minimal_cost, total_cost)
            else:
                maximum_cost = max(maximum_cost, total_cost)


print(f"Part 1: {minimal_cost}")
assert 91 == minimal_cost

print(f"Part 2: {maximum_cost}")
assert 158 == maximum_cost
