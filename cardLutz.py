import random

class Card:
    """A class that represents each individual card."""
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def suitValue(self, suit):
        """give numeric values to each suit"""
        if suit == "Clubs":
            return 4
        elif suit == "Hearts":
            return 3
        elif suit == "Diamonds":
            return 2
        else:
            return 1
        
    def rankValue(self, rank):
        """give numeric values to each rank card, including faces"""
        if rank == "T":
            return 10
        elif rank == "J":
            return 11
        elif rank == "Q":
            return 12
        elif rank == "K":
            return 13
        elif rank == "A":
            return 14
        else:
            return int(rank)
        
    def show(self):
        """show the individual card"""
        print('{} of {}'.format(self.rank, self.suit))

class Deck:
    """A class that represents a traditional deck of cards"""
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        """Build the deck of 52 cards"""
        for s in ['Clubs','Hearts','Diamonds','Spades']:
            for r in ['2','3','4','5','6','7','8','9','T','J','Q','K','A']:
                self.cards.append(Card(s, r))

    def shuffle(self):
        """Shuffle the deck"""
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def show(self):
        """Display a card from the deck"""
        for c in self.cards:
            c.show()

    def draw(self):
        """Draw a single card from the top of the deck"""
        return self.cards.pop()

class Player:
    """A class that represents each individual player."""
    def __init__(self, name):
        self.name = name
        self.hand = []

    def drawHand(self, deck):
        """Each player builds a hand by drawing cards from the deck"""
        self.hand.append(deck.draw())
        return self

    def showHand(self):
        """Display the cards in the hand"""
        for card in self.hand:
            card.show()

    def handValue(self):
        """Calculate the value of the hand using the rules"""
        self.myValList = []
        for card in self.hand:
            myVal = card.suitValue(card.suit) + card.rankValue(card.rank)
            self.myValList.append(myVal)
        return sum(self.myValList)

class Game:
    """A class that allows the game to be simulated"""
    def __init__(self):
        pass

    def playGame(self):
        """A simulation of the game, two players each drawing three cards"""
        gameDeck = Deck()
        P1 = Player("P1")
        P2 = Player("P2")
        gameDeck.shuffle()
        for h in range(3):
            P1.drawHand(gameDeck)
            P2.drawHand(gameDeck)
        P1Val = P1.handValue()
        P2Val = P2.handValue()
        print("Player 1's hand is: ")
        P1.showHand()
        print("Player 1's hand is worth " + str(P1Val) + " points.")
        print("Player 2's hand is: ")
        P2.showHand()
        print("Player 2's hand is worth " + str(P2Val) + " points.")
        if P1Val > P2Val:
            print("Player 1 wins!")
        elif P1Val < P2Val:
            print("Player 2 wins!")
        else:
            print("It's a tie!")
 

def main():
    game = Game()
    game.playGame()

if __name__ == '__main__':
    main()
