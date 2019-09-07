from typing import Dict

from .card import Card
from .action import Action


class Player:
    """
    Models a generic poker player.

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
    def __init__(self, player_id: int) -> None:
        """
        Parameters
        ----------
        player_id: int
            Player's ID.
        """
        self.budget: float = 0
        self.player_id: int = player_id
        self.current_hands: Dict[int, Dict[int, Card]] = {}
        self.current_hands_values: Dict[int, int] = {}

    def reset(self, budget: float = 0) -> None:
        """
        Resets player's params to their initial state.

        Parameters
        ----------
        budget: float
            Player's money
        """
        self.budget = budget
        self.current_hands = {}
        self.current_hands_values = {}

    def make_bet(self, bet: float) -> None:
        """
        Removes bet from player's budget.

        Attributes
        ----------
        bet: float
            Money to be subtracted.
        """
        self.budget -= bet

    def receive_reward(self, reward: float) -> None:
        """
        Adds reward to player's budget.

        Parameters
        ----------
        reward: float
            Money to be added.
        """
        self.budget += reward

    def update_hand(self, cards: Dict[int, Card], hand_id: int = 0) -> None:
        """
        Updates the hand with `hand_id` with the given `cards`.

        Parameters
        ----------
        cards: dict
            Cards to be set as new hand.
        hand_id: int
            ID of the hand to be updated.
        """
        self.current_hands[hand_id] = cards
        self._compute_hands_values()

    def _compute_hands_values(self) -> None:
        """Computes the indivual value of each player's hand."""
        self.current_hands_values = {hand_id: cards[0].value + cards[1].value for hand_id, cards in
                                     self.current_hands.items()}

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
        raise NotImplementedError("This method must be implemented in children classes")

    def get_insurance_action(self) -> Action:
        """
        Retrieves whether the player will make an insurance bet or not.

        Returns
        -------
        action_to_be_taken: blackjack.models.Action
        """
        raise NotImplementedError("This method must be implemented in children classes")
