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



# dealer=players.dealer()

print("WELCOME TO BLACKJACK")
# remove and return the 4th item

test_deck=cards.Deck() #build the deck
# print(test_deck)
test_deck.shuffle() #shuffle the deck
test_player=cards.Hand() # initiate the hand
test_player.add_card(test_deck.deal()) # deal single card and add it to the add card method
test_player.add_card(test_deck.deal()) # deal single card and add it to the add card method
print(test_player.value)


for card in test_player.cards:
    print(card)
# username=raw_input("Enter your name: ")
# currentplayer=players.human(username)
# bRoll=input("How many chips would you like to bet?")
# bankcheck=currentplayer.checkBank(bRoll)
# while not bankcheck:
#     bRoll=input("How many chips would you like to bet?")
#     bankcheck=currentplayer.checkBank(bRoll)
#     if bankcheck:
#         break

# deck=cards.Deck()#create the deck
# # deck.show()

# currentplayer.show()
# x=deck.shuffle()
# # print(x)
# # deck.showhumancards(x)
