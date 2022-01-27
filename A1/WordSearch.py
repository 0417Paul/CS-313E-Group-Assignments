#  File: WordSearch.py

#  Description: Search words in a n by n grid and give the location of the words. 

#  Student Name: Jiaxi Wang 

#  Student UT EID: jw53499

#  Partner Name: Yilin Wen

#  Partner UT EID: yw22559

#  Course Name: CS 313E 

#  Unique Number: 51120

#  Date Created: Jan 26

#  Date Last Modified:

import sys

# Input: None
# Output: function returns a 2-D list that is the grid of letters and
#         1-D list of words to search
def read_input():
  word_grid = []
  word_list = []
  # size of grid
  n = int(sys.stdin.readline().strip())
  # skip the blank line
  sys.stdin.readline()

  for row in range(n):
    r = sys.stdin.readline().strip().split(" ")
    word_grid.append(r)

  # skip the blank line
  sys.stdin.readline()

  k = int(sys.stdin.readline().strip())
  for ki in range(k):
    i = sys.stdin.readline().strip()
    word_list.append(i)

  return word_grid, word_list


# Input: a 2-D list representing the grid of letters and a single
#        string representing the word to search
# Output: returns a tuple (i, j) containing the row number and the
#         column number of the word that you are searching 
#         or (0, 0) if the word does not exist in the grid
def find_word (grid, word):


def main():
  # read the input file from stdin
  word_grid, word_list = read_input()

  # find each word and print its location
  for word in word_list:
    location = find_word (word_grid, word)
  print (word + ": " + str(location))

if __name__ == "__main__":
  main()