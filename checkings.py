from move import Move


def check_coordinates(c, r, board, figure):
    j = 0
    column = c
    row = r

    while j == 0:

        try:
            column = int(column)
            row = int(row)
            calculed = to_calc_num_inputs(column, row, figure)
            column = calculed[0]
            row = calculed[1]
        except ValueError:
            print('Only numeric values allowed!!!')
            column = -10
            row = -10

        if column < 8 and row < 8 and column > -9 and row > -9 and if_figure_equals(board, column, row, figure):

            return [column, row]
        else:
            print('Enter correct numeric values, it must be between 1 and 8:\n')
            print('Columns')
            column = input()
            print('Rows')
            row = input()


def is_out_of_bounds(step_plus_list, col, row):
    if step_plus_list[0] < 8 and step_plus_list[1] < 8 and step_plus_list[1] >= 0:
        col_after = step_plus_list[0]
        row_after = step_plus_list[1]
    else:
        print('Row cannot be negative')
        col_after = col
        row_after = row

    return [col_after, row_after]


def to_calc_num_inputs(c, r, figure):
    column = c
    row = r
    if column < 1 or row < 1:
        column = -10
        row = -10
        return [column, row]
    if figure == 'w':
        column = c * -1
        row = r - 1
    elif figure == 'b':
        column = c - 1
        row = r - 1
    return [column, row]


def if_a_move_was_made(board, figure, col_after, row_after, prev_figure, move: Move,
                       prev_col_after_and_num, prev_row_after_and_row_move, col, row, num, row_move, moves_input):
    if (figure == prev_figure and board[col_after][row_after] == ' ') or \
            ([prev_col_after_and_num, prev_row_after_and_row_move] != [col, row] and prev_figure == figure) or \
            (board[col_after - num][row_after + row_move] != ' ' and board[col_after][row_after] != ' ') or \
            (board[col_after][row_after] == ' ' and (
                    moves_input == 'lw' or moves_input == 'rw' or moves_input == 'rb' or moves_input == 'lb')):
        print('Incorrect move')
        move.set_moves_input('rb')
        move.set_to_eat('')


def if_figure_equals(board, c, r, figure):
    if board[c][r] != figure:
        print('The box is either empty or has the wrong figure')
        return False
    else:
        return True


"""
    Функция для проверки вводимых символов

"""


def check_char_inputs(fk, f):
    figure = fk
    j = 0
    while j == 0:

        if (figure == 'w' or figure == 'b') and f == 'figure':
            return figure
        elif (
                figure == 'l' or figure == 'r' or figure == 'rb' or figure == 'lb' or figure == 'lw' or figure == 'rw') and f == 'move':
            return figure
        else:
            if f == 'figure':
                print('Choose "w" or "b" figure')
            elif f == 'move':
                print('Choose "r" or "l" or "rb" or "lb" or "lw" or "rw"')
            figure = input()
