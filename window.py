import threading
import pygame


from pygame import QUIT
from gamefield import GameField
from menu import Menu, Menu2call
from label import Label
from statistics import Statistics
from textfield import Text, NumberText
from cell import Cell
from player import Player
from message import Message, LMessage, SMessage
from manager import Manager
from configuration import *
from effects import fade_to_black


class Window:
    """
    Global window with game field and message
    """
    def __init__(self):
        self.over = False
        self.fps = FPS
        pygame.init()
        pygame.font.init()
        pygame.mixer.music.load(MUSIC_WAY)
        pygame.mixer.music.set_volume(0.1)
        self.clock = pygame.time.Clock()
        self.surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.background_image = pygame.image.load(BACKGROUND_IMAGE)
        self.object_list = []
        self.hover_object_list = []
        self.text_object_list = []
        self.main_loop_object = []
        self.fade = []
        self.text_result = None
        self.manager = None
        self.ending = False
        self.fade = False
        self.text = Text(self.surface, X_BUTTON, Y_BUTTON_1, WIDTH_1, HEIGHT_T)
        self.create_menu_start_1()
        pygame.mixer.music.play(loops=-1)

    def create_menu_start_1(self):
        self.fade = True
        self.cleaner()

        button_friend = Menu(self.surface, X_BUTTON, Y_BUTTON_1, WIDTH_1, HEIGHT,
                             "game with friend", IMAGE_PATH_BUTTON_BLUE,
                             HOVER_IMAGE_PATH_BUTTON_BLUE,
                             lambda: self.create_menu_start_2())
        button_ai = Menu(self.surface, X_BUTTON, Y_BUTTON_2, WIDTH_1, HEIGHT,
                         "game with AI", IMAGE_PATH_BUTTON_BLUE,
                         HOVER_IMAGE_PATH_BUTTON_BLUE,
                         lambda: self.create_menu_start_4())
        button_mode = Menu(self.surface, X_BUTTON, Y_BUTTON_3, WIDTH_1, HEIGHT,
                           "difficult mode", IMAGE_PATH_BUTTON_BLUE,
                           HOVER_IMAGE_PATH_BUTTON_BLUE,
                           lambda: self.difficult_mode())
        button_quit = Menu(self.surface, X_BUTTON, Y_BUTTON_4, WIDTH_1, HEIGHT,
                           "quit", IMAGE_PATH_BUTTON_BLUE,
                           HOVER_IMAGE_PATH_BUTTON_BLUE,
                           quit)

        mass_obj = [button_friend, button_ai, button_mode, button_quit]
        mass_hover = [button_friend, button_ai, button_mode, button_quit]

        for elem in mass_obj:
            self.object_list.append(elem)
        for elem in mass_hover:
            self.hover_object_list.append(elem)

    def difficult_mode(self):
        self.fade = True
        self.cleaner()

        text_label_mode = Label(self.surface, "Write a size:", X_LABEL, Y_LABEL_1, BLACK)
        text_label_mode_2 = Label(self.surface, "(a size from 4 to 10)", X_BUTTON, Y_BUTTON_1, BLACK)
        text_enter_number = NumberText(self.surface, X_BUTTON, Y_BUTTON_2, WIDTH_1, HEIGHT_T)
        button_friend = Menu(self.surface, X_BUTTON, Y_BUTTON_3, WIDTH_1, HEIGHT,
                             "game with friend", IMAGE_PATH_BUTTON_BLUE,
                             HOVER_IMAGE_PATH_BUTTON_BLUE,
                             lambda: self.create_menu_start_2())
        button_back = Menu(self.surface, X_BUTTON, Y_BUTTON_4, WIDTH_1, HEIGHT,
                           "back", IMAGE_PATH_BUTTON_BLUE,
                           HOVER_IMAGE_PATH_BUTTON_BLUE,
                           lambda: self.create_menu_start_1())

        mass_obj = [text_label_mode, text_label_mode_2, text_enter_number, button_friend, button_back]
        mass_hover = [button_friend, button_back]
        mass_text = [text_enter_number]

        for elem in mass_obj:
            self.object_list.append(elem)
        for elem in mass_hover:
            self.hover_object_list.append(elem)
        for elem in mass_text:
            self.text_object_list.append(elem)

    def create_menu_start_2(self):
        self.fade = True
        self.cleaner()

        text_label_1 = Label(self.surface, "Who'll play X?", X_LABEL, Y_LABEL_1, BLACK)
        text_enter_name_1 = self.text
        button_start_1 = Menu2call(self.surface, X_BUTTON, Y_BUTTON_2, WIDTH_1, HEIGHT,
                                   "start!", IMAGE_PATH_BUTTON_RED,
                                   HOVER_IMAGE_PATH_BUTTON_RED,
                                   lambda: text_enter_name_1.handle_click(),
                                   lambda: self.create_menu_start_3())
        button_back = Menu(self.surface, X_BUTTON, Y_BUTTON_3, WIDTH_1, HEIGHT,
                           "back", IMAGE_PATH_BUTTON_BLUE,
                           HOVER_IMAGE_PATH_BUTTON_BLUE,
                           lambda: self.create_menu_start_1())

        mass_obj = [text_label_1, text_enter_name_1, button_start_1, button_back]
        mass_hover = [button_start_1, button_back]
        mass_text = [text_enter_name_1]

        for elem in mass_obj:
            self.object_list.append(elem)
        for elem in mass_hover:
            self.hover_object_list.append(elem)
        for elem in mass_text:
            self.text_object_list.append(elem)

    def create_menu_start_3(self):
        self.fade = True
        self.cleaner()

        text_label_2 = Label(self.surface, "Who'll play O?", X_LABEL, Y_LABEL_1, BLACK)
        text_enter_name_2 = self.text
        button_start_2 = Menu2call(self.surface, X_BUTTON, Y_BUTTON_2, WIDTH_1, HEIGHT,
                                   "start!", IMAGE_PATH_BUTTON_GREEN,
                                   HOVER_IMAGE_PATH_BUTTON_GREEN,
                                   lambda: text_enter_name_2.handle_click(),
                                   lambda: self.create_field())

        mass_obj = [text_label_2, text_enter_name_2, button_start_2]
        mass_hover = [button_start_2]
        mass_text = [text_enter_name_2]

        for elem in mass_obj:
            self.object_list.append(elem)
        for elem in mass_hover:
            self.hover_object_list.append(elem)
        for elem in mass_text:
            self.text_object_list.append(elem)

    def create_menu_start_4(self):
        self.fade = True
        self.cleaner()

        text_label_3 = Label(self.surface, "Enter your name", X_LABEL, Y_LABEL_1, BLACK)
        text_enter_name_3 = self.text
        button_start_x = Menu2call(self.surface, X_BUTTON_COUPLE_1, Y_BUTTON_2, WIDTH_3, HEIGHT_2,
                                   "play X", IMAGE_PATH_BUTTON_YELLOW,
                                   HOVER_IMAGE_PATH_BUTTON_YELLOW,
                                   lambda: text_enter_name_3.handle_click_ai(Cell.CROSS),
                                   lambda: self.create_field())
        button_start_o = Menu2call(self.surface, X_BUTTON_COUPLE_2, Y_BUTTON_2, WIDTH_3, HEIGHT_2,
                                   "play O", IMAGE_PATH_BUTTON_YELLOW,
                                   HOVER_IMAGE_PATH_BUTTON_YELLOW,
                                   lambda: text_enter_name_3.handle_click_ai(Cell.ZERO),
                                   lambda: self.create_field())
        button_back = Menu(self.surface, X_BUTTON, Y_BUTTON_3, WIDTH_1, HEIGHT,
                           "back", IMAGE_PATH_BUTTON_BLUE,
                           HOVER_IMAGE_PATH_BUTTON_BLUE,
                           lambda: self.create_menu_start_1())

        mass_obj = [text_label_3, text_enter_name_3, button_start_x, button_start_o, button_back]
        mass_hover = [button_start_x, button_start_o, button_back]
        mass_text = [text_enter_name_3]

        for elem in mass_obj:
            self.object_list.append(elem)
        for elem in mass_hover:
            self.hover_object_list.append(elem)
        for elem in mass_text:
            self.text_object_list.append(elem)

    def create_field(self):
        self.cleaner()
        self.ending = True
        result = Statistics.send_count()
        text = f"{Player.Player_1} {result[0]} : {result[1]} {Player.Player_2}"
        message = Message(self.surface, text)
        self.object_list.append(message)
        if 4 <= NumberText.send_size() <= 10:
            size = NumberText.send_size()
        else:
            size = None
        self.manager = Manager(self.surface, size)
        self.main_loop_object.append(self.manager)

    def create_menu_end(self):
        self.cleaner()

        result = Statistics.send_count()
        text_label_result = LMessage(self.surface, self.text_result, WHITE, Y_LABEL_1, WIDTH_1, HEIGHT)
        text_result = f"{Player.Player_1} {result[0]} : {result[1]} {Player.Player_2}"
        text_label_count = LMessage(self.surface, text_result, WHITE, Y_BUTTON_1, WIDTH_1, HEIGHT)

        button_new_game = Menu(self.surface, X_BUTTON, Y_BUTTON_2, WIDTH_1, HEIGHT,
                               "play a new game", IMAGE_PATH_BUTTON_BLUE,
                               HOVER_IMAGE_PATH_BUTTON_BLUE,
                               lambda: self.create_field())
        button_change = Menu2call(self.surface, X_BUTTON, Y_BUTTON_3, WIDTH_1, HEIGHT,
                                  "change a player", IMAGE_PATH_BUTTON_BLUE,
                                  HOVER_IMAGE_PATH_BUTTON_BLUE,
                                  lambda: self.create_menu_start_1(),
                                  lambda: Statistics.reset())
        button_set = Menu(self.surface, X_BUTTON, Y_BUTTON_4, WIDTH_1, HEIGHT,
                          "settings", IMAGE_PATH_BUTTON_BLUE,
                          HOVER_IMAGE_PATH_BUTTON_BLUE,
                          lambda: self.settings())
        button_quit = Menu(self.surface, X_BUTTON, Y_BUTTON_5, WIDTH_1, HEIGHT,
                           "quit", IMAGE_PATH_BUTTON_BLUE,
                           HOVER_IMAGE_PATH_BUTTON_BLUE,
                           quit)

        mass_obj = [text_label_result, text_label_count, button_new_game, button_change, button_set, button_quit]
        mass_hover = [button_new_game, button_change, button_set, button_quit]

        for elem in mass_obj:
            self.object_list.append(elem)
        for elem in mass_hover:
            self.hover_object_list.append(elem)

    def settings(self):
        self.fade = True
        self.cleaner()

        button_sound_on = Menu(self.surface, X_BUTTON, Y_BUTTON_1, WIDTH_1, HEIGHT,
                               "sound on", IMAGE_PATH_BUTTON_BLUE,
                               HOVER_IMAGE_PATH_BUTTON_BLUE,
                               lambda: pygame.mixer.music.play(loops=-1))
        button_sound_off = Menu(self.surface, X_BUTTON, Y_BUTTON_2, WIDTH_1, HEIGHT,
                                "sound off", IMAGE_PATH_BUTTON_BLUE,
                                HOVER_IMAGE_PATH_BUTTON_BLUE,
                                lambda: pygame.mixer.music.stop())
        button_set = Menu(self.surface, X_BUTTON, Y_BUTTON_3, WIDTH_1, HEIGHT,
                          "statistics", IMAGE_PATH_BUTTON_BLUE,
                          HOVER_IMAGE_PATH_BUTTON_BLUE,
                          lambda: self.statistics())
        button_back = Menu(self.surface, X_BUTTON, Y_BUTTON_4, WIDTH_1, HEIGHT,
                           "back", IMAGE_PATH_BUTTON_BLUE,
                           HOVER_IMAGE_PATH_BUTTON_BLUE,
                           lambda: self.create_menu_end())

        mass_obj = [button_sound_on, button_sound_off, button_set, button_back]
        mass_hover = [button_sound_on, button_sound_off, button_set, button_back]

        for elem in mass_obj:
            self.object_list.append(elem)
        for elem in mass_hover:
            self.hover_object_list.append(elem)

    def statistics(self):
        self.fade = True
        self.cleaner()

        title = "Top 10 players"
        text_label_stat = LMessage(self.surface, title, WHITE, Y_LABEL_1, WIDTH_1, HEIGHT)
        button_all = Menu(self.surface, X-200, Y_BUTTON_1, WIDTH_TOP, HEIGHT,
                          "all", IMAGE_PATH_BUTTON_YELLOW,
                          HOVER_IMAGE_PATH_BUTTON_YELLOW,
                          lambda: self.top_list("all"))
        button_3 = Menu(self.surface, X-50, Y_BUTTON_1, WIDTH_TOP, HEIGHT,
                        "3x3", IMAGE_PATH_BUTTON_YELLOW,
                        HOVER_IMAGE_PATH_BUTTON_YELLOW,
                        lambda: self.top_list("3x3"))
        button_4 = Menu(self.surface, X+100, Y_BUTTON_1, WIDTH_TOP, HEIGHT,
                        "4x4", IMAGE_PATH_BUTTON_YELLOW,
                        HOVER_IMAGE_PATH_BUTTON_YELLOW,
                        lambda: self.top_list("4x4"))
        button_5 = Menu(self.surface, X-200, Y_BUTTON_2, WIDTH_TOP, HEIGHT,
                        "5x5", IMAGE_PATH_BUTTON_YELLOW,
                        HOVER_IMAGE_PATH_BUTTON_YELLOW,
                        lambda: self.top_list("5x5"))
        button_6 = Menu(self.surface, X-50, Y_BUTTON_2, WIDTH_TOP, HEIGHT,
                        "6x6", IMAGE_PATH_BUTTON_YELLOW,
                        HOVER_IMAGE_PATH_BUTTON_YELLOW,
                        lambda: self.top_list("6x6"))
        button_7 = Menu(self.surface, X+100, Y_BUTTON_2, WIDTH_TOP, HEIGHT,
                        "7x7", IMAGE_PATH_BUTTON_YELLOW,
                        HOVER_IMAGE_PATH_BUTTON_YELLOW,
                        lambda: self.top_list("7x7"))
        button_8 = Menu(self.surface, X-200, Y_BUTTON_3, WIDTH_TOP, HEIGHT,
                        "8x8", IMAGE_PATH_BUTTON_YELLOW,
                        HOVER_IMAGE_PATH_BUTTON_YELLOW,
                        lambda: self.top_list("8x8"))
        button_9 = Menu(self.surface, X-50, Y_BUTTON_3, WIDTH_TOP, HEIGHT,
                        "9x9", IMAGE_PATH_BUTTON_YELLOW,
                        HOVER_IMAGE_PATH_BUTTON_YELLOW,
                        lambda: self.top_list("9x9"))
        button_10 = Menu(self.surface, X+100, Y_BUTTON_3, WIDTH_TOP, HEIGHT,
                         "10x10", IMAGE_PATH_BUTTON_YELLOW,
                         HOVER_IMAGE_PATH_BUTTON_YELLOW,
                         lambda: self.top_list("10x10"))
        button_back = Menu(self.surface, X_BUTTON, Y_BUTTON_4, WIDTH_1, HEIGHT,
                           "back", IMAGE_PATH_BUTTON_YELLOW,
                           HOVER_IMAGE_PATH_BUTTON_YELLOW,
                           lambda: self.settings())

        mass_obj = [text_label_stat, button_all, button_3, button_4, button_5, button_6,
                    button_7, button_8, button_9, button_10, button_back]
        mass_hover = [button_all, button_3, button_4, button_5, button_6,
                      button_7, button_8, button_9, button_10, button_back]

        for elem in mass_obj:
            self.object_list.append(elem)
        for elem in mass_hover:
            self.hover_object_list.append(elem)

    def top_list(self, mark):
        self.fade = True
        self.cleaner()

        x = 0
        y = 0

        title = "Top 10 " + mark + " players"
        text_label_stat = LMessage(self.surface, title, WHITE, Y_LABEL_1, WIDTH_1, HEIGHT)
        self.object_list.append(text_label_stat)
        data = Statistics.reader(mark)
        if len(data) > 1:
            key_t = "Player"
            text_label_stat_title = \
                key_t + "---" + str(data[key_t][0]) + "---" + str(data[key_t][1]) + "---" + str(data[key_t][2])
            text_label_title = LMessage(self.surface, text_label_stat_title,
                                        BLACK, Y_BUTTON_1 + y, WIDTH_1, HEIGHT)
            self.object_list.append(text_label_title)
            data.pop(key_t)

            data = dict(sorted(data.items(), key=lambda item: item[1][0], reverse=True))
            for key in data:
                if x < 10:
                    text = key + "---" + str(data[key][0]) + "---" + str(data[key][1]) + "---" + str(data[key][2])
                    text_label_stat = SMessage(self.surface, text, BLACK, X_LABEL_STAT, Y_STAT+y, WIDTH_ML, HEIGHT)
                    self.object_list.append(text_label_stat)
                    y += 50
                    x += 1
        else:
            text = "Nothing is here!"
            text_label_stat = Label(self.surface, text, X_LABEL, Y_BUTTON_1, ORANGE)
            self.object_list.append(text_label_stat)

        button_back_2 = Menu(self.surface, X_BUTTON, Y_BUTTON_6, WIDTH_1, HEIGHT,
                             "back", IMAGE_PATH_BUTTON_BLUE,
                             HOVER_IMAGE_PATH_BUTTON_BLUE,
                             lambda: self.statistics())

        self.object_list.append(button_back_2)
        self.hover_object_list.append(button_back_2)

    def cleaner(self):
        mass = [self.object_list, self.hover_object_list, self.text_object_list, self.main_loop_object]
        for elem in mass:
            elem.clear()

    def event(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.over = True
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i in self.hover_object_list:
                    i.handle_click()
                if self.main_loop_object and GameField.send_click():
                    x, y = pygame.mouse.get_pos()
                    self.manager.handler(x, y)
            elif event.type == pygame.KEYDOWN:
                for d in self.text_object_list:
                    d.enter(event)

    def draw(self):
        for o in self.object_list:
            o.draw()
        if self.fade:
            fade_to_black(self.surface)
            self.fade = False

    def hover_check(self):
        for h in self.hover_object_list:
            h.hover_check(pygame.mouse.get_pos())

    def main_loop(self):
        for elem in self.main_loop_object:
            self.text_result = elem.main_loop()
            if self.text_result and self.ending:
                self.ending = False
                t_1 = threading.Timer(2.5, self.create_menu_end)
                t_1.start()

    def run(self):
        while not self.over:
            self.surface.blit(self.background_image, (0, 0))
            self.draw()
            self.event()
            self.hover_check()
            self.main_loop()
            pygame.display.flip()
            self.clock.tick(self.fps)


def main():
    window = Window()
    window.run()


if __name__ == "__main__":
    main()
