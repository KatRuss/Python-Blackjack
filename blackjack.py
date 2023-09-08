from dataclasses import dataclass
from enum import Enum 
from random import shuffle, randrange
import yaml

with open('namebase.yaml','r') as file:
    namebase = yaml.safe_load(file)

class CardSuit(Enum):
    SPADES = 1
    DIAMONS = 2
    CLUBS = 3
    HEARTS = 4

@dataclass
class Card():
    rank: int
    suit: CardSuit

    def setScore(self):
        if self.rank >= 11:
            self.score = 10
        else:
            self.score = self.rank

    def setRankName(self):
        _rankStr = ""
        if self.rank == 1:
            _rankStr = "Ace"
        elif self._rankStr == 11:
            _rankStr = "Jack"
        elif self._rankStr == 12:
            _rankStr = "Queen"
        elif self._rankStr == 13:
            _rankStr = "King"
        else: 
            _rankStr = str(self.rank)
        return _rankStr

    def __post_init__(self):
        self._name = f"{self.setRankName()} of {self.suit.name}"
        self.setScore()

    def __str__(self) -> str:
        return self._name

class Player():

    def __init__(self, name: str) -> None:
        self.name = name
        self.hand = Hand()
        self.wins = 0

    def getScore(self):
        return self.hand.calculateScore()

    def printHand(self):
        print(f"{self.name} has the following cards: ")
        for card in self.hand.cards:
            print(card)
    
    def __str__(self) -> str:
        return f"{self.name} ({self.wins})"
    
    def __lt__(self, other):
        if type(other) == Player:
            return self.getScore() < other.getScore()
        else:
            yield TypeError()

class User(Player):
    def __init__(self) -> None:
        super().__init__(name="You")

    def printHand(self):
        print(f"{self.name} have the following cards: ")
        for card in self.hand.cards:
            print(card)

class Table():
    def __init__(self) -> None:
        self.players = []
        self.dealer = Dealer()
        self.generateTable(4)

    def generateTable(self, num: int):
        #Add NPCs to table
        for x in range(0,num):
            self.players.append(NPC())

class Hand():
    def __init__(self) -> None:
        self.cards = []
    
    def calculateScore(self):
        result = 0
        for card in self.cards:
            if card.rank == 1 and result <= 10: #ace check
                result += 11
            else:
                result += card.score
        return result

class Deck():
    def __init__(self) -> None:    
        self.RefreshDeck()

    def Shuffle(self):
        shuffle(self.cards)

    def DrawCards(self,amount):
        draw = []
        for x in range(0,amount):
            draw.append(self.cards.pop())
        return draw
    
    def getSize(self):
        return len(self.cards)

    def RefreshDeck(self):
        self.cards = [Card(rank=rank,suit=suit) for suit in CardSuit for rank in range(1,14)]
        self.Shuffle()

class NPC(Player):

    def __init__(self) -> None:
        super().__init__(self.nameGen()) #Get Random Name from namebase YAML

    def nameGen(self):
        return str(namebase['names'][randrange(0,len(namebase['names']))]).capitalize()

    def setName(self):
        self.name = self.nameGen()

    def playDecision(self, deck: Deck):
        roll = randrange(0,100)
        if roll >= 50:
            #choose to draw
            self.hand.cards += deck.DrawCards(1)
        else:
            #choose to hold
            pass

class Dealer(NPC):
    def __init__(self) -> None:
        super().__init__()

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

#Start a game of blackjack with a given table
def startGame(table: Table):
    # Check for winners (i.e. someone who has one 5 rounds)
    # if no winners, start a new round. If winner, the table has won. End the game and announce the winner
    # if not table.winnercheck():
    #     roundStart()
    # else:
    #     print("Someone has won the game")
    pass  

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
    startGame(newTable)

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