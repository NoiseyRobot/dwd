import subprocess
import os
import sys

board = [[" "] * 10 for _ in range(10)]

def clear():
    if os.name == "nt":
        subprocess.run("cls")
    else:
        subprocess.run("clear")

def loop(a=None, b=None, c=None, d=None, e=None, f=None, g=None, h=None, i=None, j=None):
    columns, rows = os.get_terminal_size()

    # Quit if game window not big enough
    if rows < 10:
        print("Please resize your terminal to have ten or more rows")
        sys.exit(1)

    if columns < 10:
        print("Please resize your terminal to have ten or more columns")
        sys.exit(1)

    # Update only rows that were passed in
    if a is not None: board[0] = a
    if b is not None: board[1] = b
    if c is not None: board[2] = c
    if d is not None: board[3] = d
    if e is not None: board[4] = e
    if f is not None: board[5] = f
    if g is not None: board[6] = g
    if h is not None: board[7] = h
    if i is not None: board[8] = i
    if j is not None: board[9] = j

    clear()

    for row in board:
        print("".join(row))


def clear_board():
    global board
    board = [[" "] * 10 for _ in range(10)]


def clear_row(row):
    board[row] = [" "] * 10


def clear_spot(row, column):
    board[row][column] = " "
