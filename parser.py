""" SGF Parsers
"""

import sys
import numpy as np

from sgfmill import sgf
from sgfmill import sgf_moves
from sgfmill import boards

def mat_to_sgf(mat, pathname):
    """Saves matrix of game state as sgf file.

    Expects 19x19 numpy matrix with '0' for empty, '1' for black and '-1' for
    white stones.
    """
    game = sgf.Sgf_game(size=19)
    root_node = game.get_root()
    game.set_date()
    board = boards.Board(19)
    # TODO: determine points from mat
    black_points = []
    white_points = []
    empty_points = []
    for row in range(19):
        for col in range(19):
            stone = mat.item((row,col))
            if stone == 1:
                black_points.append((row,col))
            if stone == -1:
                white_points.append((row,col))
            if stone == 0:
                empty_points.append((row,col))
    board.apply_setup(black_points, white_points, empty_points)
    sgf_moves.set_initial_position(game, board)
    with open(pathname, "wb") as f:
        f.write(game.serialise())

def sgf_to_mat(pathname, move_number = None):
    """Converts game position from sgf file to in-memory matrix representation.

    Only follows left branch of game tree. 
    Move number one is the empty board, default is the last node.
    Returns numpy matrix with '1's for black stones and '-1' for white
    ones.
    """
    with open(pathname, "rb") as f:
        sgf_src = f.read()
    try:
        sgf_game = sgf.Sgf_game.from_bytes(sgf_src)
    except ValueError:
        raise Exception("bad sgf file")
    try:
        board, plays = sgf_moves.get_setup_and_moves(sgf_game)
    except ValueError as e:
        raise Exception(str(e))
    if move_number is not None:
        move_number = max(0, move_number-1)
        plays = plays[:move_number]
    for colour, move in plays:
        if move is None:
            continue
        row, col = move
        try:
            board.play(row, col, colour)
        except ValueError:
            raise Exception("illegal move in sgf file")
    mat = np.full((19,19), 0)
    for colour, pos in board.list_occupied_points():
        if (colour == 'b'):
            mat[pos] = 1
        if (colour == 'w'):
            mat[pos] = -1
    return mat
