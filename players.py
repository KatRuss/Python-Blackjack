from cards import Deck
from random import randrange
from abc import abstractmethod, ABC
import yaml

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
    
    def __lt__(self, other):
        if type(other) == Player:
            return self.getScore() < other.getScore()
        else:
            yield TypeError()
    
    @abstractmethod
    def playRound(self, deck:Deck):
        pass

class User(Player):
    def __init__(self) -> None:
        super().__init__(name="You")

    def printHand(self):
        print(f"{self.name} have the following cards: ")
        for card in self.hand.cards:
            print(card)

    def playRound(self, deck:Deck):
        pass

class NPC(Player):

    def __init__(self) -> None:
        super().__init__(self.nameGen()) #Get Random Name from namebase YAML

    def nameGen(self):
        return str(namebase['names'][randrange(0,len(namebase['names']))]).capitalize()

    def setName(self):
        self.name = self.nameGen()

    def playDecision(self, deck: Deck):
        if self.hand.calculateScore() < 21:
            roll = randrange(0,100)
            if roll >= 50:
                #choose to draw
                self.hand.cards += deck.DrawCards(1)
                return True
            else:
                #choose to hold
                return False
        else:
            return False
        
    def playRound(self, deck:Deck):
        hasPassed = False
        while hasPassed == False:
            if not self.playDecision(deck):
                hasPassed = True

class Dealer(NPC):
    def __init__(self) -> None:
        super().__init__()