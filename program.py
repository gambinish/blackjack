import random
suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
ranks = [
    {'name': 'Two', 'value': 2},
    {'name': 'Three', 'value': 3},
    {'name': 'Four', 'value': 4},
    {'name': 'Five', 'value': 5},
    {'name': 'Six', 'value': 6},
    {'name': 'Seven', 'value': 7},
    {'name': 'Eight', 'value': 8},
    {'name': 'Nine', 'value': 9},
    {'name': 'Ten', 'value': 10},
    {'name': 'Jack', 'value': 10},
    {'name': 'Queen', 'value': 10},
    {'name': 'King', 'value': 10},
    {'name': 'Ace', 'value': 11}
]

playing = True


class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                card = {}
                card['rank'] = rank['name']
                card['value'] = int(rank['value'])
                card['suit'] = suit
                self.deck.append(card)

    def shuffle(self):
        random.shuffle(self.deck)
        return self.deck

    def deal(self):
        pass

    def __call__(self):
        return self.deck

    def __len__(self):
        return len(self.deck)


testDeck = Deck()
# print(len(testDeck))
# print(testDeck())
# print(testDeck.shuffle())


class Hand(Deck):

    def __init__(self, value=0):
        Deck.__init__(self)
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self):
        self.cards.append(self.deck[0])
        self.deck = self.deck[1::]
        for card in self.cards:
            self.value = self.value + card['value']
        return self.cards
        # print(self.deck)

    def deal_hand(self):
        random.shuffle(self.deck)
        self.cards = self.deck[0:2]
        for card in self.cards:
            self.value = self.value + card['value']
        return self.cards

    def __call__(self):
        return (self.cards, self.value)


player_hand = Hand()


class Chips:

    def __init__(self):
        self.total = 100
        self.bet = 0

    def make_bet(self):
        if (self.bet <= self.total):
            self.total = self.total - self.bet


while True:

    play_game = str(input(f'Would you like to play?, enter "y" or "n"'))
    if play_game.lower()[0] == 'y':
        print('lets play!\n')
        print('your hand is:\n')
        print(player_hand.deal_hand())
        print(player_hand.value)
        while (player_hand.value < 21):
            print(f'Your current value is {player_hand.value} \n')
            dealer_ask = str(input(f'Would you like a hit?'))
            if (dealer_ask.lower()[0] == 'y'):
                print('HIT ME')
                player_hand.add_card()
                continue
            else:
                print('DEALER TURN NOW')
                break
        else:
            print('BUST!')
            break
    else:
        print('enter valid input')
        continue
