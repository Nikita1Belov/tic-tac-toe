import sys


from cell import Cell


class AIplayer:
    """
    "AI-player"
    """

    @classmethod
    def minimax_checker(cls, matrix_minimax, n, ai_symbolic, human_symbolic):
        symbolic = [ai_symbolic, human_symbolic]
        result = None

        for sign in symbolic:
            if sign == ai_symbolic:
                state = 10
            elif sign == human_symbolic:
                state = -10

            for row in matrix_minimax:
                if row.count(sign) == n:
                    result = state

            buffer = []
            for col in range(n):
                for i in range(n):
                    buffer.append(matrix_minimax[i][col])
                if buffer.count(sign) == n:
                    result = state
                else:
                    buffer.clear()

            main_diagonal = []
            for i in range(n):
                main_diagonal.append(matrix_minimax[i][i])
            if main_diagonal.count(sign) == n:
                result = state

            side_diagonal = []
            for i in range(n):
                side_diagonal.append(matrix_minimax[i][n - i - 1])
            if side_diagonal.count(sign) == n:
                result = state

        count = 0
        for i in range(n):
            for j in range(n):
                if matrix_minimax[i][j] == Cell.VOID:
                    count += 1
        if count == 0:
            result = 0

        return result

    @classmethod
    def minimax(cls, weight, matrix_minimax, n, ai_player, human_player, ai_symbolic, human_symbolic, a, b):
        maxc = True
        minc = False

        if cls.minimax_checker(matrix_minimax, n, ai_symbolic, human_symbolic) == 10:
            return 10
        elif cls.minimax_checker(matrix_minimax, n, ai_symbolic, human_symbolic) == -10:
            return -10
        elif cls.minimax_checker(matrix_minimax, n, ai_symbolic, human_symbolic) == 0:
            return 0
        else:
            if weight == maxc:
                best_count_minimax = -sys.maxsize
                for i in range(n):
                    for j in range(n):
                        if matrix_minimax[i][j] == Cell.VOID:
                            matrix_minimax[i][j] = ai_symbolic
                            count = cls.minimax(minc, matrix_minimax, n, ai_player, human_player,
                                                ai_symbolic, human_symbolic, a, b)
                            matrix_minimax[i][j] = Cell.VOID
                            best_count_minimax = max(best_count_minimax, count)
                            a = max(best_count_minimax, a)
                            if b <= a:
                                break
                return best_count_minimax
            else:
                best_count_minimax = sys.maxsize
                for i in range(n):
                    for j in range(n):
                        if matrix_minimax[i][j] == Cell.VOID:
                            matrix_minimax[i][j] = human_symbolic
                            count = cls.minimax(maxc, matrix_minimax, n, ai_player,
                                                human_player, ai_symbolic, human_symbolic, a, b)
                            matrix_minimax[i][j] = Cell.VOID
                            best_count_minimax = min(best_count_minimax, count)
                            b = min(b, best_count_minimax)
                            if b <= a:
                                break
                return best_count_minimax

    @classmethod
    def main_cycle(cls, local_matrix, n, ai_player, human_player, ai_symbolic, human_symbolic):
        best_count = -sys.maxsize
        minc = False
        a = -sys.maxsize
        b = sys.maxsize

        for i in range(n):
            for j in range(n):
                if local_matrix[i][j] == Cell.VOID:
                    local_matrix[i][j] = ai_symbolic
                    count_main = cls.minimax(minc, local_matrix, n, ai_player,
                                             human_player, ai_symbolic, human_symbolic, a, b)
                    local_matrix[i][j] = Cell.VOID
                    if count_main > best_count:
                        best_count = count_main
                        coordinates = i, j
                    elif count_main == best_count and i == 1 and j == 1:
                        coordinates = i, j
        return coordinates
