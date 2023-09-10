from cards import Deck
from random import randrange
from abc import abstractmethod, ABC
import yaml
from controls import decisionCheck

with open('namebase.yaml','r') as file:
    namebase = yaml.safe_load(file)

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
    
    def clearHand(self):
        self.cards = []

class Player(ABC):

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
    
    @abstractmethod
    def playDecision():
        pass

    def playRound(self, deck:Deck):
        print(f"--- {self}'s turn ---")
        hasPassed = False
        while hasPassed == False:
            if not self.playDecision(deck):
                hasPassed = True
        print(f"{self.name} got {self.getScore()} points")
        if self.getScore() > 21:
            print(f"{self} has busted out")
        elif self.getScore() == 21:
            print(f"{self} has blackjack")
        print(f"--- End of {self}'s turn --")

class User(Player):
    def __init__(self) -> None:
        super().__init__(name="You")

    def printHand(self):
        print(f"{self.name} have the following cards: ")
        for card in self.hand.cards:
            print(card)

    def playDecision(self, deck:Deck):
        self.printHand()
        if self.hand.calculateScore() < 21:
            print("Would you like to draw a card? (y/n)")
            if decisionCheck("y","n"):
                #choose to draw
                print(f"{self.name} draws another card")
                self.hand.cards += deck.DrawCards(1)
                return True
            else:
                #choose to hold
                print(f"{self.name} hold")
                return False
        else:
            return False

class NPC(Player):

    def __init__(self) -> None:
        super().__init__(self.nameGen()) #Get Random Name from namebase YAML

    def nameGen(self):
        return str(namebase['names'][randrange(0,len(namebase['names']))]).capitalize()

    def setName(self):
        self.name = self.nameGen()

    def playDecision(self, deck: Deck):
        self.printHand()
        if self.hand.calculateScore() < 21:
            roll = randrange(0,100)
            if roll >= 50:
                #choose to draw
                print(f"{self.name} draws another card")
                self.hand.cards += deck.DrawCards(1)
                return True
            else:
                #choose to hold
                print(f"{self.name} holds")
                return False
        else:
            return False
        


class Dealer(NPC):
    def __init__(self) -> None:
        super().__init__()