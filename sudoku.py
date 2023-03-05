#!/usr/bin/env python
import random

def print_board(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
            if j == 2 or j == 5:
                print("|", end=" ")
        print()
        if i == 2 or i == 5:
            print("-" * 22)

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def is_valid(board, num, pos):
    row, col = pos
    # Check row
    if num in board[row]:
        return False
    # Check column
    if num in [board[i][col] for i in range(9)]:
        return False
    # Check square
    square_x = (col // 3) * 3
    square_y = (row // 3) * 3
    for i in range(square_y, square_y + 3):
        for j in range(square_x, square_x + 3):
            if board[i][j] == num:
                return False
    return True

def solve_board(board):
    find = find_empty(board)
    if not find:
        return True
    row, col = find
    for i in range(1, 10):
        if is_valid(board, i, (row, col)):
            board[row][col] = i
            if solve_board(board):
                return True
            board[row][col] = 0
    return False

def generate_board():
    board = [[0 for i in range(9)] for j in range(9)]
    solve_board(board)
    empty_spots = random.randint(50, 60)
    while empty_spots > 0:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if board[row][col] != 0:
            board[row][col] = 0
            empty_spots -= 1
    return board

def play_game():
    board = generate_board()
    print_board(board)
    while True:
        row = int(input("Enter row number (1-9): ")) - 1
        col = int(input("Enter column number (1-9): ")) - 1
        if board[row][col] != 0:
            print("That position is already filled!")
            continue
        num = int(input("Enter a number (1-9): "))
        if not is_valid(board, num, (row, col)):
            print("That number is not valid!")
            continue
        board[row][col] = num
        print_board(board)
        if find_empty(board) is None:
            print("Congratulations, you won!")
            break

if __name__ == "__main__":
    play_game()
