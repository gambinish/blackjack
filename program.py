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


class Hand(Deck):

    def __init__(self, name):
        Deck.__init__(self)
        self.name = name
        self.cards = []
        self.value = 0
        self.preview = 0
        self.aces = 0

    def add_card(self):
        self.value = 0
        self.cards.append(self.deck[0])
        self.deck = self.deck[1::]
        for card in self.cards:
            self.value = self.value + card['value']
        return self.cards

    def deal_hand(self):
        random.shuffle(self.deck)
        self.cards = self.deck[0:2]
        self.preview = self.cards[0]['value']
        for card in self.cards:
            self.value = self.value + card['value']
        return self.cards

    def preview_hand(self):
        print(f'{self.name} hand: '.upper())
        print(str(self.cards[0]['rank'] + ' of ' + self.cards[0]['suit']))
        print(str('Dealer Preview: ' + str(self.cards[0]['value'])))
        return ''

    def __call__(self):
        return self.cards

    def __str__(self):
        print(f'{self.name} hand: '.upper())
        for card in self.cards:
            print(str(card['rank'] + ' of ' + card['suit']))
        print(str('Current Value: ' + str(self.value)))
        return ''


# deal hands
# player_hand = Hand('player')
# dealer_hand = Hand('dealer')

def show_table_preview():
    print('****************')
    print(player_hand)
    print(dealer_hand.preview_hand())
    print('****************')


def show_table_full():
    print('****************')
    print(player_hand)
    print(dealer_hand)
    print('****************')


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
        playing = True
        # deal hands
        player_hand = Hand('player')
        dealer_hand = Hand('dealer')
        print('lets play!\n')
        player_hand.deal_hand()
        dealer_hand.deal_hand()
        show_table_preview()
        while (player_hand.value < 22):
            if (playing):
                print('PLAYER TURN')
                player_ask = ''
                player_ask = str(input(f'Hit or Stay?'))
                # hit, handle player
                if (player_ask.lower()[0] == 'h'):
                    player_hand.add_card()
                    show_table_preview()
                    continue
                # stay, handle dealer
                else:
                    # dealer wins
                    while (dealer_hand.value < player_hand.value):
                        show_table_full()
                        dealer_hand.add_card()
                        if (dealer_hand.value < player_hand.value):
                            show_table_full()
                            continue
                        elif (dealer_hand.value > 21):
                            show_table_full()
                            print('DEALER BUST! PLAYER WINS!')
                            playing = False
                            break
                        else:
                            show_table_full()
                            print('DEALER WINS!')
                            playing = False
                            break
            else:
                break
        else:
            show_table_preview()
            print('PLAYER BUST! DEALER WINS')
            # replay()
            continue
    else:
        print('enter "y" to begin playing')
        break
