from dataclasses import dataclass
from enum import Enum 
from random import shuffle

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
        elif self.rank == 11:
            _rankStr = "Jack"
        elif self.rank == 12:
            _rankStr = "Queen"
        elif self.rank == 13:
            _rankStr = "King"
        else: 
            _rankStr = str(self.rank)
        return _rankStr

    def __post_init__(self):
        self._name = f"{self.setRankName()} of {self.suit.name}"
        self.setScore()

    def __str__(self) -> str:
        return self._name
    
class Deck():
    def __init__(self) -> None:    
        self.RefreshDeck()

    def Shuffle(self):
        shuffle(self.cards)

    def DrawCards(self,amount):
        draw = []
        for x in range(0,amount):
            if len(self.cards) <= 0:
                print("** The dealer has pulled out a fresh deck of cards from under the table. **")
                self.RefreshDeck()
            draw.append(self.cards.pop())
        return draw
    
    def getSize(self):
        return len(self.cards)

    def RefreshDeck(self):
        self.cards = [Card(rank=rank,suit=suit) for suit in CardSuit for rank in range(1,14)]
        self.Shuffle()