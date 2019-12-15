class Chips:

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):

    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet?"))
        except ValueError:
            print("Sorry, a bet must be an integer")
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet can't exceed", chips.total)
            else:
                break


def hit(deck, hand):

    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input("Would you like to hit or stand? Enter 'h' or 's' ")

        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing")
            player = False

        else:
            print("Sorry, please try again")
            continue
        break


def show_some(player, dealer):
    pass


def show_all(player, dealer):
    pass


def player_busts():
    pass


def player_wins():
    pass


def dealer_busts():
    pass


def dealer_wins():
    pass


def push():
    pass
