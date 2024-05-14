#!/usr/bin/python3
"""A Python script that solves the N queens problem"""


import sys

def is_safe(board, row, col):
    # To check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 'N':
            return False

    # To check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'N':
            return False

    # To check right diagonal
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 'N':
            return False

    return True


def solve_n_queens(board, row, n):
    if row == n:
        print_solution(board)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row][col] = 'N'
            solve_n_queens(board, row + 1, n)
            board[row][col] = '.'

def print_solution(board):
    for row in board:
        print(' '.join(row))
    print()

def nqueens(N):
    try:
        N = int(N)
    except ValueError:
        print('N must be a number')
        sys.exit(1)
    
    if N < 4:
        print('N must be at least 4')
        sys.exit(1)
    
    board = [['.' for _ in range(N)] for _ in range(N)]
    solve_n_queens(board, 0, N)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)
    
    nqueens(sys.argv[1])