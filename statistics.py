import os

from player import Player
from state import State


class Statistics:
    """
    To read and write/rewrite statistics of the game and players
    """
    count_player_1 = 0
    count_player_2 = count_player_1
    draw = 0
    result_count = (count_player_1, count_player_2)
    win_player = None
    size = {3: "3x3", 4: "4x4", 5: "5x5", 6: "6x6", 7: "7x7", 8: "8x8", 9: "9x9", 10: "10x10"}

    @classmethod
    def counter(cls, win_player, n):
        if win_player == State.WIN_P1:
            cls.count_player_1 += 1
        elif win_player == State.WIN_P2:
            cls.count_player_2 += 1
        elif win_player == State.DRAW:
            cls.draw += 1
        cls.result_count = (cls.count_player_1, cls.count_player_2)
        cls.win_player = win_player
        result = {Player.Player_1: (cls.count_player_1, cls.draw, cls.count_player_2),
                  Player.Player_2: (cls.count_player_2, cls.draw, cls.count_player_1)}
        result_2 = {Player.Player_1: (cls.count_player_1, cls.draw, cls.count_player_2),
                    Player.Player_2: (cls.count_player_2, cls.draw, cls.count_player_1)}
        cls.writer_all(result)
        for key in cls.size:
            if n == key:
                mark = cls.size[key]
                cls.writer(mark, result_2)

    @classmethod
    def send_count(cls):
        return cls.result_count

    @classmethod
    def reset(cls):
        cls.count_player_1 = 0
        cls.count_player_2 = cls.count_player_1
        cls.draw = 0
        cls.result_count = (cls.count_player_1, cls.count_player_2)

    @classmethod
    def reader(cls, mark):
        data = {}
        file_name = "statistics" + mark + ".csv"
        if os.path.isfile(file_name):
            with open(file_name, "r") as file:
                for row in file:
                    row = row.strip()
                    player_f, win_f, draw_f, defeat_f = row.split(";")
                    data[player_f] = (win_f, draw_f, defeat_f)
        return data

    @classmethod
    def writer(cls, mark, result):
        file_name = "statistics" + mark + ".csv"
        title = "Player" + ";" + "Win" + ";" + "Draw" + ";" + "Defeat" + "\n"
        data = {}

        if os.path.isfile(file_name):
            pass
        else:
            open(file_name, "x")
        with open(file_name, "r") as file:
            if os.stat(file_name).st_size > 0:
                for row in file:
                    row = row.strip()
                    player_f, win_f, draw_f, defeat_f = row.split(";")
                    data[player_f] = (win_f, draw_f, defeat_f)
                for key_1 in list(data):
                    for key_2 in list(result):
                        if key_1 == key_2:
                            if cls.win_player == State.WIN_P1:
                                if key_2 == Player.Player_1:
                                    win = int(data[key_1][0]) + 1
                                    draw = int(data[key_1][1])
                                    defeat = int(data[key_1][2])
                                elif key_2 == Player.Player_2:
                                    win = int(data[key_1][0])
                                    draw = int(data[key_1][1])
                                    defeat = int(data[key_1][2]) + 1
                            elif cls.win_player == State.DRAW:
                                win = int(data[key_1][0])
                                draw = int(data[key_1][1]) + 1
                                defeat = int(data[key_1][2])
                            elif cls.win_player == State.WIN_P2:
                                if key_2 == Player.Player_1:
                                    win = int(data[key_1][0])
                                    draw = int(data[key_1][1])
                                    defeat = int(data[key_1][2]) + 1
                                elif key_2 == Player.Player_2:
                                    win = int(data[key_1][0]) + 1
                                    draw = int(data[key_1][1])
                                    defeat = int(data[key_1][2])
                            data[key_1] = (str(win), str(draw), str(defeat))
                            result.pop(key_2)
                if len(result) > 0:
                    for key in result:
                        data[key] = (str(result[key][0]), str(result[key][1]), str(result[key][2]))
                with open(file_name, "w") as file:
                    for key in data:
                        buffer_str_1 = key + ";" + str(data[key][0]) + ";" + str(data[key][1]) + ";" \
                                       + data[key][2] + "\n"
                        file.write(buffer_str_1)
            else:
                with open(file_name, "w") as file:
                    file.write(title)
                    for key in result:
                        buffer_str_2 = key + ";" + str(result[key][0]) + ";" \
                                       + str(result[key][1]) + ";" + str(result[key][2]) + "\n"
                        file.write(buffer_str_2)

    @classmethod
    def writer_all(cls, result):
        file_name = "statisticsall.csv"
        title = "Player" + ";" + "Win" + ";" + "Draw" + ";" + "Defeat" + "\n"
        data = {}

        if os.path.isfile(file_name):
            pass
        else:
            open(file_name, "x")
        with open(file_name, "r") as file:
            if os.stat(file_name).st_size > 0:
                for row in file:
                    row = row.strip()
                    player_f, win_f, draw_f, defeat_f = row.split(";")
                    data[player_f] = (win_f, draw_f, defeat_f)
                for key_1 in list(data):
                    for key_2 in list(result):
                        if key_1 == key_2:
                            if cls.win_player == State.WIN_P1:
                                if key_2 == Player.Player_1:
                                    win = int(data[key_1][0]) + 1
                                    draw = int(data[key_1][1])
                                    defeat = int(data[key_1][2])
                                elif key_2 == Player.Player_2:
                                    win = int(data[key_1][0])
                                    draw = int(data[key_1][1])
                                    defeat = int(data[key_1][2]) + 1
                            elif cls.win_player == State.DRAW:
                                win = int(data[key_1][0])
                                draw = int(data[key_1][1]) + 1
                                defeat = int(data[key_1][2])
                            elif cls.win_player == State.WIN_P2:
                                if key_2 == Player.Player_1:
                                    win = int(data[key_1][0])
                                    draw = int(data[key_1][1])
                                    defeat = int(data[key_1][2]) + 1
                                elif key_2 == Player.Player_2:
                                    win = int(data[key_1][0]) + 1
                                    draw = int(data[key_1][1])
                                    defeat = int(data[key_1][2])
                            data[key_1] = (str(win), str(draw), str(defeat))
                            result.pop(key_2)
                if len(result) > 0:
                    for key in result:
                        data[key] = (str(result[key][0]), str(result[key][1]), str(result[key][2]))
                with open(file_name, "w") as file:
                    for key in data:
                        buffer_str_1 = key + ";" + str(data[key][0]) + ";" + str(data[key][1]) + ";" \
                                       + data[key][2] + "\n"
                        file.write(buffer_str_1)
            else:
                with open(file_name, "w") as file:
                    file.write(title)
                    for key in result:
                        buffer_str_2 = key + ";" + str(result[key][0]) + ";" \
                                       + str(result[key][1]) + ";" + str(result[key][2]) + "\n"
                        file.write(buffer_str_2)
