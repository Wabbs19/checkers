class Board:

    @property
    def create_board(self):

        matrix = [[' ' for a in range(8)] for b in range(8)]
        figures = ['w', 'b']

        for j in range(8):
            if j > 2:
                figure = figures[0]
            else:
                figure = figures[1]
            for i in range(8):
                if j != 3 and j != 4:
                    if j % 2 == 0 and i % 2 != 0:
                        matrix[j][i] = figure
                    if j % 2 != 0 and i % 2 == 0:
                        matrix[j][i] = figure

        return matrix
