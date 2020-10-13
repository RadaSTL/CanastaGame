import random as rnd

def intCast(input):
    try:
        int(input)
        return int(input)
    except ValueError:
        return False
    except:
        raise

class Deck:
    def __init__(self):
        self.CurrentDeck = []

    def CreateDeck(self, playerCount):

        if playerCount % 2 != 0:
            raise Exception("Invalid Number of players!")

        faceCards = ["A", "K", "Q", "J"]
        shapes = ["⯁", "♥", "♠", "♣"]
        joker = "Joker"

        for y in range(int(playerCount/2)):
            for i in range(len(shapes)):
                for j in range(len(faceCards)):
                    self.CurrentDeck.append(shapes[i]+faceCards[j])
                for j in range(2,11):
                    self.CurrentDeck.append(shapes[i]+str(j))

        self.CurrentDeck.append(joker)
        self.CurrentDeck.append(joker)
        self.CurrentDeck.append(joker)
        self.CurrentDeck.append(joker)

        rnd.shuffle(self.CurrentDeck)

        return self.CurrentDeck

    def getCardBonus(self, card):

        if intCast(card[1]) in [4,5,6,7] or card in ["♠3", "♣3"]:
            return 5
        elif intCast(card[1:]) in [8,9,10] or card[1:] in ["Q","J","K"]:
            return 10
        elif intCast(card[1:]) in [2] or card[1:] in ["A"]:
            return 20
        elif card == "Joker":
            return 50
        else:
            return 100

    def getCardValue(self,card):
        if intCast(card[1:]):
            return int(card[1:])
        elif card != "Joker":
            return card[1:]
        else:
            return "Joker"

    def getCardColor(self,card):
        colors = {"⯁": "red", "♥": "red", "♠": "black", "♣": "black"}

        if card[0] in colors:
            return colors[card[0]]
        else:
            return "Joker"


    def __str__(self):

        return "A class for deck and the cards. Including following functions:\n" \
               "CreateDeck(playerCount) = Creates a deck of cards to play canasta " \
               "epending on the number of players, " \
               "i.e: if there are 4 players, 2 decks will be dealt (playerCount/2).\n" \
               "getCardBonus(card) = returns the point value of selected card.\n" \
               "getCardValue(card) = returns the value of the card.\n" \
               "getCardColor(card) = returns the color of card.\n"


