import pygame


from configuration import *


def fade_to_black(surface):
    fade_level = 0
    go = True
    while go:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                go = False

        fade_lay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        fade_lay.fill(BLACK)
        fade_lay.set_alpha(fade_level)
        surface.blit(fade_lay, (0, 0))

        fade_level += 5
        if fade_level >= 120:
            fade_level = 255
            go = False

        pygame.display.flip()
