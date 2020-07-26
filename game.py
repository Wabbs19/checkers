from move import Move


def set_num(figure, pos_or_neg_value, moves_input) -> int:

    if figure == 'w' and not (moves_input == 'lw' or moves_input == 'rw') or moves_input == 'rb' or moves_input == 'lb':
        num = pos_or_neg_value[0]
    else:
        num = pos_or_neg_value[1]

    return num


def setting_to_eat_value_and_inversing_moves_input_value(move: Move, figure, moves_input):

    if figure == 'w':
        move.set_to_eat('b')
        if moves_input == 'lw':
            move.set_moves_input('rw')
        elif moves_input == 'rw':
            move.set_moves_input('lw')
    elif figure == 'b':
        move.set_to_eat('w')
        if moves_input == 'r':
            move.set_moves_input('l')
        elif moves_input == 'l':
            move.set_moves_input('r')


def step_plus(moves_input, col, row, num):

    if moves_input == 'r' or moves_input == 'rb' or moves_input == 'rw':
        col_after = col - num
        row_after = row + num
    elif moves_input == 'l' or moves_input == 'lb' or moves_input == 'lw':
        col_after = col - num
        row_after = row - num

    return [col_after, row_after]


def pick_row(figure, moves_input, pos_or_neg_value: list) -> int:

    if figure == 'w' and moves_input == 'l':
        row_move = pos_or_neg_value[1]
    elif figure == 'b' and moves_input == 'l':
        row_move = pos_or_neg_value[0]
    elif figure == 'w' and moves_input == 'r':
        row_move = pos_or_neg_value[0]
    elif figure == 'b' and moves_input == 'r':
        row_move = pos_or_neg_value[1]
    elif figure == 'b' and moves_input == 'rb':
        row_move = pos_or_neg_value[0]
    elif figure == 'b' and moves_input == 'lb':
        row_move = pos_or_neg_value[1]
    elif figure == 'w' and moves_input == 'lw':
        row_move = pos_or_neg_value[0]
    elif figure == 'w' and moves_input == 'rw':
        row_move = pos_or_neg_value[1]

    return row_move


def gameplay(col_after, row_after, col, row, to_eat, num, row_move, figure, board):

    if board[col_after][row_after] == ' ':
        board[col][row] = ' '
        board[col_after][row_after] = figure

    elif board[col_after][row_after] == to_eat and board[col_after-num][row_after + row_move] == ' ':
        board[col][row] = ' '
        board[col_after][row_after] = ' '
        board[col_after-num][row_after + row_move] = figure


def show_board(board: list):
    for i in range(len(board)):
        print(board[i])
