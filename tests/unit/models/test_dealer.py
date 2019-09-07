import pytest

from blackjack.models import Dealer, Card, Action


@pytest.mark.unit
def test_dealer_get_next_action_is_hit_if_hand_is_less_than_17():
    dealer = Dealer()
    dealer.current_hands_values = {0: 11}
    dealer.current_hands = {
        0: {0: Card('A', 'diamonds')}
    }

    assert dealer.get_next_action({Action.hit: '', Action.stand: ''}) == Action.hit


@pytest.mark.unit
def test_dealer_get_next_action_is_hit_if_hand_is_17_but_has_ace():
    dealer = Dealer()
    dealer.current_hands_values = {0: 17}
    dealer.current_hands = {
        0: {0: Card('A', 'diamonds'), 1: Card('6', 'spades')}
    }

    assert dealer.get_next_action({Action.hit: '', Action.stand: ''}) == Action.hit


@pytest.mark.unit
def test_dealer_get_next_action_is_stand_if_hand_is_17_and_has_no_ace():
    dealer = Dealer()
    dealer.current_hands_values = {0: 17}
    dealer.current_hands = {
        0: {0: Card('K', 'diamonds'), 1: Card('7', 'spades')}
    }

    assert dealer.get_next_action({Action.hit: '', Action.stand: ''}) == Action.stand


@pytest.mark.unit
def test_dealer_raises_valueerror_if_hit_not_in_possible_actions():
    with pytest.raises(ValueError, match="Dealer must always have the possibility to hit."):
        Dealer().get_next_action({})
