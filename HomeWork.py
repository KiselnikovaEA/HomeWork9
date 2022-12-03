class TicTacToeBoard:

    def __init__(self):
        self.board = [['-','-','-'],['-','-','-'],['-','-','-']]
        self.char = 'X'
        self.count = 0
        self.game_on = True

    def new_game(self):
        self.board = [['-','-','-'],['-','-','-'],['-','-','-']]
        self.game_on = True

    def get_field(self):
        return self.board

    def make_move(self, row, col):
        if self.game_on == True:
            if self.board[row-1][col-1] == '-':
                self.board[row-1][col-1] = self.char
                self.count += 1

                if self.count >= 5:
                    return self.check_field()
                else:
                    if self.char == 'X':
                        self.char = '0'
                    else:
                        self.char = 'X'
                    return 'Продолжаем играть'

            else:
                return f'Клетка {row},{col} уже занята'
        else:
            return 'Игра уже завершена'

    def check_field(self):
        if self.board[0].count(self.char) == 3 or self.board[1].count(self.char) == 3 or \
            self.board[2].count(self.char) == 3 or \
            list(zip(self.board[0], self.board[1], self.board[2]))[0].count(self.char) == 3 or \
            list(zip(self.board[0], self.board[1], self.board[2]))[1].count(self.char) == 3 or \
            list(zip(self.board[0], self.board[1], self.board[2]))[2].count(self.char) == 3 or \
            self.board[0][0] == self.board[1][1] == self.board[2][2] == self.char or \
            self.board[0][2] == self.board[1][1] == self.board[2][0] == self.char:
            self.game_on = False
            return f'Победил игрок {self.char}'
        else:
            if self.char == 'X':
                self.char = '0'
            else:
                self.char = 'X'
            return 'Продолжаем играть'


game = TicTacToeBoard()
print(*game.get_field(), sep="\n")
print(game.make_move(1, 1))
print(*game.get_field(), sep="\n")
print(game.make_move(1, 1))
print(game.make_move(1, 2))
print(*game.get_field(), sep="\n")
print(game.make_move(2, 1))
print(game.make_move(2, 2))
print(game.make_move(3, 1))
print(game.make_move(2, 2))
print(*game.get_field(), sep="\n")
