import pytest

from blackjack.models import Action


@pytest.mark.unit
def test_action_correct_initialization():
    assert Action(0) == Action.hit
    assert Action(1) == Action.stand
    assert Action(2) == Action.double_down
    assert Action(3) == Action.split
    assert Action(4) == Action.insurance_yes
    assert Action(5) == Action.insurance_no


@pytest.mark.unit
def test_action_correct_values():
    assert Action.hit.value == 0
    assert Action.stand.value == 1
    assert Action.double_down.value == 2
    assert Action.split.value == 3
    assert Action.insurance_yes.value == 4
    assert Action.insurance_no.value == 5
