class Move:

    column = row = 0
    figure = to_eat = moves_input = ''

    def __init__(self, column, row, figure, moves_input):

        self.column = column
        self.row = row
        self.figure = figure
        self.moves_input = moves_input

    def set_to_eat(self, to_eat):
        self.to_eat = to_eat

    def set_moves_input(self, moves_input):
        self.moves_input = moves_input

    def get_column(self):
        return self.column

    def get_row(self):
        return self.row

    def get_figure(self):
        return self.figure

    def get_to_eat(self):
        return self.to_eat

    def get_moves_input(self):
        return self.moves_input