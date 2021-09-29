class Player:
    def __init__(self, deck):
        self.deck = deck

    def play_card(self):
        return self.deck.pop(0)
    
    def take_cards(self, cards):
        self.deck.extend(sorted(cards, reverse=True))
    
    def lost(self):
        return len(self.deck) == 0


with open('input.txt') as file:
    data = file.read()


# parse data
p1_data, p2_data = data.split('\n\n')
p1 = Player([int(x) for x in p1_data.splitlines()[1:]])
p2 = Player([int(x) for x in p2_data.splitlines()[1:]])

rounds = 0


def play_round():
    global rounds
    rounds += 1
    p1_card, p2_card = p1.play_card(), p2.play_card()
    if p1_card > p2_card:
        p1.take_cards([p1_card, p2_card])
    else:
        p2.take_cards([p1_card, p2_card])


def calc_score(winner):
    return sum(m * card for m, card in enumerate(reversed(winner.deck), 1))


while not p1.lost() and not p2.lost():
    play_round()


if not p1.lost():
    score = calc_score(p1)
    print("Player 1 wins!")
else: 
    score = calc_score(p2)
    print("Player 2 wins!")
    
print(f"Rounds: {rounds}, score: {score}")