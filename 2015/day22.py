import re


COST = {"missle": 53, "drain": 73, "shield": 113, "poison": 173, "recharge": 229}
ALL_SPELLS = set(COST.keys())


class Effect:
    def __init__(self, name):
        self.name = name
        self.duration = 0

    def apply(self, target):
        if self.name == "shield":
            self.duration = 6
            target.armor += 7
        elif self.name == "poison":
            self.duration = 6
        elif self.name == "recharge":
            self.duration = 5

    def update(self, target):
        self.duration -= 1
        if self.name == "shield":
            pass
        elif self.name == "poison":
            target.hp -= 3
        elif self.name == "recharge":
            target.mana += 101

    def end(self, target):
        if self.name == "shield":
            target.armor -= 7
        elif self.name == "poison":
            pass
        elif self.name == "recharge":
            pass


class Player:
    def __init__(self, name, hp=0, mana=0, damage=0):
        self.name = name
        self.hp = hp
        self.mana = mana
        self.damage = damage
        self.effects = []
        self.armor = 0
        self.mana_spent = 0

    def attack(self, other, spell=None):
        self.mana -= COST.get(spell, 0)
        self.mana_spent += COST.get(spell, 0)

        if spell == "missle":
            other.hp -= 4
        elif spell == "drain":
            other.hp -= 2
            self.hp += 2
        elif spell == "shield":
            self.effects.append(Effect("shield"))
            self.effects[-1].apply(self)
        elif spell == "poison":
            other.effects.append(Effect("poison"))
            other.effects[-1].apply(self)
        elif spell == "recharge":
            self.effects.append(Effect("recharge"))
            self.effects[-1].apply(self)
        elif spell is None:
            other.hp -= max(1, self.damage - other.armor)
        else:
            raise Exception(f"unknown spell: {spell}")

        assert self.mana >= 0

    def info(self):
        return f"- {self.name} has {self.hp} hit points, {self.armor} armor, {self.mana} mana"


class Game:
    def __init__(self, me, boss):
        self.me = me
        self.boss = boss
        self.turns = 0
        self.winner = None

    def play(self, spell, part):
        spells = [spell, '']

        while spells:

            if self.turns % 2 == 0:
                if spells[0] == '':
                    break

            # part 2
            if part == 2 and self.turns % 2 == 0: # player turn
                self.me.hp -= 1
                if self.me.hp <= 0:
                    self.winner = "Boss"
                    return True

            # update effects
            for i in reversed(range(len(self.me.effects))):
                self.me.effects[i].update(self.me)
                if self.me.effects[i].duration == 0:
                    self.me.effects[i].end(self.me)
                    del self.me.effects[i]

            for i in reversed(range(len(self.boss.effects))):
                self.boss.effects[i].update(self.boss)
                if self.boss.effects[i].duration == 0:
                    self.boss.effects[i].end(self.boss)
                    del self.boss.effects[i]

            # check end game
            if self.me.hp <= 0 or self.boss.hp <= 0:
                self.winner = 'Player' if self.boss.hp <= 0 else 'Boss'
                return True

            # action
            if self.turns % 2 == 0:
                spell = spells.pop(0)
                self.me.attack(self.boss, spell)
            else:
                self.boss.attack(self.me)

            self.turns += 1
        return False


def copy_game(game):
    me_effects = []
    for e in game.me.effects:
        new_e = Effect(e.name)
        new_e.duration = e.duration
        me_effects.append(new_e)

    boss_effects = []
    for e in game.boss.effects:
        new_e = Effect(e.name)
        new_e.duration = e.duration
        boss_effects.append(new_e)

    new_me = Player("Player")
    new_me.name = game.me.name
    new_me.hp = game.me.hp
    new_me.mana = game.me.mana
    new_me.damage = game.me.damage
    new_me.effects = me_effects
    new_me.armor = game.me.armor
    new_me.mana_spent = game.me.mana_spent

    new_boss = Player("Boss")
    new_boss.name = game.boss.name
    new_boss.hp = game.boss.hp
    new_boss.mana = game.boss.mana
    new_boss.damage = game.boss.damage
    new_boss.effects = boss_effects
    new_boss.armor = game.boss.armor
    new_boss.mana_spent = game.boss.mana_spent

    new_game = Game(None, None)
    new_game.me = new_me
    new_game.boss = new_boss
    new_game.turns = game.turns
    new_game.winner = game.winner
    return new_game


def get_valid_spells(game):
    active_spells = {e.name for e in game.me.effects if e.duration > 1} | {e.name for e in game.boss.effects if e.duration > 1}
    possible_spells = ALL_SPELLS - active_spells
    return {s for s in possible_spells if game.me.mana >= COST[s]}


# works only for part 1
def go_recursive(game, spell=''):
    global min_mana

    if game.me.mana_spent >= min_mana:
        return

    if spell:
        if game.play(spell, 1) == True:
            if game.winner == 'Player':
                min_mana = min(min_mana, game.me.mana_spent)
            return

    # execute spells
    for s in get_valid_spells(game):
        go_recursive(copy_game(game), s)


def go_iter(g, spell='', part=1):
    global min_mana

    games = [(copy_game(g), spell) for spell in get_valid_spells(g)]

    while games:
        game, spell = games.pop()
        if game.play(spell, part) == True:
            if game.winner == 'Player':
                min_mana = min(min_mana, game.me.mana_spent)
        else:
            if game.me.mana_spent >= min_mana:
                continue
            games.extend((copy_game(game), spell) for spell in get_valid_spells(game))


with open("inp22.txt") as file:
    data = file.read()


boss_hp, boss_damage = [int(x) for x in re.findall(r"\d+", data)]

me, boss = Player("Player", hp=50, mana=500, damage=0), Player("Boss", hp=boss_hp, mana=0, damage=boss_damage)
game = Game(me, boss)


min_mana = float('inf')
go_iter(copy_game(game), part=1)
assert 1824 == min_mana
print(f"Part 1: {min_mana}")


min_mana = float('inf')
go_iter(game, part=2)
print(f"Part 2: {min_mana}")
assert 1937 == min_mana
