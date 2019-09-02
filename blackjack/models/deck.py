import random

from .card import Card


class Deck:
    """
    Models a deck.

    Parameters
    cards: list
        List of blackjack.models.Card in deck
    remaining_cards: int
        Number of cards left in deck.
    """

    def __init__(self) -> None:
        self._initialize_cards()
        self.shuffle()
        self.remaining_cards = len(self.cards)

    def _initialize_cards(self) -> None:
        """Generates all cards for a new deck."""
        ranks = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"}
        suits = {"clubs", "diamonds", "hearts", "spades"}
        self.cards = [Card(rank, suit) for rank in ranks for suit in suits]

    def shuffle(self) -> None:
        """Shuffles the list of current cards"""
        random.shuffle(self.cards)

    def remove_card(self, rank, suit) -> None:
        """
        Removes the card matching rank and suit from the deck

        Parameters
        ----------
        rank: str
            Card number or letter.
        suit: str
            Either "clubs", "diamonds", "hearts" or "spades"

        Raises
        ------
        ValueError: if any card matching both rank and suit is found in deck
        """

        for card in self.cards:
            if card.rank == rank and card.suit == suit:
                self.cards.remove(card)
                self.remaining_cards -= 1
                return

        raise ValueError(f"Card with rank {rank} and suit {suit} not found in deck")
