from typing import Dict

from .card import Card
from .action import Action


class Player:
    def __init__(self, player_id: int):
        self.budget: float = 0
        self.player_id: int = player_id
        self.current_hands: Dict[int, Dict[int, Card]] = {}
        self.current_hands_values: Dict[int, int] = {}

    def reset(self, budget: int = 0):
        self.budget = budget
        self.current_hands = {}
        self.current_hands_values = {}

    def make_bet(self, bet: float) -> None:
        self.budget -= bet

    def receive_reward(self, reward: float) -> None:
        self.budget += reward

    def update_hand(self, cards: Dict[int, Card], hand_id: int = 0) -> None:
        self.current_hands[hand_id] = cards

    def _compute_hands_values(self) -> None:
        self.current_hands_values = {hand_id: cards[0].value + cards[1].value for hand_id, cards in
                                     self.current_hands.items()}

    def get_next_action(self, possible_actions: Dict[Action, str]):
        raise NotImplementedError("This method must be implemented in children classes")

    def get_insurance_action(self):
        raise NotImplementedError("This method must be implemented in children classes")