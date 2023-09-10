from cards import Deck
from players import User, NPC, Dealer, Player

class Table():
    def __init__(self) -> None:
        self.players = []
        self.dealer = Dealer()
        self.deck = Deck()
        self.generateTable(4)


    def generateTable(self, num: int):
        #Add NPCs to table
        for x in range(0,num):
            self.players.append(NPC())
        self.deck.RefreshDeck()

    def winnerCheck(self):
        for player in self.players:
            if player.getScore() >= 5:
                return player
        return False # if there was no player who won, return None




#Universal Yes/No user input function
def decisionCheck(yesInput: str, noInput: str): 
    decision = input(">> ")
    if decision == yesInput:
        return True
    elif decision == noInput:
        return False
    else:
        print(f"{decision} is not a valid key")
        print(f"The Valid Keys are [{yesInput}/{noInput}]")
        return decisionCheck(yesInput,noInput)


def PlayRound(table: Table):
    for player in table.players:
        player.playRound(table.deck)


#Start a game of blackjack with a given table
def GameLoop(table: Table):
    # Check for winners (i.e. someone who has one 5 rounds) if no winners, start a new round. If winner, the table has won. End the game and announce the winner
    winner = table.winnerCheck()
    if isinstance(winner,Player):
        # a player has won!
        print(f"{winner} has won!")
    elif winner == False:
        PlayRound(table)


def tableLook():
    tableFound = False
    print("You enter the casio. Through the garish wallpaper and carpet you find a table")
    while not tableFound:
        #Create and Introduce Table
        newTable = Table()
        print("On this table you see the following players: ")
        for player in newTable.players:
            print(player)
        print("The dealer for the table is: ")
        print(newTable.dealer)
        print("Would you like to sit at this table? (y/n)")
        if decisionCheck("y","n"):
            #sit at table
            print("You have sat at the table")
            tableFound = True
        else:
            print("You look for a different table")
    #Start game
    newTable.players.append(User())
    GameLoop(newTable)

#Main Game Init
def init():
    print("-- Welcome to the Python Blackjack Casino! -- ")
    print("Would you like to play or quit? (y/n)")
    if decisionCheck("y","n"):
        #start game
        print("-- Starting Game! --")
        tableLook()
    else:
        print(" -- Exiting Game! -- ")
        pass

init()