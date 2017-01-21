from copy import deepcopy

from main import tic_tac_toe
from main.tic_tac_toe import Player


def get_move(board, player=Player.X, alpha=float('-inf'), beta=float('inf')):
    # Terminate search at the bottom of the tree
    if len(tic_tac_toe.get_valid_moves(board)) == 0:
        return None, tic_tac_toe.get_score_difference(board);

    if player == Player.X:
        best_score = float('-inf');
        for move in tic_tac_toe.get_valid_moves(board):
            dupeBoard = deepcopy(board);
            tic_tac_toe.make_move(dupeBoard, move, Player.X);
            _, score = get_move(dupeBoard, Player.O, alpha, beta);
            if score > best_score:
                best_move = move;
                best_score = score;
            alpha = max(alpha, score);
            if alpha > beta:
                break;
        return best_move, best_score;
    else:
        best_score = float('inf');
        for move in tic_tac_toe.get_valid_moves(board):
            dupeBoard = deepcopy(board);
            tic_tac_toe.make_move(dupeBoard, move, Player.O);
            _, score = get_move(dupeBoard, Player.X, alpha, beta);
            if score < best_score:
                best_move = move;
                best_score = score;
            beta = min(beta, score);
            if alpha > beta:
                break;
        return best_move, best_score;
    return best_move, score;

if __name__ == '__main__':
    board_size = 3
    board = [[Player.NONE for _ in range(board_size)] for _ in range(board_size)]
    tic_tac_toe.display_board(board)
    player = Player.X

    while True:
        if player == Player.X:
            move, score = get_move(board, player)
        else:
            move = [int(x) for x in input().split(',')]
        if move == None: break
        tic_tac_toe.make_move(board, move, player)
        tic_tac_toe.display_board(board)
        player = Player.O if player == Player.X else Player.X
