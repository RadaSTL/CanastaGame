import Deck as d
import Player as p

class GameLogic(d.Deck,p.Player):

    def __init__(self):
        d.Deck.__init__(self)
        p.Player.__init__(self)
        self.playerList = {}
        self.playerArray = []
        self.deck = []
        self.playerCount = 0x
        self.pile = []
        self.teamCanastas = {}

    def getDeck(self):
        return self.deck

    def getPlayerList(self):
        return self.playerArray

    def getPlayerDict(self):
        return self.playerList

    def getCardFromDeck(self, cardNum):
        return self.deck[cardNum]

    def getPlayer(self,playerIndex):
        return self.playerArray[playerIndex]

    def getPlayerHand(self, playerNum):
        return self.playerList[self.playerArray[playerNum]].hand

    def getPile(self):
        return self.pile

    def startGame(self,playerCount):
        if playerCount not in (2,4):
            raise Exception("You have to either pick 2 or 4")
        else:
            for i in range(playerCount):
                playerName = input("Please enter Player" + str(i) + "'s name: ")
                self.playerArray.append(playerName)
                self.playerList[playerName] = p.Player(playerName, playerCount%1)
            self.deck = d.Deck.CreateDeck(self, playerCount)
            self.playerList[playerCount%1] = []


    def dealCard(self):
        while True:
            self.pile.append(self.deck[-1])
            self.deck.pop(-1)
            if d.Deck.getCardValue(self, self.pile[-1]) not in ["Joker", 2]:
                break

        for i in range(len(self.playerArray)):
            for j in range(15):
                self.playerList[self.playerArray[i]].addCard(self.deck[-1])
                self.deck.pop(-1)

    def discardCard(self, playerNum, card):
        self.pile.append(card)
        self.playerList[self.playerArray[playerNum]].hand.pop(self.playerList[self.playerArray[playerNum]].hand.index(card))

    def drawCard(self,playerNum):
        card = self.deck[-1]
        print("Picked: " + card)
        self.playerList[self.playerArray[playerNum]].hand.append(card)
        self.deck.pop(-1)

    def meldCheck(self,playerNum, card):
        playerDeck = self.playerList[self.playerArray[playerNum]].hand
        currentPile = self.teamCanastas[playerNum]
        pileDic = {}
        for i in range(len(currentPile)):
            pileDic[d.Deck.getCardValue(currentPile[i])] += 1


