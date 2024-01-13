from cell import Cell
from configuration import *


class Player:
    """
    Information about players and their statistics
    """
    Player_1 = ""
    Player_2 = ""

    @classmethod
    def add(cls, players):
        if len(cls.Player_1) == 0 and len(cls.Player_2) == 0:
            if len(players) == 0:
                cls.Player_1 = "Player_1"
            else:
                cls.Player_1 = players
        elif len(cls.Player_1) > 0 and len(cls.Player_2) > 0:
            cls.Player_2 = ""
            if len(players) == 0:
                cls.Player_1 = "Player_1"
            else:
                cls.Player_1 = players
        else:
            if len(players) == 0:
                cls.Player_2 = "Player_2"
            else:
                cls.Player_2 = players

    @classmethod
    def add_ai(cls, players, state):
        if state == Cell.CROSS:
            if len(players) == 0:
                cls.Player_1 = "Player_1"
            else:
                cls.Player_1 = players
            cls.Player_2 = AI
        elif state == Cell.ZERO:
            if len(players) == 0:
                cls.Player_2 = "Player_2"
            else:
                cls.Player_2 = players
            cls.Player_1 = AI
