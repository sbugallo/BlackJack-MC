from typing import Dict

from .action import Action
from .player import Player


class Dealer(Player):
    """
    Models the dealer.

    Attributes
    ----------
    budget: int
        Player's money.
    player_id: float
        Player's ID.
    current_hands: dict
        Player's cards. Format {hand_id: {0: Card, 1: Card}}
    current_hands_values: dict
        Value of each hand.
    """

    def __init__(self) -> None:
        super().__init__(-1)

    def get_next_action(self, possible_actions: Dict[Action, str]) -> Action:
        """
        Retrieves the next action to be taken by the dealer. It will always choose hit till its hand value is 17 or
        higher.

        Parameters
        ----------
        possible_actions: dict
            Possible actions to be taken. Format: {blackjack.models.Action: description}

        Returns
        -------
        action_to_be_taken: blackjack.models.Action
        """
        if Action.hit not in possible_actions:
            raise ValueError("Dealer must always have the possibility to hit.")

        if self.current_hands_values[0] >= 17:
            for card_id, card in self.current_hands[0].items():
                if card.rank == "A" and self.current_hands_values[0] >= 17:
                    card.swap_ace_value()
                    self._compute_hands_values()

                    if self.current_hands_values[0] < 17:
                        return Action.hit
        else:
            return Action.hit

        return Action.stand
