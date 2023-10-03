#!/usr/bin/python3

"""
101-nqueens explores all possible solutions to the N queens puzzle, including
translations and reflections.

We attempted virtual backtracking without using recursion. In our local tests, the process
begins to slow down noticeably for N > 8, and it is successful up to N = 11. However, attempting
to solve for N > 11 will result in termination. Using recursion could potentially lead to a more
efficient process, but we haven't yet determined how to keep track of already derived solutions
using that method.

Attributes:
    N (int): The initial number of queens and the length of the board's side in piece positions.
    candidates (list of lists of lists of int): A list containing all successful solutions for
        a given number of columns checked.
"""
from sys import argv

if len(argv) is not 2:
    print('Usage: nqueens N')
    exit(1)

if not argv[1].isdigit():
    print('N must be a number')
    exit(1)

N = int(argv[1])

if N < 4:
    print('N must be at least 4')
    exit(1)

def board_column_gen(board=[]):

"""
Adds a column of zeroes to the right of a given board before testing it for
queen arrangements in that column.

Args:
    board (list of lists of int): A 2D list of integers, resized as needed to test
    the rightmost column for queen conflicts.

Returns:
    A modified 2D list with an additional column of zeros.
"""

if len(board):
        for row in board:
            row.append(0)
    else:
        for row in range(N):
            board.append([0])
    return board


def add_queen(board, row, col):

"""
Sets a "queen" (represented by 1) at the specified coordinates in the given board.

Args:
    board (list of lists of int): A 2D list of integers, resized as needed to test
        the rightmost column for queen conflicts.
    row (int): The index in the first dimension.
    col (int): The index in the second dimension.
"""

 board[row][col] = 1


def new_queen_safe(board, row, col):

	"""
Checks that, for the given board, when a new queen is placed in the rightmost
column, there are no other queens (represented by 1 values) to the left,
diagonally up-left, and diagonally down-left.

Args:
    board (list of lists of int): A 2D list of integers, sized to test the
        rightmost column for queen conflicts.
    row (int): The index in the first dimension.
    col (int): The index in the second dimension.

Returns:
    True if no conflicts are found on the left side for the new queen, or False
    if a conflict is found.
"""
	x = row
	y = col

# Check for conflicts when placing a queen at (x, y) on the chessboard
for i in range(1, N):
    if (y - i) >= 0:
        # Check the up-left diagonal
        if (x - i) >= 0:
            if board[x - i][y - i]:
                return False
        # Check the left side
        if board[x][y - i]:
            return False
        # Check the down-left diagonal
        if (x + i) < N:
            if board[x + i][y - i]:
                return False
return True

def coordinate_format(candidates):
    """Converts a chessboard (matrix of 1 and 0) into a list of row/column
    indices for each queen (1).

    Args:
        candidates (list of lists of lists of int): List containing all successful
            solutions for the number of columns last checked.

    Returns:
        List of queen coordinates as (row, column) pairs.
    """
    queen_coordinates = []
    for x, attempt in enumerate(candidates):
        queen_coordinates.append([])
        for i, row in enumerate(attempt):
            queen_coordinates[x].append([])
            for j, col in enumerate(row):
                if col:
                    queen_coordinates[x][i].append(i)  # Row index
                    queen_coordinates[x][i].append(j)  # Column index
    return queen_coordinates

# Initialize the candidates list with the first column of 0s
candidates = []
candidates.append(board_column_gen())

# Iterate through columns, testing the rightmost column
for col in range(N):
    # Start a new generation of the candidate list for every round of testing
    new_candidates = []
    # Test each candidate from the previous round at the current column
    for matrix in candidates:
        # For every row in that candidate's rightmost column
        for row in range(N):
            # Check if placing a queen at these coordinates results in conflicts
            if new_queen_safe(matrix, row, col):
                # No conflicts? Create a copy of that candidate
                temp = [line[:] for line in matrix]
                # Place a queen in that position
                add_queen(temp, row, col)
                # Unless this is the last round of testing, add a new column of 0s on the right
                if col < N - 1:
                    board_column_gen(temp)
                # Add the new candidate to this round's list of successes
                new_candidates.append(temp)
    # When finished with the round, discard the "parent" candidates
    candidates = new_candidates

# Format results to match the desired output
for item in coordinate_format(candidates):
    print(item)

