"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_X = sum(row.count(X) for row in board)
    count_O = sum(row.count(O) for row in board)
    if count_X <= count_O:
        return X
    else:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    result = set()
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if col == EMPTY:
                result.add((i, j))
    return result

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]):
        raise Exception("Invalid move: Move out of bounds")
    if board[i][j] is not EMPTY:
        raise Exception("Invalid move")
    new_board = copy.deepcopy(board)
    new_board[i][j] = player(board)
    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if row[0] == row[1] == row[2] and row[0] in (X, O):
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] in (X, O):
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] in (X, O):
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] in (X, O):
        return board[0][2]

    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    for row in board:
        if EMPTY in row:
            return False
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    current_player = player(board)

    if current_player == X:
        value, move = max_value(board)
    else:
        value, move = min_value(board)

    return move

def max_value(board):
    if terminal(board):
        return utility(board), None

    v = float("-inf")
    best_action = None

    for action in actions(board):
        min_val, _ = min_value(result(board, action))
        if min_val > v:
            v = min_val
            best_action = action
    return v, best_action

def min_value(board):
    if terminal(board):
        return utility(board), None

    v = float("inf")
    best_action = None

    for action in actions(board):
        max_val, _ = max_value(result(board, action))
        if max_val < v:
            v = max_val
            best_action = action
    return v, best_action

