from colorama import init, Fore


class Card:
    """
    Models a card.

    Attributes
    ----------
    rank: str
        Card number or letter.
    suit: str
        Either "clubs", "diamonds", "hearts" or "spades"
    icon: str
        Unicode symbol representing card's suit.
    value: int
        Value of the card in a BlackJack game.
    suit_to_icon: dict
        Suit name to icon symbol mapping dict.
    rank_to_value: dict
        Rank to value mapping dict.
    """
    def __init__(self, rank: str, suit: str) -> None:
        """
        Parameters
        ----------
        rank: str
            Card number or letter.
        suit: str
            Either "clubs", "diamonds", "hearts" or "spades"
        """

        self.rank = rank
        self.suit = suit

        self.suit_to_icon = {"clubs": "\u2663", "diamonds": "\u2666", "hearts": "\u2665", "spades": "\u2660"}
        self.rank_to_value = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10,
                              "Q": 10, "K": 10, "A": 11}

        if rank not in self.rank_to_value:
            raise ValueError(f"Invalid rank {rank}")
        if suit not in self.suit_to_icon:
            raise ValueError(f"Invalid suit {suit}")

        self.rank = rank
        self.suit = suit
        self.value = self.rank_to_value[self.rank]
        self.icon = self.suit_to_icon[self.suit]

    def to_string(self) -> str:
        """
        Generates a colored string with card's rank + suite's symbol.

        Returns
        -------
        colored_string: str
        """
        init(autoreset=True)

        if self.suit in {"diamonds", "hearts"}:
            color = Fore.RED
        else:
            color = Fore.BLUE

        return f"{self.rank}{color}{self.icon}{Fore.RESET}"

    def swap_ace_value(self) -> None:
        """
        If the card is an ace, it swaps it toggles its value between 1 and 11.

        Raises
        ------
        ValueError: if card is not and ace.
        """

        if self.rank == "1":
            self.rank = "A"
            self.value = 11

        elif self.rank == "A":
            self.rank = "1"
            self.value = 1
        else:
            raise ValueError("Only aces can swap values")
