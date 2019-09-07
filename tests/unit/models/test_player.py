import pytest

from blackjack.models import Player, Card


@pytest.mark.unit
def test_player_initializes_correctly():
    player = Player(1)
    assert player.budget == 0
    assert player.player_id == 1
    assert player.current_hands == {}
    assert player.current_hands_values == {}


@pytest.mark.unit
@pytest.mark.parametrize("budget", [0, 100, 2000])
def test_player_reset_correctness(budget):
    player = Player(1)
    player.budget = 5
    player.current_hands_values = {0: 10, 1: 21}
    player.current_hands = {
        0: {0: Card('4', 'hearts'), 1: Card('6', 'clubs')},
        1: {0: Card('A', 'diamonds'), 1: Card('10', 'spades')}
    }

    player.reset(budget)

    assert player.budget == budget
    assert player.player_id == 1
    assert player.current_hands == {}
    assert player.current_hands_values == {}


@pytest.mark.unit
@pytest.mark.parametrize("bet", [10, 100, 1000])
def test_player_make_bet_subtracts_correct_value(bet):
    player = Player(1)
    player.budget = 1000

    player.make_bet(bet)

    assert player.budget == 1000 - bet


@pytest.mark.unit
@pytest.mark.parametrize("reward", [10, 100, 1000])
def test_player_make_bet_adds_correct_value(reward):
    player = Player(1)
    player.budget = 1000

    player.receive_reward(reward)

    assert player.budget == 1000 + reward


@pytest.mark.unit
def test_player_compute_hands_values_correctness():
    player = Player(1)

    player.current_hands = {
        0: {0: Card('4', 'hearts'), 1: Card('6', 'clubs')},
        1: {0: Card('A', 'diamonds'), 1: Card('10', 'spades')}
    }

    player._compute_hands_values()

    assert player.current_hands_values == {0: 10, 1: 21}


@pytest.mark.unit
def test_player_update_hand_correctness():
    player = Player(1)

    player.update_hand({0: Card('4', 'hearts'), 1: Card('6', 'clubs')}, 0)
    player.update_hand({0: Card('A', 'diamonds'), 1: Card('10', 'spades')}, 1)

    assert player.current_hands_values == {0: 10, 1: 21}
    assert player.current_hands[0][0].rank == '4'
    assert player.current_hands[0][0].suit == 'hearts'
    assert player.current_hands[0][1].rank == '6'
    assert player.current_hands[0][1].suit == 'clubs'
    assert player.current_hands[1][0].rank == 'A'
    assert player.current_hands[1][0].suit == 'diamonds'
    assert player.current_hands[1][1].rank == '10'
    assert player.current_hands[1][1].suit == 'spades'


@pytest.mark.unit
def test_player_get_next_action_raises_notimplementederror():
    with pytest.raises(NotImplementedError, match="This method must be implemented in children classes"):
        Player(1).get_next_action(None)


@pytest.mark.unit
def test_player_get_insurance_action_next_action_raises_notimplementederror():
    with pytest.raises(NotImplementedError, match="This method must be implemented in children classes"):
        Player(1).get_insurance_action()
