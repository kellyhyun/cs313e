
#  File: Triangle.py

#  Description: finding the greatest path sum using different methods

#  Student Name: Soomin Hyun

#  Student UT EID: sh52679

#  Partner Name: Joon Kim (Unique Number: 52595)

#  Partner UT EID: jk45873

#  Course Name: CS 313E

#  Unique Number: 52600

#  Date Created: 10/6/21

#  Date Last Modified: 10/6/21


import sys

from timeit import timeit

# returns the greatest path sum using exhaustive search
def brute_force (grid):
 all_possible_sums = []
 brute_force_helper(grid, 0, grid[0][0], all_possible_sums, 0)

 return max(all_possible_sums)


def brute_force_helper (grid, col_position, sum, all_possible_sums, n):
 if n == len(grid)-1:
   all_possible_sums.append(sum)
 else:
   brute_force_helper(grid, col_position, sum+grid[n+1][col_position], all_possible_sums, n+1)
   brute_force_helper(grid, col_position+1, sum+grid[n+1][col_position+1], all_possible_sums, n+1)


# returns the greatest path sum using greedy approach
def greedy (grid):
 sum = grid[0][0]
 row_position = 1
 col_position = 0

 while row_position < len(grid) :
   if grid[row_position][col_position] > grid[row_position][col_position+1]:
    col_position = col_position
   elif grid[row_position][col_position+1] > grid[row_position][col_position]:
    col_position += 1
   else:
    temp_row_position = row_position
    position_1 = col_position
    position_2 = col_position + 1
    temp_pos_1 = position_1
    temp_pos_2 = position_2

    while grid[temp_row_position][temp_pos_1] == grid[temp_row_position][temp_pos_2]:
      temp_row_position += 1

      # What if the next two numbers under one column position are the same?
      if grid[temp_row_position][temp_pos_1] > grid[temp_row_position][temp_pos_1+1]:
        temp_pos_1 = temp_pos_1
      else:
        temp_pos_1 += 1

      if grid[temp_row_position][temp_pos_2] > grid[temp_row_position][temp_pos_2+1]:
        temp_pos_2 = temp_pos_2
      else:
        temp_pos_2 += 1

    if grid[temp_row_position][temp_pos_1] > grid[temp_row_position][temp_pos_2]:
      col_position = position_1
    else:
      col_position = position_2

   sum += grid[row_position][col_position]

   row_position += 1

 return sum


# returns the greatest path sum using divide and conquer (recursive) approach
def divide_conquer (grid):
  max_value = divide_conquer_helper(grid, 0, grid[0][0], 0)
  return max_value


def divide_conquer_helper(grid, col_position, sum, n):
 if n == len(grid)-1:
   return sum
 else:
   return max(divide_conquer_helper(grid, col_position, sum+grid[n+1][col_position], n+1), divide_conquer_helper(grid, col_position+1, sum+grid[n+1][col_position+1], n+1))

# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog (grid):
 new_grid = grid[:]
 for i in range(-1, -len(grid), -1):
   for j in range(len(grid[i])-1):
    if grid[i][j] > grid[i][j+1]:
      new_grid[i-1][j] += new_grid[i][j]
    else:
      new_grid[i-1][j] += new_grid[i][j+1]

 return new_grid[0][0]


# reads the file and returns a 2-D list that represents the triangle
def read_file ():
 # read number of lines
 line = sys.stdin.readline()
 line = line.strip()
 n = int (line)

 # create an empty grid with 0's
 grid = [[0 for i in range (n)] for j in range (n)]

 # read each line in the input file and add to the grid
 for i in range (n):
   line = sys.stdin.readline()
   line = line.strip()
   row = line.split()
   row = list (map (int, row))
   for j in range (len(row)):
     grid[i][j] = grid[i][j] + row[j]

 return grid

def main ():
 # read triangular grid from file
 grid = read_file()


 '''
 # check that the grid was read in properly
 print (grid)
 '''

 # output greatest path from exhaustive search
 times = timeit ('brute_force({})'.format(grid), 'from __main__ import brute_force', number = 10)
 times = times / 10
 # print time taken using exhaustive search
 print('The greatest path sum through exhaustive search is ')
 print(brute_force(grid))
 print('The time taken for exhaustive search in seconds is')
 print(times)
 print()

 # output greatest path from greedy approach
 times = timeit ('greedy({})'.format(grid), 'from __main__ import greedy', number = 10)
 times = times / 10
 # print time taken using greedy approach
 print('The greatest path sum through greedy search is ')
 print(greedy(grid))
 print('The time taken for greedy search in seconds is')
 print(times)
 print()


 # output greatest path from divide-and-conquer approach
 times = timeit ('divide_conquer({})'.format(grid), 'from __main__ import divide_conquer', number = 10)
 times = times / 10
 # print time taken using divide-and-conquer approach
 print('The greatest path sum through recursive search is ')
 print(divide_conquer(grid))
 print('The time taken for recursive search in seconds is')
 print(times)
 print()

 # output greatest path from dynamic programming
 times = timeit ('dynamic_prog({})'.format(grid), 'from __main__ import dynamic_prog', number = 10)
 times = times / 10
 # print time taken using dynamic programming
 print('The greatest path sum through dynamic programming is ')
 print(dynamic_prog(grid))
 print('The time taken for dynamic programming in seconds is')
 print(times)

if __name__ == "__main__":
 main()



