from enum import Enum


class State(Enum):
    """
    State of game (the first player or the second player won and a draw)
    """
    WIN_P1 = 1
    WIN_P2 = 0
    DRAW = 2
