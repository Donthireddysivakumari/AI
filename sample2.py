N = 8
def print_board(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print()
def is_safe(board, row, col):
    # Check column
    for i in range(row):
        if board[i][col]:
            return False
    # Check left diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i][j]:
            return False
    # Check right diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, N)):
        if board[i][j]:
            return False
    return True
def solve(board, row):
    if row == N:
        print_board(board)
        return True  # To stop at the first solution, remove this to find all
    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1
            if solve(board, row + 1):
                return True
            board[row][col] = 0  # Backtrack
    return False
board = [[0] * N for _ in range(N)]
solve(board, 0)
