from cardPackage import cards
from playerPackage import players
# blackjack rule
# will need-two players - human and computer---------- done
# will need-deck of cards --------------------- done
# human player has bank roll ----------------- done
# player starts with two cards face up
# dealer starts with two cards, 1 face up and 1 face down
# player goes first
# player goal is to get closer to total of 21 (sum of cards) before dealer
# player can hit (receive) or stay (stop receiving cards)
# turn by turn basis
# computer turn - if player still under 21, dealer hits until they beat player or busts (go over 21)
# player keeps hitting - and they go over 21, then they bust and lose bet and computer collects the money
# if computer beats by hitting and they get sum higher than human, then computer wins - sum over 21 - simpler version
# will need- face cards (jack,queen,king) count as a value of 10
# aces can count as either 1 or 11 whichever value is preferable to the player

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




global playing
while True:
    
    print("\nWELCOME TO BLACKJACK\n ")

    #build the deck and shuffle
    deck=cards.Deck()
    deck.shuffle()

    #get two cards for player
    player_hand=cards.Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    #get two cards for dealer
    dealer_hand=cards.Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    #take the bet from player
    player_chips=players.Chips()
    take_bet(player_chips)

    players.show_some(player_hand,dealer_hand)

    while players.playing:

        players.hit_or_stand(deck,player_hand)

        players.show_some(player_hand,dealer_hand)

        if player_hand.value > 21:
            players.player_busts(player_hand,dealer_hand,player_chips)
            break 

    

    

