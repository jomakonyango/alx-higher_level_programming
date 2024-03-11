#!/usr/bin/python3
import sys

def print_solution(board):
    """Print the solution"""
    solution = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                solution.append([i, j])
    print(solution)

def is_safe(board, row, col):
    """Check if a queen can be placed on board[row][col]"""
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_nq(board, col):
    """Solve the N queens problem using backtracking"""
    if col == len(board):
        print_solution(board)
        return True
    res = False
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            res = solve_nq(board, col + 1) or res
            board[i][col] = 0
    return res

def solve(n):
    """Solve the N queens problem"""
    board = [[0]*n for _ in range(n)]
    if not solve_nq(board, 0):
        return
    return

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)
if n < 4:
    print("N must be at least 4")
    sys.exit(1)
solve(n)
