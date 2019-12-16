playing = True

class Chips:

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def hit(deck, hand):

    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing

    while True:
        x = raw_input("Would you like to hit or stand? Enter 'h' or 's' ")
        print(x)
        if x[0].lower() == 'h':
            hit(deck, hand)

        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing")
            playing = False

        else:
            print("Sorry, please try again")
            continue
        break


def show_some(player, dealer):
    print("------------------------show some-------------")
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print(''+dealer.cards[1].__str__()+"\n")
    for x in player.cards:
        print("Player's Hand: "+x.__str__())
    print("------------------------show some-------------")
    # print("\nPlayer's Hand:".join((str(p) for p in player.cards))+"\n ")


def show_all(player, dealer):
    print("------------------------show ALL-------------")
    print("\nDealer's Hand:".join((str(p) for p in dealer.cards)))
    print("Dealer's Hand =", dealer.value)
    for x in player.cards:
        print("\nPlayer's Hand:"+x.__str__())
    print("Player's Hand =", player.value)
    print("------------------------show all-------------")


def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()


def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()


def dealer_busts(player,dealer,chips):
    print("Dealer busts")
    chips.win_bet()


def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet


def push(player, dealer):
    print("Dealer and Player tie! It's a push.")
