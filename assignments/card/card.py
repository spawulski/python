"""
Docmentation for the Card and Deck classes.

When combined these classes represent a deck of playing cards.
"""
import random


class Card:
    """
    The Card class.

    The Card class represents an individual playing card.
    """

    def __init__(self, suit, number):
        """Instantiate an instance of the Card class with a suit and number."""
        self._suit = suit
        self._number = number

    def __repr__(self):
        """Text representation of a Card."""
        return self._number + " of " + self._suit

    @property
    def suit(self):
        """Getter for Card suit."""
        return self._suit

    @suit.setter
    def suit(self, suit):
        if suit in ["hearts", "clubs", "diamonds", "spades"]:
            self._suit = suit
        else:
            print("That's not a suit!")

    @property
    def number(self):
        """Getter for Card number."""
        return self._number

    @number.setter
    def number(self, number):
        valid = [str(n) for n in range(2, 11)] + ["J", "Q", "K", "A"]
        if number in valid:
            self._number = number
        else:
            print("That's not a valid number")


class Deck:
    """
    The Deck class.

    The Deck class represents a standard full deck of playing cards.
    """

    def __init__(self):
        """Initialize a Deck object with a full set of playing cards."""
        self._cards = []
        self.populate()

    def populate(self):
        """Iterate through the suits and numbers to build a deck of cards."""
        suits = ["hearts", "clubs", "diamonds", "spades"]
        numbers = [str(n) for n in range(2, 11)] + ["J", "Q", "K", "A"]
        self._cards = [Card(s, n) for s in suits for n in numbers]

    def shuffle(self):
        """Shuffle randomizes the order of cards in a Deck object."""
        random.shuffle(self._cards)

    def deal(self, no_of_cards):
        """Deal a number of cards as a hand."""
        dealt_cards = []
        for _i in range(no_of_cards):
            dealt_card = self._cards.pop(0)
            dealt_cards.append(dealt_card)
        return dealt_cards

    def __repr__(self):
        """Print out the number of cards currently in the deck."""
        cards_in_deck = len(self._cards)
        return "Deck of " + str(cards_in_deck) + " cards"


DECK = Deck()
print(DECK)
Deck.shuffle(DECK)
print(Deck.deal(DECK, 7))
print(DECK)
