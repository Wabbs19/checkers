from board import Board
import move
from game import pick_row, set_num, setting_to_eat_value_and_inversing_moves_input_value, step_plus, show_board, gameplay
from checkings import check_char_inputs, check_coordinates


board = Board().create_board

pos_or_neg = [1, -1]

show_board(board)

# j = 0
# while j < 3:

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

num = set_num(my_move.get_figure(), pos_or_neg)

setting_to_eat_value_and_inversing_moves_input_value(
    my_move, my_move.get_figure(), my_move.get_moves_input())

step_plus_list = step_plus(my_move.get_moves_input(
), my_move.get_column(), my_move.get_row(), num)

col_after = step_plus_list[0]

row_after = step_plus_list[1]

row_move = pick_row(my_move.get_figure(),
                    my_move.get_moves_input(), pos_or_neg)

gameplay(col_after, row_after, my_move.get_column(), my_move.get_row(),
         my_move.get_to_eat(), num, row_move, my_move.get_figure(), board)

show_board(board)
