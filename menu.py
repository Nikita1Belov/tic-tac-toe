import pygame

from configuration import *


class Menu:
    """
    Game menu buttons
    """
    def __init__(self, surface, x, y, width, height, text, hover_image, hover_image_path, call):
        self.surface = surface
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.call = call

        self.image = pygame.image.load(hover_image)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.hover_image = self.image

        if hover_image_path:
            self.hover_image = pygame.image.load(hover_image_path)
            self.hover_image = pygame.transform.scale(self.hover_image, (width, height))

        self.rect = self.image.get_rect(topleft=(x, y))
        self.is_hovered = False

    def draw(self):
        if self.is_hovered:
            current_image = self.hover_image
        else:
            current_image = self.image
        self.surface.blit(current_image, self.rect.topleft)
        text_surface = FONT_BUTTON.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        self.surface.blit(text_surface, text_rect)

    def hover_check(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def handle_click(self):
        if self.is_hovered:
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))
            self.call()


class Menu2call(Menu):
    def __init__(self, surface, x, y, width, height, text, hover_image, hover_image_path, call, call_2):
        super().__init__(surface, x, y, width, height, text, hover_image, hover_image_path, call)
        self.call_2 = call_2

    def handle_click(self):
        if self.is_hovered:
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))
            self.call()
            self.call_2()
