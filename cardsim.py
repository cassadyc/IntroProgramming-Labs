#Cassady Czarnecki
#CMPT 120
#Project 5:Text-Based Card Drawing Simulator
# 2020-05-05
#Collaborated with Vincent Manna

import random

class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def getRank(self):
        return self.rank
    def getSuit(self):
        return self.suit
    
class Deck():
    suits = ["hearts", "clubs", "spades", "diamonds"]
    ranks = ["ace", "jack", "queen", "king", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    def __init__(self):
        self.cards = []
        for rank in Deck.ranks:
            for suit in Deck.suits:
                card = Card(rank, suit)
                self.cards.append(card)
    def shuffle(self):
        random.shuffle(self.cards)
    def draw(self):
        return self.cards.pop()
    
def final():
    d = Deck()
    d.shuffle()
    for i in range(52):
        card = d.draw()
        print("{} of {}".format(card.getSuit(),card.getRank()))

final()





