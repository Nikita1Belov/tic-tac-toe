import pygame


from configuration import *
from player import Player


class Text:
    """
    Text from keyboard (player's names)
    """
    def __init__(self, surface, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.message = ""
        self.surface = surface
        self.name = ""

    def enter(self, event):
        if event.key == pygame.K_BACKSPACE:
            self.name = self.name[0:-1]
        else:
            self.name += event.unicode

    def handle_click(self):
        Player.add(self.name)
        self.name = ""

    def handle_click_ai(self, state):
        Player.add_ai(self.name, state)
        self.name = ""

    def draw(self):
        pygame.draw.rect(self.surface, BLACK,
                         (self.x, self.y, self.width, self.height), 3)
        if len(self.name) > 0:
            self.surface.blit(FONT_COMICS.render(self.name, 1, WHITE), (self.x+3, self.y-3))


class NumberText:
    """
    Text from keyboard (player's names)
    """
    number = 0

    def __init__(self, surface, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.message = ""
        self.surface = surface
        self.text_number = ""

    def enter(self, event):
        for obj in KEY_OBJ:
            if event.key == obj:
                self.text_number += event.unicode
                self.write_size(self.text_number)
            elif event.key == pygame.K_BACKSPACE:
                self.text_number = self.text_number[0:-1]
                self.write_size(self.text_number)

    def draw(self):
        pygame.draw.rect(self.surface, BLACK,
                         (self.x, self.y, self.width, self.height), 3)
        if len(self.text_number) > 0:
            self.surface.blit(FONT_COMICS.render(self.text_number, 1, WHITE), (self.x+3, self.y-3))

    @classmethod
    def write_size(cls, text_number):
        if text_number:
            text_number = int(text_number)
        if text_number == 1 or text_number == 0:
            text_number = 3
        cls.number = text_number

    @classmethod
    def send_size(cls):
        return cls.number
