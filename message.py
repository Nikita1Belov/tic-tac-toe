from configuration import *


class Message:
    """
    Message with a count
    """
    def __init__(self, surface, text):
        self.surface = surface
        self.text = text

    def draw(self):
        rectangle = pygame.Surface((WINDOW_WIDTH, MESSAGE_HEIGHT))
        rectangle.fill(PEACH_PUFF)
        self.surface.blit(rectangle, (0, 0))
        text_label = FONT_COMICS.render(self.text, 1, BLACK)
        self.surface.blit(text_label, (X - pygame.Surface.get_width(text_label)//2, Y_LABEL_1))


class LMessage(Message):
    """
    Messages after ending of the game
    """
    def __init__(self, surface, text, color_font, x, y, width, height):
        super().__init__(surface, text)
        self.surface = surface
        self.text = text
        self.color_font = color_font
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self):
        text_label = FONT_COMICS.render(self.text, 1, self.color_font)
        rectangle = pygame.Surface((pygame.Surface.get_width(text_label), self.height))
        rectangle.set_alpha(0)
        self.surface.blit(rectangle, (X - pygame.Surface.get_width(text_label)//2, self.y))
        self.surface.blit(text_label, (X - pygame.Surface.get_width(text_label)//2, self.y))


class SMessage(Message):
    """
    Messages after ending of the game
    """
    def __init__(self, surface, text, color_font, x, y, width, height):
        super().__init__(surface, text)
        self.surface = surface
        self.text = text
        self.color_font = color_font
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self):
        text_label = FONT_COMICS.render(self.text, 1, self.color_font)
        rectangle = pygame.Surface((self.width, self.height))
        rectangle.fill(WHITE)
        rectangle.set_alpha(120)
        self.surface.blit(rectangle, (self.x, self.y))
        self.surface.blit(text_label, (self.x, self.y))
