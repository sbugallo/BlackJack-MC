from blackjack.models import Deck
import pytest


@pytest.mark.unit
def test_deck_initializes_correctly():
    deck = Deck()
    assert deck.remaining_cards == len(deck.cards) == 52

    num_aces = 0
    num_ones = 0
    num_spades = 0
    for card in deck.cards:
        if card.rank == "1":
            num_ones += 1
        elif card.rank == "A":
            num_aces += 1

        if card.suit == "spades":
            num_spades += 1

    assert num_aces == 0
    assert num_ones == 4
    assert num_spades == 13


@pytest.mark.unit
def test_deck_shuffles_cards():
    deck = Deck()
    before = deck.cards.copy()
    deck.shuffle()
    assert before != deck.cards


@pytest.mark.unit
def test_deck_removes_cards():
    deck = Deck()
    rank = "4"
    suit = "clubs"

    assert deck.remaining_cards == 52
    deck.remove_card(rank, suit)
    assert deck.remaining_cards == 51

    for card in deck.cards:
        assert card.suit != suit or card.rank != rank


@pytest.mark.unit
def test_deck_raises_error_when_trying_to_remove_card_not_in_deck():

    deck = Deck()
    deck.remove_card("4", "spades")
    with pytest.raises(ValueError, match="Card with rank 4 and suit spades not found in deck"):
        deck.remove_card("4", "spades")

    with pytest.raises(ValueError, match="Card with rank fake_rank and suit fake_suit not found in deck"):
        deck.remove_card("fake_rank", "fake_suit")
