from cell import Cell
from gamefield import GameField
from configuration import *
from player import Player
from state import State
from statistics import Statistics
from ai import AIplayer


class Manager:
    """
    Managing of the game
    """
    n = 3
    cell_margin = 7.5
    cell_width = 190
    cell_height = cell_width
    stop = False

    def __init__(self, surface, n):
        self.surface = surface
        self.step = 0
        if n:
            self.cell_margin = 6
            self.n = n
            self.cell_width = (GAME_WIDTH - self.cell_margin * (self.n + 1)) / self.n
            self.cell_height = self.cell_width
        else:
            self.n = Manager.n
            self.cell_margin = Manager.cell_margin
            self.cell_width = Manager.cell_width
            self.cell_height = self.cell_height
        self.matrix = [[Cell.VOID] * self.n for i in range(self.n)]
        self.send_stat = True
        self.game_field = GameField(self.surface, self.cell_margin, self.cell_width, self.cell_height, self.n)

    def checker(self):
        win_player = None
        win_list_coordinates = []
        player_list = [Player.Player_1, Player.Player_2]

        for gamer in player_list:
            if gamer == Player.Player_1:
                sign = Cell.CROSS
                state = State.WIN_P1
            elif gamer == Player.Player_2:
                sign = Cell.ZERO
                state = State.WIN_P2

            for row in self.matrix:
                if row.count(sign) == self.n:
                    win_player = state
                    for i in range(self.n):
                        win_list_coordinates.append((self.matrix.index(row), i))
                    break

            buffer = []
            for col in range(self.n):
                for i in range(self.n):
                    buffer.append(self.matrix[i][col])
                if buffer.count(sign) == self.n:
                    win_player = state
                    for i in range(self.n):
                        win_list_coordinates.append((i, self.matrix.index(self.matrix[col])))
                    break
                else:
                    buffer.clear()

            main_diagonal = []
            for i in range(self.n):
                main_diagonal.append(self.matrix[i][i])
            if main_diagonal.count(sign) == self.n:
                win_player = state
                for i in range(self.n):
                    win_list_coordinates.append((i, i))
                break
            else:
                main_diagonal.clear()

            side_diagonal = []
            for i in range(self.n):
                side_diagonal.append(self.matrix[i][self.n - i - 1])
            if side_diagonal.count(sign) == self.n:
                win_player = state
                for i in range(self.n):
                    win_list_coordinates.append((i, self.n - i - 1))
                break
            else:
                side_diagonal.clear()

        count = 0
        if win_player is None:
            for i in range(self.n):
                for j in range(self.n):
                    if self.matrix[i][j] == Cell.VOID:
                        count += 1
            if count == 0:
                win_list_coordinates = False
                win_player = State.DRAW

        return win_player, win_list_coordinates

    def handler(self, x, y):
        i = int(x // (self.cell_margin + self.cell_width))
        j = int((y - MESSAGE_HEIGHT) // (self.cell_margin + self.cell_height))
        if self.matrix[i][j] == Cell.VOID:
            if self.step % 2 == 0:
                self.matrix[i][j] = Cell.CROSS
            else:
                self.matrix[i][j] = Cell.ZERO
            self.step += 1

    def ai_round(self, i, j, ai_symbolic):
        self.matrix[i][j] = ai_symbolic
        self.step += 1

    @staticmethod
    def count(win_player):
        if win_player == State.WIN_P1:
            text = f"{Player.Player_1} won!"
        elif win_player == State.WIN_P2:
            text = f"{Player.Player_2} won!"
        elif win_player == State.DRAW:
            text = "It's a draw!"
        return text

    @staticmethod
    def send_statistics(win_player, n):
        Statistics.counter(win_player, n)

    def ai_mode(self):
        if Player.Player_1 == AI and self.step % 2 == 0:
            ai_player = Player.Player_1
            ai_symbloic = Cell.CROSS
            human_player = Player.Player_2
            human_symbolic = Cell.ZERO
            i, j = AIplayer.main_cycle(self.matrix, self.n, ai_player, human_player, ai_symbloic, human_symbolic)
            self.ai_round(i, j, ai_symbloic)
        elif Player.Player_2 == AI and self.step % 2 != 0:
            ai_player = Player.Player_2
            ai_symbloic = Cell.ZERO
            human_player = Player.Player_1
            human_symbolic = Cell.CROSS
            i, j = AIplayer.main_cycle(self.matrix, self.n, ai_player, human_player, ai_symbloic, human_symbolic)
            self.ai_round(i, j, ai_symbloic)

    def hover_check(self):
        x, y = pygame.mouse.get_pos()
        if MESSAGE_HEIGHT < y < WINDOW_HEIGHT - self.cell_margin and 0 < x < GAME_WIDTH - self.cell_margin:
            self.game_field.hover_check(x, y, self.matrix)

    def main_loop(self):
        self.game_field.draw()
        self.game_field.update(self.matrix)
        self.hover_check()
        win_player, win_list_coordinates = self.checker()
        if not win_list_coordinates and win_player is None:
            self.ai_mode()
        else:
            if self.send_stat:
                self.send_statistics(win_player, self.n)
                self.send_stat = False
            self.game_field.win_way(win_list_coordinates, win_player)
        if self.game_field.send_stop():
            self.game_field.stop_set()
            text = self.count(win_player)
            return text
