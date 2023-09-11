from cards import Deck
from players import User, NPC, Dealer, Player
from controls import decisionCheck

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

    def winnerOfGameCheck(self):
        for player in self.players:
            if player.wins >= 5:
                return player
        return False # if there was no player who won, return None

    def winnerOfRoundCheck(self):
        valid = []
        for x in self.players:
            if x.getScore() <= 21:
                print(f"{x} score: {x.getScore()}")
                valid.append(x)
            else:
                print(f"{x} score: BUSTED")
        if valid == []:
            return False #If everyone busted, no one has won.
        else:
            return sorted(valid, key=lambda x: x.getScore(), reverse=True)[0]

def PlayRound(table: Table):
    for player in table.players:
        player.hand.clearHand()
        player.hand.cards += table.deck.DrawCards(2)
        player.playRound(table.deck)

    winner = table.winnerOfRoundCheck()
    if winner == False:
        print("No one Won")
    else:
        print(f"{winner} Won the Round!")
        winner.wins += 1


#Start a game of blackjack with a given table
def GameLoop(table: Table):
    # Check for winners (i.e. someone who has one 5 rounds) if no winners, start a new round. 
    # If winner, the table has won. End the game and announce the winner
    winner = table.winnerOfGameCheck()

    while winner == False:
        PlayRound(table)
        winner = table.winnerOfGameCheck()
    
    print(f"{winner} Won the game")


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
            print("---")
            tableFound = True
        else:
            print("You look for a different table")
    #Start game
    newTable.players.append(User())
    GameLoop(newTable)

def startGame():
    tableLook()