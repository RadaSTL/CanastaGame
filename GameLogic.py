import Deck as d
import Player as p

class GameLogic(d.Deck,p.Player):

    def __init__(self):
        d.Deck.__init__(self)
        p.Player.__init__(self)
        self.playerList = {}
        self.playerArray = []
        self.deck = []
        self.playerCount = 0
        self.pile = []
        self.teamCanastas = {}

    def getDeck(self):
        return self.deck

    def getTeamCanastas(self):
        return self.teamCanastas

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

    def getTeamMendCards(self, teamNum):
        return self.teamCanastas[teamNum][0]

    def getTeamMendValues(self, teamNum):
        return self.teamCanastas[teamNum][1]

    def getPlayerTeam(self, playerNum):
        if playerNum in [0,2]:
            return 1
        else:
            return 2

    def startGame(self,playerCount):
        if playerCount not in (2,4):
            raise Exception("You have to either pick 2 or 4")
        else:
            canastaDic = {"cardCanasta":[], "valueCanasta":[]}
            for i in range(playerCount):
                playerName = input("Please enter Player" + str(i) + "'s name: ")
                self.playerArray.append(playerName)
                self.playerList[playerName] = p.Player(playerName, playerCount%1)
            for i in range(2):
                self.teamCanastas[i+1] = canastaDic
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

    def meldCheck(self,playerNum, card = None, mend = []):
        teamNum = self.getPlayerTeam(playerNum)
        index = self.teamCanastas[teamNum]["cardCanasta"].indexof(mend)
        cardVal = self.getCardValue(card)
        mendVal = self.teamCanastas[teamNum]["valueCanasta"][index]
        mendType = 0
        # Type = 1 same numbers, Type = 2 serials (like 3,4,5)

        if cardVal == 1402 and mendVal.count(1402) < 3:
            return True
        elif cardVal == 1402 and mendVal.count(1402) == len(mendVal):
            return True

        checkVal = mendVal[0]%100
        cnt = 0
        for i in mendVal:
            if checkVal == i%100 or i%100 == 2:
                cnt += 1
            else:
                cnt -= 1
        if cnt >= 3:
            mendType = 1
        else:
            mendType = 2

        index = 0

        while mendType == 1:
            try:
                if mendVal[index] != 1402 and cardVal%100 == mendVal[index]%100:
                    return True
                else:
                    index += 1
            except:
                return False





    def meldCheck(self,playerNum, cardArray = []):
        teamNum = self.getPlayerTeam(playerNum)
        playerDeck = self.playerList[self.playerArray[playerNum]].hand
        currentMends = self.teamCanastas[teamNum]


