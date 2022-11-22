"""
Tic Tac Toe Player
"""

import copy
import math

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
    x = 0
    o = 0
    for row in board:
        x += row.count(X)
        o += row.count(O)
    if (x == 0 and o == 0) or x == o:
        return X

    return O

   


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    list_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                list_actions.add((i,j))
    print(f"list of actions : {list_actions}")
    return list_actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i,j = action[0], action[1]
    try:
        board[i][j] = player(board)
    except:
        # board[i][j] is not EMPTY
        print('already taken')
    return board

def wins(player, board):
    """ 
    Returns true if the given player won, and false if not
    """
    for i in range(3):
        if [board[i][x] for x in range(3)].count(player) == 3 : return True
        if [board[x][i] for x in range(3)].count(player) == 3 : return True
    if [board[0][0], board[1][1],board[2][2]].count(player) == 3 : return True
    elif [board[0][2], board[1][1],board[2][0]].count(player) == 3 : return True
    return False


def board_full(board):
    """
    Returns true if the board is full
    """
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY: return False
    return True

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if wins(X,board): return X
    elif wins(O,board) : return O
    return


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if wins(X,board) or wins(O,board) or board_full(board) : return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == X: return 1
        elif winner(board) == O : return -1
        return 0
    return

def minimax_beta(board):
    copy_board = copy.deepcopy(board)

    if terminal(copy_board):
        return utility(copy_board)
    if player(copy_board) == X:
        best = -1000
        for action in actions(copy_board):
            
            copy_board = result(copy_board,action)
        
            best = max(best, minimax_beta(copy_board))
            copy_board = board
        return best
    else:
        best = 1000
        for action in actions(copy_board):
            
            copy_board = result(copy_board,action)
        
            best = min(best, minimax_beta(copy_board))
            copy_board = board
        return best

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    copy_board = copy.deepcopy(board)

    if player(copy_board) == X:
        optimal_action = (-1,-1)
        best = -1000
        for action in actions(copy_board):
            
            copy_board = result(copy_board,action)
            value = minimax_beta(copy_board)
            if value> best:
                best = value
                optimal_action = action
        print(f"optimal action : {optimal_action}")
        return optimal_action
    else:
        optimal_action = (-1,-1)
        best = 1000
        for action in actions(copy_board):
            
            copy_board = result(copy_board,action)
        
            value = minimax_beta(copy_board)
            if value < best:
                best = value
                optimal_action = action
        print(f"optimal action : {optimal_action}")
        return optimal_action

