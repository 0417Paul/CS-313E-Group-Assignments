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
    r = sys.stdin.readline().strip().split(" ")
    word_grid.append(r)

  # skip the blank line
  sys.stdin.readline()

  # read the word list
  k = int(sys.stdin.readline().strip())
  for ki in range(k):
    i = sys.stdin.readline().strip()
    word_list.append(i)
  
  return word_grid, word_list


def find_word (grid, word,row,col):
    dir = [[-1, 0], [1, 0], [1, 1], 
        [1, -1], [-1, -1], [-1, 1],
        [0, 1], [0, -1]]
    
    if grid[row][col] != word[0]:
        return False

    for x,y in dir:

        rd, cd = row + x, col + y
        flag = True

        for k in range(1, len(word)):

            if (0 <= rd < self.R and 0 <= cd < self.C and word[k] == grid[rd][cd]):
                rd += x
                cd += y

            else:
                flag = False
                break

        if flag:
            return True

    return False

    # Searches given word in a given matrix
    # in all 8 directions   
def patternSearch(self, grid, word):
         
  # Rows and columns in given grid
  self.R = len(grid)
  self.C = len(grid[0])
         
  # Consider every point as starting point
  # and search given word
  for row in range(self.R):
    for col in range(self.C):
      if self.search2D(grid, row, col, word):
        print("pattern found at " +
                str(row) + ', ' + str(col))

    
    