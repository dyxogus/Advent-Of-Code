import logging

from save_christmas.beautifier.functional import transform


class Bingo:
    @staticmethod
    def parse_line_to_numbers(line):
        return transform(int, line.split(','))

    @staticmethod
    def parse_lines_to_boards(raw_lines):
        return [BingoBoard(BingoBoard.raw_input_to_board_state(raw_line)) for raw_line in raw_lines]

    @staticmethod
    def read_input_from_file(file_path):
        boards = []

        with open(file_path) as input_file:
            numbers = current_line = input_file.readline().rstrip()
            while current_line:
                # We have empty line as divider
                current_line = input_file.readline()
                if not current_line: break

                raw_string_board = [input_file.readline().rstrip() for _ in range(BingoBoard.COL_SIZE)]
                boards.append(raw_string_board)

            return numbers, boards

    def __init__(self, numbers, boards):
        self.numbers = numbers
        self.boards = boards

    def find_earliest_winner(self):
        for number in self.numbers:
            logging.debug(f'Drawn number {number}')
            for board in self.boards:
                board.mark_entry(number)

                if board.check_if_won():
                    return board.get_score(number)

        assert False, 'There was no winner!'


class BingoBoard:
    ROW_SIZE = COL_SIZE = 5

    @staticmethod
    def raw_input_to_board_state(raw_string_board):
        def raw_line_to_row(raw_line):
            return transform(int, pre_process_line(raw_line))

        def pre_process_line(line):
            return line.lstrip().rstrip().replace('  ', ' ').split(' ')

        return transform(raw_line_to_row, raw_string_board)

    def __init__(self, board):
        assert (len(board) == len(board[0]))
        assert (len(board) == BingoBoard.ROW_SIZE)
        self.board = board
        self.marked = [[False] * BingoBoard.ROW_SIZE for _ in range(BingoBoard.COL_SIZE)]

    def mark_entry(self, entry):
        for col_index in range(BingoBoard.COL_SIZE):
            for row_index in range(BingoBoard.ROW_SIZE):
                if self.board[col_index][row_index] == entry:
                    self.marked[col_index][row_index] = True

    def check_if_won(self):
        has_any_rows_won = any(all(marked_row) for marked_row in self.marked)
        has_any_cols_won = any(all(marked_row[col_index] for marked_row in self.marked)
                               for col_index in range(BingoBoard.COL_SIZE))
        return has_any_rows_won or has_any_cols_won

    def get_score(self, multiplier):
        assert (self.check_if_won()), 'Only call this function if the board is a winner'

        unmarked_indices = [
            (col_index, row_index)
            for col_index in range(BingoBoard.COL_SIZE) for row_index in range(BingoBoard.ROW_SIZE)
            if not self.marked[col_index][row_index]
        ]

        return sum(self.board[col_index][row_index] for (col_index, row_index) in unmarked_indices) * multiplier


def q4_p1(numbers_string, boards_string):
    numbers = Bingo.parse_line_to_numbers(numbers_string)
    boards = Bingo.parse_lines_to_boards(boards_string)

    bingo_game = Bingo(numbers, boards)
    return bingo_game.find_earliest_winner()


def q4_p2(numbers_string, boards_string):
    pass


if __name__ == '__main__':
    args = Bingo.read_input_from_file('../inputs/input_04.txt')
    print(q4_p1(*args))
