
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}

# card class to show suit and rank


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of '+self.suit


class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n '+card.__str__()
        return 'The deck has:' + deck_comp

    def shuffle(self):  # shuffles the deck
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()  # gets one card from deck using pop method
        print(single_card)
        return single_card


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        # print(card.rank)
        self.value += values[card.rank] #adds up value of cards when player adds to holding cards array above
        if card.rank == 'Ace':
            self.aces+=1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces: #if value exceeds 21 and there are aces in hand, then reduce total value by 10 (1to11) and reduce ace used by 1
            self.value -=10
            self.aces -=1

