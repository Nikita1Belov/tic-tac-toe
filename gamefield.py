import pygame


from cell import Cell
from configuration import *
from state import State


class GameField:
    """
    Drawing and updating of the field
    """
    click = False

    def __init__(self, surface, margin, width, height, n):
        self.surface = surface
        self.stop = False
        self.rect = pygame.rect
        self.is_hovered = False
        self.cell_margin = margin
        self.cell_width = width
        self.cell_height = height
        self.n = n

    def draw(self):
        rectangle = pygame.Surface((self.cell_width * self.n + self.cell_height * (self.n + 1),
                                    self.cell_width * self.n + self.cell_margin * (self.n + 1)))
        rectangle.fill(ROYAL_BLUE)
        self.surface.blit(rectangle, (0, MESSAGE_HEIGHT))
        cell = pygame.Surface((self.cell_width, self.cell_height))
        cell.fill(BLACK)
        for i in range(self.n):
            for j in range(self.n):
                x = i * self.cell_width + (i + 1) * self.cell_margin
                y = j * self.cell_height + (j + 1) * self.cell_margin + MESSAGE_HEIGHT
                self.surface.blit(cell, (x, y))
        self.click_set(True)

    def update(self, matrix):
        for i in range(self.n):
            for j in range(self.n):
                x = i * self.cell_width + (i + 1) * self.cell_margin
                y = j * self.cell_height + (j + 1) * self.cell_margin + MESSAGE_HEIGHT
                if matrix[i][j] == Cell.CROSS:
                    pygame.draw.line(self.surface, BLUE, (x + self.cell_margin, y + self.cell_margin),
                                     (x + self.cell_width - self.cell_margin, y + self.cell_height - self.cell_margin),
                                     14)
                    pygame.draw.line(self.surface, BLUE, (x + self.cell_width - self.cell_margin, y + self.cell_margin),
                                     (x + self.cell_margin, y + self.cell_height - self.cell_margin), 14)
                elif matrix[i][j] == Cell.ZERO:
                    pygame.draw.circle(self.surface, YELLOW, (x + self.cell_width // 2, y + self.cell_height // 2),
                                       self.cell_height // 2 - self.cell_margin, 16)

    def hover_check(self, x, y, matrix):
        i = int(x // (self.cell_margin + self.cell_width))
        j = int((y - MESSAGE_HEIGHT) // (self.cell_margin + self.cell_height))
        cell = pygame.Surface((self.cell_width, self.cell_height))
        cell.fill(GRAY)
        ix = i * self.cell_width + (i + 1) * self.cell_margin
        jy = j * self.cell_width + j * self.cell_margin + self.cell_margin + MESSAGE_HEIGHT
        if matrix[i][j] == Cell.VOID:
            self.surface.blit(cell, (ix, jy))

    def win_way(self, list_coordinates, player):
        if list_coordinates:
            for i in range(self.n):
                cell = pygame.Surface((self.cell_width, self.cell_height))
                cell.fill(WHITE)
                x = list_coordinates[i][0] * self.cell_width + (list_coordinates[i][0] + 1) * self.cell_margin
                y = list_coordinates[i][1] * self.cell_width + \
                    list_coordinates[i][1] * self.cell_margin + self.cell_margin + MESSAGE_HEIGHT
                self.surface.blit(cell, (x, y))
                if player == State.WIN_P1:
                    pygame.draw.line(self.surface, GREEN, (x + self.cell_margin, y + self.cell_margin),
                                     (x + self.cell_width - self.cell_margin, y + self.cell_height - self.cell_margin),
                                     14)
                    pygame.draw.line(self.surface, GREEN, (x + self.cell_width - self.cell_margin, y + self.cell_margin),
                                     (x + self.cell_margin, y + self.cell_height - self.cell_margin), 14)
                elif player == State.WIN_P2:
                    pygame.draw.circle(self.surface, GREEN, (x + self.cell_width // 2, y + self.cell_height // 2),
                                       self.cell_height // 2 - self.cell_margin, 16)
        else:
            pass
        self.stop = True
        self.click_set(False)

    def send_stop(self):
        return self.stop

    def stop_set(self):
        self.stop = False

    @classmethod
    def click_set(cls, value):
        cls.click = value

    @classmethod
    def send_click(cls):
        return cls.click
