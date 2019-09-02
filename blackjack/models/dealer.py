from typing import Dict

from .action import Action
from .player import Player


class Dealer(Player):

    def get_next_action(self, possible_actions: Dict[Action, str]):
        if Action.hit not in possible_actions:
            raise ValueError("Dealer must always have the possibility to hit.")

        if self.current_hands_values[0] >= 17:
            for card_id, card in self.current_hands[0].items():
                if card.rank == "A" and self.current_hands_values[0] >= 17:
                    card.swap_ace_value()

        else:
            return Action.hit

        return Action.stand
