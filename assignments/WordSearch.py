#  File: WordSearch.py

#  Description: solving crossword puzzle and outputting the word and position

#  Student Name: Soomin Hyun

#  Student UT EID: sh52679

#  Partner Name: Joon Kim (Unique Number: 52595)

#  Partner UT EID: jk45873

#  Course Name: CS 313E 

#  Unique Number: 52600

#  Date Created: 9/2/21

#  Date Last Modified: 9/3/21

import sys

# Input: None
# Output: function returns a 2-D list that is the grid of letters and
# 1-D list of words to search
def read_input ( ):
  grid = []
  words = []

  number_of_characters = sys.stdin.readline()
  nString = number_of_characters.strip() # strip the newline character at the end
  n = int(nString) #turn into a int for later for loop
  sys.stdin.readline() #skipping the blank line

  for i in range(n): #for loop to make the grid
    line = sys.stdin.readline(" \n")
    lineStrip = line.strip()
    characters = lineStrip.split()
    grid.append(characters)

  sys.stdin.readline() #to skip blank line
  number_of_words = sys.stdin.readline() #reading the line to find number of words in the list
  wString = number_of_words.strip()
  w = int(wString)

  for i in range(w): #for loop to read each word
    line = sys.stdin.readline()
    word = line.strip()
    words.append(word)

  sys.stdin.close()

  return grid, words


# Input: a 2-D list representing the grid of letters and a single
#        string representing the word to search
# Output: returns a tuple (i, j) containing the row number and the
#         column number of the word that you are searching 
#         or (0, 0) if the word does not exist in the grid
def find_word (grid, word):
  go = False #initializing the variable so that the position is not stored when it shouldn't be
  position_tuple = tuple() #initializing tuple

  target_letters = [] #initializing lists
  ################################################
  for char in word:  #make each char a different element on list
    target_letters.append(char)

  if len(target_letters) <= 1: #for words that are only one letter
    for i in range(len(grid)):
      for j in range(len(grid)):

        if grid[i][j] == target_letters[0]:
          return ('({}, {})'.format(str(i + 1), str(j + 1)))

    ################################################
  else: #for all other target words
    for i in range(len(grid)): #two for loops to read entire grid
      for j in range(len(grid)):

        if grid[i][j] == target_letters[0]: #target letter matches grid letter
          for r in range(i-1, i+2): #two for loops to check all directions
            for c in range(j-1, j+2):

              if in_bounds(r, c, grid): #check letter we're finding is in grid
                if grid[r][c] == target_letters[1]: #check that second grid letter is same as second target letter
              ##############################
                  row_dir = r-i #finding what row direc
                  col_dir = c-j #finding col direction
                  new_r = r
                  new_c = c
                  go = True #true will store our location
                  for each in range(2, len(target_letters)): #will check all letters of word with the line in grid

                    new_r += row_dir
                    new_c += col_dir
                    if in_bounds(new_r, new_c, grid): #makes sure the letter is in grid
                      if grid[new_r][new_c] != target_letters[each]:
                        go = False #don't store location if the letter in grid is not the same as target_letter
                    else:
                      go = False #if not in bounds, don't store the location
                if go:
                  return ('({}, {})'.format(str(i+1), str(j+1))) #add 1 to i and j to make it the correct location
                  go = False

  return (0, 0) #returning (0,0) if the word is not found in grid


# Input: r, c, grid
# Output: returns boolean depending on whether the row and column inputted are within the specified grid limits
def in_bounds (r, c, grid):
  return 0 <= r < len(grid) and 0 <= c < len(grid[r])

# Input: other methods
# output: actions of other methods specified above
def main():
  # read the input file from stdin
  word_grid, word_list = read_input()
  find_word(word_grid, word_list)

  # find each word and print its location
  for word in word_list:
    location = find_word(word_grid, word)
    print (word + ": " + str(location))

if __name__ == "__main__":

 main()