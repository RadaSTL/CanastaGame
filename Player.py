class Player:

    def __init__(self, name = ""):
        self.name = name
        self.hand = []
        self.score = 0
        self.meld = []

    def getName(self):
        return self.name

    def addCard(self, card):
        self.hand.append(card)