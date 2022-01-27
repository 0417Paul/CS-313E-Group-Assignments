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
#   for grid in word_grid:
#     print(grid) 
  
#   #for lst in word_list:
#   print(word_list)

# read_input()

# Input: a 2-D list representing the grid of letters and a single
#        string representing the word to search
# Output: returns a tuple (i, j) containing the row number and the
#         column number of the word that you are searching 
#         or (0, 0) if the word does not exist in the grid
def find_word (grid, word):
  i = 1
  j = 1
  for w in range(len(word)):
    # row search
    for g in grid:  
      if word[w] in g:
        for gl in range(len(g)): 
          g_index = gl
          w_index = w
          while w_index <= len(word)-1 and g_index <= len(g)-1:                               
            if word[w_index] == g[g_index]:
              #print(g[g_index])
              if w_index == len(word) - 1: 
                #print(tuple([i, g_index]))               
                break
              w_index += 1
              g_index += 1
                          
            elif word[w] != g[g_index]:
              break 
    #i += 1
  print(tuple([i, g_index]))
      #print(tuple([i, g.index(w)]))
            
     
find_word ([['S', 'I', 'N', 'S', 'N', 'O', 'W', 'S', 'T', 'O', 'R', 'M', 'W', 'I'],['K', 'L', 'N', 'T', 'S', 'N', 'O', 'W', 'M', 'A', 'N', 'E', 'F', 'E']], "SNOW")

# def main():
#   # read the input file from stdin
#   word_grid, word_list = read_input()

#   # find each word and print its location
#   for word in word_list:
#     location = find_word (word_grid, word)
#   print (word + ": " + str(location))

# if __name__ == "__main__":
#   main()