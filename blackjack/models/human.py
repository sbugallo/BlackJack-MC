from typing import Dict

from loguru import logger

from .action import Action
from .player import Player


class Human(Player):

    def get_next_action(self, possible_actions: Dict[Action, str]):

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

    def get_insurance_action(self):
        logger.info("Do you want to make an insurance bet?\n\t- 1. Yes\n\t2. No\n")
        idx_to_action = {0: Action.insurance_yes, 1: Action.insurance_no}

        chosen_action = int(input()) - 1
        while chosen_action not in idx_to_action.keys():
            logger.info("Wrong option! Please try again: ")
            chosen_action = int(input()) - 1

        return idx_to_action[chosen_action]
