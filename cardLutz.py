"""
This module creates a Card class, Deck class, Player class,
and Game class to simulate a simple game of cards.
Two players are created and dealt hands of three cards,
which are scored according to the traditional ranks,
Ace high, and scores assigned to the suits.
"""
import random

class Card:
    """A class that represents each individual card."""
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def suit_value(self, suit):
        """give numeric values to each suit"""
        if self.suit == "Clubs":
            return 4
        if self.suit == "Hearts":
            return 3
        if self.suit == "Diamonds":
            return 2
        return 1

    def rank_value(self, rank):
        """give numeric values to each rank card, including faces"""
        if self.rank == "T":
            return 10
        if self.rank == "J":
            return 11
        if self.rank == "Q":
            return 12
        if self.rank == "K":
            return 13
        if self.rank == "A":
            return 14
        return int(rank)

    def show(self):
        """show the individual card"""
        self.format_hand = f"{self.rank} of {self.suit}"
        print(self.format_hand)

class Deck:
    """A class that represents a traditional deck of cards"""
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        """Build the deck of 52 cards"""
        for hand_suit in ['Clubs','Hearts','Diamonds','Spades']:
            for hand_rank in ['2','3','4','5','6','7','8','9','T','J','Q','K','A']:
                self.cards.append(Card(hand_suit, hand_rank))

    def shuffle(self):
        """Shuffle the deck"""
        for card in range(len(self.cards) - 1, 0, -1):
            rand_card = random.randint(0, card)
            self.cards[card], self.cards[rand_card] = self.cards[rand_card], self.cards[card]

    def show(self):
        """Display a card from the deck"""
        for card in self.cards:
            card.show()

    def draw(self):
        """Draw a single card from the top of the deck"""
        return self.cards.pop()

class Player:
    """A class that represents each individual player."""
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.my_val_list = []

    def draw_hand(self, deck):
        """Each player builds a hand by drawing cards from the deck"""
        self.hand.append(deck.draw())
        return self

    def show_hand(self):
        """Display the cards in the hand"""
        for card in self.hand:
            card.show()

    def hand_value(self):
        """Calculate the value of the hand using the rules"""
        #self.my_val_list = []
        for card in self.hand:
            my_val = card.suit_value(card.suit) + card.rank_value(card.rank)
            self.my_val_list.append(my_val)
        return sum(self.my_val_list)

class Game:
    """A class that allows the game to be simulated"""
    def __init__(self):
        self.deck = Deck()
        self.player_one = Player("P1")
        self.player_two = Player("P2")

    def play_game(self):
        """A simulation of the game, two players each drawing three cards"""
        self.deck.shuffle()
        for hand in range(3):
            self.player_one.draw_hand(self.deck)
            self.player_two.draw_hand(self.deck)
        p1_val = self.player_one.hand_value()
        p2_val = self.player_two.hand_value()
        print("Player 1's hand is: ")
        self.player_one.show_hand()
        print("Player 1's hand is worth " + str(p1_val) + " points.")
        print("Player 2's hand is: ")
        self.player_two.show_hand()
        print("Player 2's hand is worth " + str(p2_val) + " points.")
        if p1_val > p2_val:
            print("Player 1 wins!")
        elif p1_val < p2_val:
            print("Player 2 wins!")
        else:
            print("It's a tie!")

def main():
    game = Game()
    game.play_game()

if __name__ == '__main__':
    main()
