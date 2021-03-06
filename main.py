from board import Board
import move
from game import pick_row, set_num, setting_to_eat_value_and_inversing_moves_input_value, step_plus, show_board, gameplay
from checkings import check_char_inputs, check_coordinates, is_out_of_bounds, if_a_move_was_made


board = Board().create_board

pos_or_neg = [1, -1]

show_board(board)

prev_figure = 'c'
prev_col_after_and_num = 0
prev_row_after_and_row_move = 0

j = 0
while j == 0:

    try:

        print('Whose turn')
        figure = input()

        figure = check_char_inputs(figure, 'figure')

        print('Columns')
        column = input()

        print('Rows')
        row = input()

        cols_and_rows = check_coordinates(column, row, board, figure)

        column = cols_and_rows[0]
        row = cols_and_rows[1]

        print('Which side')
        moves_input = input()

        moves_input = check_char_inputs(moves_input, 'move')

        my_move = move.Move(column, row, figure, moves_input)

        num = set_num(my_move.get_figure(), pos_or_neg,
                      my_move.get_moves_input())

        setting_to_eat_value_and_inversing_moves_input_value(
            my_move, my_move.get_figure(), my_move.get_moves_input())

        step_plus_list = step_plus(my_move.get_moves_input(
        ), my_move.get_column(), my_move.get_row(), num)

        cr_after = is_out_of_bounds(
            step_plus_list, my_move.get_column(), my_move.get_row())

        col_after = cr_after[0]
        row_after = cr_after[1]

        row_move = pick_row(my_move.get_figure(),
                            my_move.get_moves_input(), pos_or_neg)

        if_a_move_was_made(board, my_move.get_figure(),
                           col_after, row_after, prev_figure, my_move, prev_col_after_and_num,
                           prev_row_after_and_row_move, my_move.get_column(), my_move.get_row(), num, row_move, my_move.get_moves_input())

        list_of_prev_moves = gameplay(col_after, row_after, my_move.get_column(), my_move.get_row(),
                                      my_move.get_to_eat(), num, row_move, my_move.get_figure(), board, my_move.get_moves_input())

        prev_figure = list_of_prev_moves[0]
        prev_col_after_and_num = list_of_prev_moves[1]
        prev_row_after_and_row_move = list_of_prev_moves[2]

        show_board(board)

    except Exception as e:
        print(f'Error occuried: {e}')
