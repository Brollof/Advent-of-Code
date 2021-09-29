DEBUG = 0
def dprint(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)


class Player:
    def __init__(self, deck):
        self.decks = [deck]
        self.di = 0

    @property
    def cards_count(self):
        return len(self.decks[self.di])

    @property
    def deck(self):
        return self.decks[self.di]
        
    def play_card(self):
        return self.decks[self.di].pop(0)
    
    def take_cards(self, cards):
        self.decks[self.di].extend(cards)
    
    def lost(self):
        return len(self.decks[self.di]) == 0
    
    def copy_deck(self, n):
        self.di += 1
        self.decks.append(self.decks[-1][:n])

    def flush(self):
        del self.decks[-1]
        self.di -= 1


class History:
    def __init__(self):
        self.data = {}


with open('input.txt') as file:
    data = file.read()

# data = """Player 1:
# 9
# 2
# 6
# 3
# 1

# Player 2:
# 5
# 8
# 4
# 7
# 10"""

# data = """Player 1:
# 43
# 19

# Player 2:
# 2
# 29
# 14"""

# parse data
p1_data, p2_data = data.split('\n\n')
p1 = Player([int(x) for x in p1_data.splitlines()[1:]])
p2 = Player([int(x) for x in p2_data.splitlines()[1:]])

grounds = 0
p1_prev = None
p2_prev = None

def calc_score(deck):
    return sum(m * card for m, card in enumerate(reversed(deck), 1))

history = {}
def check_if_prev_was_the_same(current_game):
    p1_current_deck = p1.deck.copy()
    p2_current_deck = p2.deck.copy()

    if current_game in history:
        for deck in history[current_game][1]:
            if deck == p1_current_deck:
                return True

        for deck in history[current_game][2]:
            if deck == p2_current_deck:
                return True
    else:
        history[current_game] = {1: [], 2: []}
    history[current_game][1].append(p1_current_deck)
    history[current_game][2].append(p2_current_deck)

    return False


def play_round(rounds, game):
    # normal draw
    p1_card, p2_card = p1.play_card(), p2.play_card()
    dprint(f"Player 1 plays: {p1_card}")
    dprint(f"Player 2 plays: {p2_card}")

    # check condition for starting sub-game
    if p1.cards_count >= p1_card and p2.cards_count >= p2_card:
        dprint("Playing a sub-game to determine the winner...\n")
        p1.copy_deck(p1_card)
        p2.copy_deck(p2_card)
        winner = play_game()
        p1.flush()
        p2.flush()
        if winner == 1:
            # dprint(f"(r) Player 1 wins round {rounds} of game {game}!")
            p1.take_cards([p1_card, p2_card])
        else:
            # dprint(f"(r) Player 2 wins round {rounds} of game {game}!")
            p2.take_cards([p2_card, p1_card])

    else: # normal game
        if p1_card > p2_card:
            dprint(f"Player 1 wins round {rounds} of game {game}!")
            p1.take_cards([p1_card, p2_card])
        else:
            dprint(f"Player 2 wins round {rounds} of game {game}!")
            p2.take_cards([p2_card, p1_card])

total_games = 0
def play_game():
    global grounds, total_games
    total_games += 1
    game = total_games
    rounds = 0

    dprint(f"=== Game {game} ===")
    while True:
        rounds += 1
        grounds += 1
        dprint(f"-- Round {rounds} (Game {game}) --")
        dprint(f"Player 1's deck: {', '.join(map(str, p1.deck))}")
        dprint(f"Player 2's deck: {', '.join(map(str, p2.deck))}")

        # check recursive end
        if check_if_prev_was_the_same(game):
            game -= 1
            return 1
        
        play_round(rounds, game)
        if p1.lost():
            dprint(f"The winner of game {game} is player 2!")
            game -= 1
            return 2
        if p2.lost():
            dprint(f"The winner of game {game} is player 1!")
            game -= 1
            return 1



winner = play_game()
if winner == 1:
    score = calc_score(p1.deck)
else:
    score = calc_score(p1.deck)
    
print(f"Winner: player {winner}, score: {score}")