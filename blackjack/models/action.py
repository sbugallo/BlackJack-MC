from enum import Enum


class Action(Enum):
    """Models all possible actions."""
    hit: int = 0
    stand: int = 1
    double_down: int = 2
    split: int = 3
    insurance_yes: int = 4
    insurance_no: int = 5
