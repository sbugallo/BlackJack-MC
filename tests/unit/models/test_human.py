import pytest
import builtins

from blackjack.models import Human, Action


@pytest.mark.unit
def test_human_get_next_action_asks_for_action_till_selects_valid_option(mocker):
    human = Human(1)

    with mocker.patch('builtins.input', side_effect=[5, 6, 1]):
        assert human.get_next_action({Action.hit: '', Action.stand: ''}) == Action.hit
        assert builtins.input.call_count == 3


@pytest.mark.unit
def test_human_get_insurance_action_asks_for_action_till_selects_valid_option(mocker):
    human = Human(1)

    with mocker.patch('builtins.input', side_effect=[5, 6, 1]):
        assert human.get_insurance_action() == Action.insurance_yes
        assert builtins.input.call_count == 3
