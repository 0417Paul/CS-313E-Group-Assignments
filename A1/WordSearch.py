#  File: WordSearch.py

#  Description: Search words in a n by n grid and give the location of the words. 

#  Student Name: Jiaxi Wang 

#  Student UT EID: jw53499

#  Partner Name: Yilin Wen

#  Partner UT EID: yw22559

#  Course Name: CS 313E 

#  Unique Number: 51120

#  Date Created: Jan 26

#  Date Last Modified: Jan 27

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

  #read the grid into a list
  for row in range(n):
    r = sys.stdin.readline().strip().upper().split(" ")
    word_grid.append(r)

  # skip the blank line
  sys.stdin.readline()

  # read the word list
  k = int(sys.stdin.readline().strip())
  for ki in range(k):
    i = sys.stdin.readline().strip().upper()
    word_list.append(i)
  
  return word_grid, word_list



# Input: a 2-D list representing the grid of letters and a single
#        string representing the word to search
# Output: returns a tuple (i, j) containing the row number and the
#         column number of the word that you are searching 
#         or (0, 0) if the word does not exist in the grid

def find_word (grid, word):
  # 8 directions for searching words
  direc = [[-1, 0], [1, 0], [1, 1], 
        [1, -1], [-1, -1], [-1, 1],
        [0, 1], [0, -1]]
  # boundaries of the grid
  rows = len(grid)
  cols = len(grid[0])

  # go through the entire grid
  for r in range(rows):
    
    for c in range(cols):
      
      # if the first letter matches
      if grid[r][c] == word[0]:
        
        # case if the word only contains 1 letter, no need to go further
        if len(word) == 1:
          return tuple([r + 1, c + 1])
          
        # walk through all 8 directions
        for x,y in direc:
          r_direc = r + x
          c_direc = c + y
          
          # check if the rest of the letters in 8 directions matches the rest of the letters in the word
          for w in range(1, len(word)):
            
            # assign the boundries of the grid and check letters
            if (0 <= r_direc < rows and 0 <= c_direc < cols and grid[r_direc][c_direc] == word[w]):
              r_direc += x
              c_direc += y
              
              # if checked till the last letter
              if w == len(word) - 1:
                return tuple([r + 1, c + 1])

            # if the rest of the letters don't match the word
            else:
              break
  
  # no word match found
  return tuple([0, 0])    



def main():
  # read the input file from stdin
  word_grid, word_list = read_input()

  # find each word and print its location
  for word in word_list:
    location = find_word (word_grid, word)
    print (word + ": " + str(location))

if __name__ == "__main__":
  main()