def check_coordinates(c, r, board, figure):

    j = 0
    column = c
    row = r
    
    while j == 0:

        try:
            column = int(column)
            row = int(row)
        except ValueError:
            print('Only numeric values allowed!!!')
            column = -10
            row = -10

        if column < 8 and row < 8 and column > -9 and row > -9 and if_figure_equals(board, column, row, figure):
            return [column, row]
        else:
            print('Enter correct numeric values, it must be between -8 and 7:\n')
            print('Columns')
            column = input()
            print('Rows')
            row = input()
            


def if_figure_equals(board, c, r, figure):

    if board[c][r] != figure:
        print('The box is either empty or has the wrong figure')
        return False
    else:
        return True


def check_char_inputs(fk, f):
    figure = fk
    j = 0
    while j == 0:
        if (figure == 'w' or figure == 'b') and f == 'figure':
            return figure
        elif (figure == 'l' or figure == 'r') and f == 'move':
            return figure
        else:
            if f == 'figure':
                print('Choose "w" or "b" figure')
            elif f == 'move':
                print('Choose "r" or "l"')
            figure = input()
