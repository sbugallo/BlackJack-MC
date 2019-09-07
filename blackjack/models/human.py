from typing import Dict

from loguru import logger

from .action import Action
from .player import Player


class Human(Player):
    """
    Models a human player.

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

    def get_next_action(self, possible_actions: Dict[Action, str]) -> Action:
        """
        Retrieves the next action to be taken by the player.

        Parameters
        ----------
        possible_actions: dict
            Possible actions to be taken. Format: {blackjack.models.Action: description}

        Returns
        -------
        action_to_be_taken: blackjack.models.Action
        """

        idx_to_action = {}
        text = "\nIt's your turn, what would you like to do?\n"
        for i, (action, description) in enumerate(possible_actions.items()):
            idx_to_action[i] = action
            action_idx = i + 1
            action_name = action.name.upper()
            text += f"\t- {action_idx}. {action_name}: {description}\n"

        chosen_action = int(input()) - 1
        while chosen_action not in idx_to_action.keys():
            logger.info("Wrong option! Please try again: ")
            chosen_action = int(input()) - 1

        return idx_to_action[chosen_action]

    def get_insurance_action(self) -> Action:
        """
        Retrieves whether the player will make an insurance bet or not.

        Returns
        -------
        action_to_be_taken: blackjack.models.Action
        """

        logger.info("Do you want to make an insurance bet?\n\t- 1. Yes\n\t2. No\n")
        idx_to_action = {0: Action.insurance_yes, 1: Action.insurance_no}

        chosen_action = int(input()) - 1
        while chosen_action not in idx_to_action.keys():
            logger.info("Wrong option! Please try again: ")
            chosen_action = int(input()) - 1

        return idx_to_action[chosen_action]
