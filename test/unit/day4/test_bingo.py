from save_christmas.q4 import BingoBoard

EXAMPLE_BOARD_1_RAW_INPUT = [
    '22 13 17 11  0',
    ' 8  2 23  4 24',
    '21  9 14 16  7',
    ' 6 10  3 18  5',
    ' 1 12 20 15 19',
]
EXAMPLE_BOARD_2_RAW_INPUT = [
    ' 3 15  0  2 22',
    ' 9 18 13 17  5',
    '19  8  7 25 23',
    '20 11 10 24  4',
    '14 21 16 12  6',
]
EXAMPLE_BOARD_3_RAW_INPUT = [
    '14 21 17 24  4',
    '10 16 15  9 19',
    '18  8 23 26 20',
    '22 11 13  6  5',
    ' 2  0 12  3  7',
]
EXAMPLE_BOARDS = [EXAMPLE_BOARD_1_RAW_INPUT, EXAMPLE_BOARD_2_RAW_INPUT, EXAMPLE_BOARD_3_RAW_INPUT]


def test_raw_input_to_board_state():
    assert BingoBoard.raw_input_to_board_state(EXAMPLE_BOARD_1_RAW_INPUT) == [
        [22, 13, 17, 11, 0, ],
        [8, 2, 23, 4, 24, ],
        [21, 9, 14, 16, 7, ],
        [6, 10, 3, 18, 5, ],
        [1, 12, 20, 15, 19, ],
    ]
