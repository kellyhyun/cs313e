
#  File: MagicSquare.py

#  Description: creating magic squares with permuations

#  Student Name: Soomin Hyun
#
# Student UT EID: sh52679
#
# Partner Name: Joon Kim (Unique Number: 52595)
#
# Partner UT EID: jk45873
#
# Course Name: CS 313E
#
# Unique Number: 52600
#
# Date Created: 10/25/21
#
# Date Last Modified: 10/27/21

import sys

# checks if a 1-D list if converted to a 2-D list is magic
# a is 1-D list of integers
# returns True if a is magic and False otherwise
def is_magic ( a ):
  n = int((len(a))**.5)
  magic_constant = (n * (n**2 + 1)) // 2
  a2 = []
  index = 0

  for i in range(n):
    new_line = []
    for j in range(n):
      new_line.append(a[index])
      index += 1
    a2.append(new_line)


  for i in range(n):
    row_sum = 0
    col_sum = 0
    for j in range(n):
      row_sum += a2[i][j]
      col_sum += a2[j][i]
    if (row_sum != magic_constant or col_sum != magic_constant):
      return False

    start_left_diag = 0
    start_right_diag = 0
    for i in range(n):
      start_left_diag += a2[i][i]
      start_right_diag += a2[n-i-1][i]
    if (start_left_diag != magic_constant or start_right_diag != magic_constant):
      return False
  return True

# this function recursively permutes all magic squares
# a is 1-D list of integers and idx is an index in a
# function stores all 1-D lists that are magic in the list all_magic
def permute (a, idx, all_magic):
  hi = len(a)
  magic_constant = len(a) * ((len(a)) ** 2 + 1) // 2
  if (idx == hi) and is_magic(a):
    print(a)
    all_magic.append(a)

  elif (idx == hi - hi ** 0.5):
    current_col_sum = []
    step_size = hi ** 0.5
    for i in range(int(hi ** 0.5)):
      sum = 0
      for j in range(int(hi ** 0.5 - 1)):
        sum += a[i + j * step_size]
      current_col_sum.append(sum)

    for i in range(int(hi ** 0.5)):
      a[idx + i] = magic_constant - current_col_sum[i]

    permute(a, len(a), all_magic)

  else:
    for i in range(idx, hi):
      a[idx], a[i] = a[i], a[idx]
      if idx % int(len(a) ** 0.5) == 0:
        if check_row_sum(a, int(len(a) ** 0.5)):
          permute(a, idx + 1, all_magic)
        else:
          return
      permute(a, idx + 1, all_magic)
      a[idx], a[i] = a[i], a[idx]


def check_row_sum (a, n):
  magic_constant = len(a) * ((len(a))**2 + 1) // 2
  for i in range(n-1):
    sum = a[n*i:n*(i+1)+1]
    if sum != magic_constant:
      return False
  return True

def main():
  # read the dimension of the magic square
  line = sys.stdin.readline()
  line = line.strip()
  n = int (line)

  # create an empty list for all magic squares
  all_magic = []

  # create the 1-D list that has the numbers 1 through n^2
  list_int = []
  for i in range(n**2):
    list_int.append(i+1)

  # generate all magic squares using permutation 
  all_magic = permute(list_int, 0, all_magic)

  print(all_magic)

  # print all magic squares
  #for square in all_magic:
    #print (square)

if __name__ == "__main__":
  main()

