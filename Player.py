class Player:

    def __init__(self, name = "", team = 0):
        self.name = name
        self.hand = []
        self.score = 0
        self.meld = []
        self.team = team

    def getName(self):
        return self.name

    def addCard(self, card):
        self.hand.append(card)

    def getTeam(self):
        return self.team