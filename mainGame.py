import GameLogic as gl

testGame = gl.GameLogic()

testGame.startGame(2)
testGame.dealCard()

print(testGame.getPile())

card = testGame.getPile()[0]

print(card)

for card in testGame.getPlayerHand(0):
    cardVal = testGame.getCardValue(card)%100
    print(testGame.getCardValue(card))
    print(cardVal)

