from configuration import *


class Label:
    """
    Labels
    """
    def __init__(self, surface, text, x, y, color):
        self.surface = surface
        self.text = text
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        text_label = FONT_COMICS.render(self.text, 1, self.color)
        self.surface.blit(text_label, (self.x, self.y))
