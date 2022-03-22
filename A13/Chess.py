
#  File: Chess.py

#  Description: Find all solutions of the Queen problem for a board of a particular size. 

#  Student Name: Jiaxi Wang

#  Student UT EID: jw53499

#  Partner Name: Yilin Wen

#  Partner UT EID: yw22559

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: Mar 18

#  Date Last Modified: Mar 18

import sys

class Queens (object):
  # initialize the board
  def __init__ (self, n = 8):
    self.board = []
    self.n = n

    # create an empty board, using '*' to denote empty square
    for i in range (self.n):
      row = []
      for j in range (self.n):
        row.append ('*')
      self.board.append (row)
    self.solutions = []

  # print the board
  def print_board (self):
    for i in range (self.n):
      for j in range (self.n):
        print (self.board[i][j], end = ' ')
      print ()
    print ()

  # check if a position on the board is valid
  def is_valid (self, row, col):
    for i in range (self.n):
      # first going for a given row, along the column, then going for a given column along rows
      if (self.board[row][i] == 'Q') or (self.board[i][col] == 'Q'):
        return False
    
    # check diagnosis
    for i in range (self.n):
      for j in range (self.n):
        row_diff = abs (row - i)
        col_diff = abs (col - j)
        # if row_diff & col_diff are the same, it has to be on the diagnosis
        if (row_diff == col_diff) and (self.board[i][j] == 'Q'):
          return False
    return True
    
  # do the recursive backtracking
  def recursive_solve (self, col):
    # base case, if have reached the very last column
    if (col == self.n):
      # append the solutions we found to the list of all solutions
      self.solutions.append(self.board)
      return True
    else:
      for i in range(self.n):
        # if it's a safe place to place a queen
        if (self.is_valid(i, col)):
          self.board[i][col] = 'Q'
          # go recursively to next 
          self.recursive_solve (col + 1)
          self.board[i][col] = '*'
      return False

  # if the problem has a solution print the board
  def solve (self):
    for i in range (self.n):
      if (self.recursive_solve(i)):
        self.print_board()

def main():
  # read the size of the board
  line = sys.stdin.readline()
  line = line.strip()
  n = int (line)

  # create a chess board
  game = Queens (n)

  # place the queens on the board and count the solutions
  game.recursive_solve(0)

  # print the number of solutions
  print(len(game.solutions))
 
if __name__ == "__main__":
  main()

