"""
LAB0 TASK2
GitHub: https://github.com/S-Daria/LAB0_TASK2.git
"""


def split_board(board: list) -> list:
    """
    get board as list of strings (lines)
    splits them into tuples of elements in line
    return list of tuples with elements

    >>> split_board(['**  3****', '* 4 1****'])
    [('*', '*', ' ', ' ', '3', '*', '*', '*', '*'), \
('*', ' ', '4', ' ', '1', '*', '*', '*', '*')]
    """
    splitted_board = []
    for line in board:
        splitted_line = []
        for letter in line:
            splitted_line.append(letter)
        splitted_board.append(tuple(splitted_line))
    return splitted_board


def check_horizontal(splitted_board: list) -> bool:
    """
    get splitted board (list of tuples with elements)
    checks whether it is no more than one number in range(1,9) in each row
    return True if line fits criteria
    False if not
    >>> check_horizontal([('*', '*', ' ', ' ', '3', '*', '*', '*', '*'), \
('*', ' ', '4', ' ', '1', '*', '*', '*', '*')])
    True
    >>> check_horizontal([('*', '*', ' ', '3', '3', '*', '*', '*', '*')])
    False
    """
    for number in [str(num) for num in range(1, 9)]:
        for line in splitted_board:
            if line.count(number) > 1:
                return False
    return True


def check_vertical(splitted_board: list) -> bool:
    """
    get splitted board (list of tuples with elements)
    checks whether it is no more than one number in range(1,9) in each column
    return True if column fits criteria
    False if not
    """
    for number in [str(num) for num in range(1, 9)]:
        for column_indx in range(9):
            times_in = 0
            for line in splitted_board:
                if line[column_indx] == number:
                    times_in += 1
                    if times_in > 1:
                        return False
    return True


def check_color_zones(splitted_board: list) -> bool:
    """
    get splitted board (list of tuples with elements)
    checks whether it is no more than one number in range(1,9)
    in each from 5 color zones
    return True if color zone fits criteria
    False if not
    """
    for number in [str(num) for num in range(1, 9)]:
        for zone in range(5):
            times_in = 0
            for line in range(zone, zone + 5):
                if splitted_board[8 - line][zone] == number:
                    times_in += 1
            times_in += splitted_board[8 -
                                       zone][zone + 1: zone + 5].count(number)
            if times_in > 1:
                return False
    return True


# board = [
#     '**** ****',
#     '***1 ****',
#     '**  3****',
#     '* 4 1****',
#     '     9 5 ',
#     ' 6  83  *',
#     '3   1  **',
#     '  8  2***',
#     '  2  ****'
# ]

# splitted_board = split_board(board)
# print(splitted_board)
# print(check_vertical(splitted_board))
# print(check_color_zones(splitted_board))


def validate_board(board):
    """
    get board
    check whether board fits all the criteria
    return True if fits
    return False if not
    """
    splitted_board = split_board(board)
    if check_horizontal(splitted_board) and check_vertical(splitted_board)\
            and check_color_zones(splitted_board):
        return True
    return False
