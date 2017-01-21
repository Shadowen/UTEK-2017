from enum import Enum


class Player(Enum):
    NONE = 0
    X = 1
    O = 2


def display_board(board):
    for row in board:
        for x in row:
            if x == Player.O:
                print("O", end="")
            elif x == Player.X:
                print("X", end="")
            else:
                print("-", end="")
        print()
    print()


def get_valid_moves(board):
    # Game is over
    if get_score_difference(board) != 0:
        return []

    valid_moves = []
    for y in range(3):
        for x in range(3):
            if board[x][y] == Player.NONE:
                valid_moves.append((x, y))
    return valid_moves


def make_move(board, move, player):
    board[move[0]][move[1]] = player


def get_score_difference(board):
    # Row check
    for x in range(3):
        this_player = board[x][0]
        if this_player == Player.NONE:
            continue
        matching = True
        for y in range(3):
            if board[x][y] != this_player:
                matching = False
                break
        if matching:
            return 1 if this_player == Player.X else -1

    # Column check
    for y in range(3):
        this_player = board[0][y]
        if this_player == Player.NONE:
            continue
        matching = True
        for x in range(3):
            if board[x][y] != this_player:
                matching = False
                break
        if matching:
            return 1 if this_player == Player.X else -1

    # Diagonal check
    if board[0][0] == board[1][1] == board[2][2] != Player.NONE:
        return 1 if board[0][0] == Player.X else -1

    if board[0][2] == board[1][1] == board[2][0] != Player.NONE:
        return 1 if board[0][2] == Player.X else -1

    return 0  # Neither player has won


if __name__ == '__main__':
    board = [[Player.NONE for _ in range(3)] for _ in range(3)]
    display_board(board)
    print(get_valid_moves(board))
    print(get_score_difference(board))
    make_move(board, (0, 0), Player.O)
    display_board(board)
    print(get_score_difference(board))

    make_move(board, (0, 1), Player.X)
    display_board(board)
    print(get_valid_moves(board))
    print(get_score_difference(board))

    make_move(board, (1, 1), Player.O)
    display_board(board)
    print(get_valid_moves(board))
    print(get_score_difference(board))

    make_move(board, (0, 2), Player.X)
    display_board(board)
    print(get_valid_moves(board))
    print(get_score_difference(board))

    make_move(board, (2, 2), Player.O)
    display_board(board)
    print(get_valid_moves(board))
    print(get_score_difference(board))
