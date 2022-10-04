#  File: WordSearch2Test.py

#  Description: solving crossword puzzle.

#  Student Name: Soomin Hyun

#  Student UT EID: sh52679

#  Partner Name: Joon Kim (Unique Number: 52595)

#  Partner UT EID: jk45873

#  Course Name: CS 313E 

#  Unique Number: 52600

#  Date Created: 9/2/21

#  Date Last Modified:

import sys

# Input: None
# Output: function returns a 2-D list that is the grid of letters and
# 1-D list of words to search
def read_input ( ):
  grid = []
  words = []

  number_of_characters = sys.stdin.readline()
  nString = number_of_characters.rstrip("\n")
  n = int(nString)
  sys.stdin.readline()

  for i in range(n):
    line = sys.stdin.readline()
    lineStrip = line.rstrip("\n")   # strip the newline character at the end
    characters = lineStrip.split()
    grid.append(characters)

  sys.stdin.readline()
  number_of_words = sys.stdin.readline()
  wString = number_of_words.rstrip("\n")
  w = int(wString)

  for i in range(w):
    line = sys.stdin.readline()
    word = line.rstrip("\n")   # strip the newline character at the end)
    words.append(word)

  sys.stdin.close()

  return grid, words

# Input: a 2-D list representing the grid of letters and a single
#        string representing the word to search
# Output: returns a tuple (i, j) containing the row number and the
#         column number of the word that you are searching 
#         or (0, 0) if the word does not exist in the grid


def find_word (grid, word):
  word_and_position = {}
  go = False
  position_tuple = tuple()

  target_letters = []
  ################################################
  for char in word:
    target_letters.append(char)

  #print(target_letters)
  ################################################

  for i in range(len(grid)):
    for j in range(len(grid)):

      if grid[i][j] == target_letters[0]:
        for r in range(i, i+1):
          for c in range(j+1, j+2):

            if in_bounds(r, c, grid):
              if grid[r][c] == target_letters[1]:
                  ##############################
                row_dir = r-i
                col_dir = c-j
                new_r = r
                new_c = c
                go = True
                for each in range(2, len(target_letters)):

                  new_r += row_dir
                  new_c += col_dir
                  if in_bounds(new_r, new_c, grid):
                    if grid[new_r][new_c] != target_letters[each]:
                      go = False
                  else:
                    go = False
      if go:
        position_tuple = ('({}, {})'.format(str(i+1),str(j+1)))
        go = False
  return position_tuple

  #for target_word in word:
    #print('{}: {}'.format(target_word, word_and_position[target_word]))


def in_bounds (r, c, grid):
  return 0 <= r < len(grid) and 0 <= c < len(grid[r]) #and (i!=r and j!=c)


def main():
  # read the input file from stdin

  word_grid, word_list = read_input()
  find_word(word_grid, word_list)
  print(word_grid)

  # find each word and print its location
  for word in word_list:
    location = find_word(word_grid, word)
    print (word + ": " + str(location))

if __name__ == "__main__":

 main()
