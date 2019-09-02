import pytest

from blackjack.models import Card


@pytest.mark.unit
@pytest.mark.parametrize("rank, suit, expected_icon, expected_value", [
    ("1", "clubs", "\u2663", 1),
    ("2", "hearts", "\u2665", 2),
    ("3", "spades", "\u2660", 3),
    ("4", "diamonds", "\u2666", 4),
    ("5", "clubs", "\u2663", 5),
    ("6", "hearts", "\u2665", 6),
    ("7", "spades", "\u2660", 7),
    ("8", "diamonds", "\u2666", 8),
    ("9", "clubs", "\u2663", 9),
    ("10", "hearts", "\u2665", 10),
    ("J", "spades", "\u2660", 10),
    ("Q", "diamonds", "\u2666", 10),
    ("K", "clubs", "\u2663", 10),
    ("A", "hearts", "\u2665", 11),
])
def test_card_correct_initilization(rank, suit, expected_icon, expected_value):

    card = Card(rank, suit)

    assert card.rank == rank
    assert card.suit == suit
    assert card.icon == expected_icon
    assert card.value == expected_value


@pytest.mark.unit
def test_card_raises_valueerror_if_invalid_rank():
    with pytest.raises(ValueError, match="Invalid rank fake_rank"):
        Card("fake_rank", "clubs")


@pytest.mark.unit
def test_card_raises_valueerror_if_invalid_suit():
    with pytest.raises(ValueError, match="Invalid suit fake_suit"):
        Card("A", "fake_suite")


@pytest.mark.unit
@pytest.mark.parametrize("rank, suit, expected_string", [
    ("1", "clubs", "1\x1b[34m\u2663\x1b[39m"),
    ("2", "hearts", "2\x1b[31m\u2665\x1b[39m"),
    ("3", "spades", "3\x1b[34m\u2660\x1b[39m"),
    ("4", "diamonds", "4\x1b[31m\u2666\x1b[39m"),
    ("5", "clubs", "5\x1b[34m\u2663\x1b[39m"),
    ("6", "hearts", "6\x1b[31m\u2665\x1b[39m"),
    ("7", "spades", "7\x1b[34m\u2660\x1b[39m"),
    ("8", "diamonds", "8\x1b[31m\u2666\x1b[39m"),
    ("9", "clubs", "9\x1b[34m\u2663\x1b[39m"),
    ("10", "hearts", "10\x1b[31m\u2665\x1b[39m"),
    ("J", "spades", "J\x1b[34m\u2660\x1b[39m"),
    ("Q", "diamonds", "Q\x1b[31m\u2666\x1b[39m"),
    ("K", "clubs", "K\x1b[34m\u2663\x1b[39m"),
    ("A", "hearts", "A\x1b[31m\u2665\x1b[39m")
])
def test_card_to_string_correctness(rank, suit, expected_string):
    card = Card(rank, suit)
    assert card.to_string() == expected_string


@pytest.mark.unit
@pytest.mark.parametrize("rank, initial_value, expected_value", [
    ("1", 1, 11),
    ("A", 11, 1),
])
def test_card_swap_ace_value_correctness(rank, initial_value, expected_value):
    card = Card(rank, "clubs")
    assert card.value == initial_value
    card.swap_ace_value()
    assert card.value == expected_value


@pytest.mark.unit
def test_card_swap_ace_value_raises_valueerror_if_card_is_not_an_ace():
    card = Card("2", "hearts")
    with pytest.raises(ValueError, match="Only aces can swap values"):
        card.swap_ace_value()
