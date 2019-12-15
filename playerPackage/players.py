


class human:
    def __init__(self, name):
        self.name = name
        self.bank = 100

    def show(self):
        print("{} is name and {} is bank".format(self.name, self.bank))

    def checkBank(self, desiredamount):
        print(desiredamount)
        if desiredamount < self.bank:
            self.bank = self.bank-desiredamount
            print("New amount is {}".format(self.bank))
            return True
        else:
            print("Sorry you don't have enough chips. You have: {}".format(self.bank))
            return False



class dealer:
    def __init__(self):
        self.name = "Dealer"
        print("Dealer created")
