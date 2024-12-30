def print_board(board):
    """Print the Sudoku board in a readable format."""
    for row in range(len(board)):
        if row % 3 == 0 and row != 0:
            print("-" * 21)
        for col in range(len(board[0])):
            if col % 3 == 0 and col != 0:
                print("|", end=" ")
            if col == 8:
                print(board[row][col])
            else:
                print(board[row][col], end=" ")

def is_valid(board, num, pos):
    """
    Check if a number can be placed at a specific position.

    Args:
    - board: 2D list representing the Sudoku board.
    - num: Number to check.
    - pos: Tuple (row, col) representing the position.

    Returns:
    - True if valid, False otherwise.
    """
    row, col = pos

    # Check row
    if num in board[row]:
        return False

    # Check column
    if num in [board[i][col] for i in range(len(board))]:
        return False

    # Check 3x3 box
    box_x, box_y = col // 3, row // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num:
                return False

    return True

def find_empty(board):
    """
    Find the next empty space on the board.

    Args:
    - board: 2D list representing the Sudoku board.

    Returns:
    - Tuple (row, col) of the empty position, or None if the board is full.
    """
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 0:
                return (row, col)
    return None

def solve(board):
    """
    Solve the Sudoku puzzle using backtracking.

    Args:
    - board: 2D list representing the Sudoku board.

    Returns:
    - True if a solution is found, False otherwise.
    """
    empty = find_empty(board)
    if not empty:
        return True
    row, col = empty

    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if solve(board):
                return True

            # Undo move (backtrack)
            board[row][col] = 0

    return False

# Example Sudoku Board (0 represents empty cells)
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

# Solve and display the Sudoku board
print("Original Sudoku Board:")
print_board(sudoku_board)
if solve(sudoku_board):
    print("\nSolved Sudoku Board:")
    print_board(sudoku_board)
else:
    print("\nNo solution exists.")
