import GameLogic as gl

testGame = gl.GameLogic()

testGame.startGame(2)
testGame.dealCard()

print(testGame.getPile())