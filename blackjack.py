from controls import decisionCheck
from gameloop import startGame

#Main Game Init
def init():
    print("-- Welcome to the Python Blackjack Casino! -- ")
    print("Would you like to play or quit? (y/n)")
    if decisionCheck("y","n"):
        #start game
        print("-- Starting Game! --")
        startGame()
    else:
        print(" -- Exiting Game! -- ")
        pass

init()

    