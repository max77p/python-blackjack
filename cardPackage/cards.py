import random;

# suits=pass
# ranks=pass
# values=pass

# player=True

class Card:
    def __init__(self):
        pass

    def __str__(self);
        pass


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in range(1, 14):
                self.cards.append(Card(s, v))

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in reversed(xrange(len(self.cards)-1)):
            r = random.randint(0, i)
            self.cards[r].show()
            self.cards[i].show()


    # def showhumancards(self, rand):
    #     self.cards[rand[0]].show()
    #     self.cards[rand[1]].show()
