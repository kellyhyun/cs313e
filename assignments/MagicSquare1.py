#  File: MagicSquare.py

#  Description: Making a magic square of the specified number of rows and columns

#  Student Name: Soomin Hyun

#  Student UT EID: sh52679

#  Partner Name: Joon Kim (Unique Number: 52595)

#  Partner UT EID: jk45873

#  Course Name: CS 313E

#  Unique Number: 52600

#  Date Created: 9/7/21

#  Date Last Modified: 9/7/21

import sys

# input: none
# output: the dimension of square, and the number which we find sum of neighbors
def read_input ():
    find_this = sys.stdin.readline()
    n = int(find_this.strip(' \n'))
    find_sums_around = []
    find_this = sys.stdin.readline()
    while find_this != '': #not reading last empty line
        find_this = int(find_this.strip(' \n'))
        find_sums_around.append(find_this)
        find_this = sys.stdin.readline()

    return n, find_sums_around

# input: dimension
# output: magic square with given dimensions
# Populate a 2-D list with numbers from 1 to n2
# This function must take as input an integer. You may assume that
# n >= 1 and n is odd. This function must return a 2-D list (a list of
# lists of integers) representing the square.
# Example 1: make_square(1) should return [[1]]
# Example 2: make_square(3) should return [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
def make_square(n):
    magic_square = []
    for i in range(n): # makes empty list of number with all zeros for square later
        empty_list = []
        for j in range(n):
            empty_list.append(0)
        magic_square.append(empty_list)


    list_of_numbers = [] # makes list of all numbers
    for i in range(1, n**2+1):
        list_of_numbers.append(i)


    row_index = n - 1
    col_index = n // 2
    each_number = 0
    # for loops to make the square
    for i in range(n):
        for j in range(n):
            magic_square[row_index][col_index] = list_of_numbers[each_number]
            each_number += 1

            if j < n:
                row_index += 1
                col_index += 1

                if row_index == n:
                    row_index -= n
                if col_index == n:
                    col_index -= n
        if each_number < n**2:
            row_index -= 2
            col_index -= 1
            magic_square[row_index][col_index] = list_of_numbers[each_number]

    return magic_square

# input: magic square
# output: prints formated square
# Print the magic square in a neat format where the numbers
# are right justified. This is a helper function.
# This function must take as input a 2-D list of integers
# This function does not return any value
# Example: Calling print_square (make_square(3)) should print the output
# 4 9 2
# 3 5 7
# 8 1 6
def print_square(magic_square):
    for i in range(len(magic_square)):
        for j in range(len(magic_square)):
            print('{:3d}'.format(magic_square[i][j]), end=' ') # makes good spacing
        print()

# input: magic square
# output: false if sums aren't right. true if good.
# Check that the 2-D list generated is indeed a magic square
# This function must take as input a 2-D list, and return a boolean
# This is a helper function.
# Example 1: check_square([[1, 2], [3, 4]]) should return False
# Example 2: check_square([[4, 9, 2], [3, 5, 7], [8, 1, 6]]) should return True
def check_square(magic_square):
    overall_test = True
    n = len(magic_square)
    check_sum = n * (n ** 2 + 1) // 2
    for i in range(n): #for loop for checking each row sum
        sum = 0
        for j in range(n):
            sum += magic_square[i][j]
        if sum != check_sum:
            overall_test = False

    for j in range(n): #for loop for checking each col sum
        sum = 0
        for i in range(n):
            sum += magic_square[j][i]
        if sum != check_sum:
            overall_test = False

    row_index = 0
    col_index = 0
    sum = 0

    for i in range(n): #for loop for checking the right diagonal
        sum += magic_square[row_index][col_index]

        row_index += 1
        col_index += 1

    if sum != check_sum:
        overall_test = False

    row_index = 0
    col_index = n - 1
    sum = 0

    for i in range(n): #for loop for checking the left diagonal
        sum += magic_square[row_index][col_index]

        row_index += 1
        col_index -= 1

    if sum != check_sum:
        overall_test = False

    return overall_test


# Input: square is a 2-D list and n is an integer
# Output: returns an integer that is the sum of the
#         numbers adjacent to n in the magic square
#         if n is outside the range return 0
def sum_adjacent_numbers(square, n):
    sum = 0
    for i in range(len(square)):
        for j in range(len(square)):

            if square[i][j] == n:

                for r in range(i-1, i+2):  # two for loops to check all directions
                    for c in range(j-1, j+2):

                        if in_bounds(r, c, square):
                            sum += square[r][c]
                sum -= square[i][j] # subtracts for when i = r and j = c

    return sum



#input: row, col, magic square
#output: true if within square bounds
def in_bounds (r, c, square):
  return 0 <= r < len(square) and 0 <= c < len(square[r])


def main():
    dimension, target_numbers = read_input()
    magic_square = make_square(dimension)
    for n in target_numbers:
        print(sum_adjacent_numbers(magic_square, n))

# read the input file from stdin

# create the magic square

# print the sum of the adjacent numbers

# This line above main is for grading purposes. It will not affect how
# your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN

if __name__ == "__main__":
    main()