from copy import deepcopy
import requests
from requests.exceptions import ConnectionError
import time

import tic_tac_toe
from tic_tac_toe import Player


def get_move(board, player=Player.X, alpha=float('-inf'), beta=float('inf')):
    # Terminate search at the bottom of the tree
    if len(tic_tac_toe.get_valid_moves(board)) == 0:
        return None, tic_tac_toe.get_score_difference(board)

    if player == Player.X:
        best_score = float('-inf')
        for move in tic_tac_toe.get_valid_moves(board):
            dupeBoard = deepcopy(board)
            tic_tac_toe.make_move(dupeBoard, move, Player.X)
            _, score = get_move(dupeBoard, Player.O, alpha, beta)
            if score > best_score:
                best_move = move
                best_score = score
            alpha = max(alpha, score)
            if alpha > beta:
                break
        return best_move, best_score
    else:
        best_score = float('inf')
        for move in tic_tac_toe.get_valid_moves(board):
            dupeBoard = deepcopy(board)
            tic_tac_toe.make_move(dupeBoard, move, Player.O)
            _, score = get_move(dupeBoard, Player.X, alpha, beta)
            if score < best_score:
                best_move = move
                best_score = score
            beta = min(beta, score)
            if alpha > beta:
                break
        return best_move, best_score
    return best_move, score

if __name__ == '__main__':
    board_size = 3
    board = [[Player.NONE for _ in range(board_size)] for _ in range(board_size)]
    tic_tac_toe.display_board(board)
    player = Player.X

    # Game Loop
    while True:
        if player == Player.X:
            print("Computer turn")
            move, score = get_move(board, player)
        else:
            print("player turn")
            move = None
            while(True):
                move_str = input("Enter move ('r,c'): ")
                try:
                    move = [int(x) for x in move_str.split(",")]
                    if (len(move) == 2 and 0 <= move[0] <= 2 and 0 <= move[1] <= 2):
                        if (board[move[0]][move[1]] == Player.NONE):                            
                            break
                        else:
                            print("Please choose an unoccupied squre")
                    else:
                        print("Please enter a valid move")
                except Exception as e:
                    e.print_stack_trace()
        
        tic_tac_toe.make_move(board, move, player)
        tic_tac_toe.display_board(board)        

        pos = {'Z' : move[0]*3 + move[1], 'p': 'X' if player == player.X else 'O'}

        try:
            r = requests.get("http://169.254.170.177/move", params=pos, timeout=1)
            time.sleep(2)
        except ConnectionError as e:
            print("Failed to connect to arduino")

        if (tic_tac_toe.get_score_difference(board) != 0):
            print("Player {} wins".format(player))
            break
        elif (len(tic_tac_toe.get_valid_moves(board)) == 0):
            print("Draw game")
            break

        player = Player.O if player == Player.X else Player.X
        
