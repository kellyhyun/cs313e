#  File: OfficeSpace.py

#  Description:

#  Student Name: Soomin Hyun

#  Student UT EID: sh52679

#  Partner Name: Joon Kim (Unique Number: 52595)

#  Partner UT EID: jk45873

#  Course Name: CS 313E

#  Unique Number: 52600

#  Date Created:9/21/21

#  Date Last Modified:9/21/21

import sys


# Input: a rectangle which is a tuple of 4 integers (x1, y1, x2, y2)
# Output: an integer giving the area of the rectangle
def area (rect):
  x1, x2, y1, y2 = rect[0], rect[2], rect[1], rect[3]
  area_int = abs(x1-x2)*abs(y1-y2) # absolute values are there so that we always get the value of length and width
  return area_int

# Input: two rectangles in the form of tuples of 4 integers
# Output: a tuple of 4 integers denoting the overlapping rectangle.
#         return (0, 0, 0, 0) if there is no overlap
def overlap (rect1, rect2):
  new_x1, new_x2, new_y1, new_y2 = 0, 0, 0, 0 # initiailzingthe overlap so that if there is no overlap, it returns (0, 0, 0, 0)
  r1x1, r1x2, r1y1, r1y2 = rect1[0], rect1[2], rect1[1], rect1[3] # coords of rect 1
  r2x1, r2x2, r2y1, r2y2 = rect2[0], rect2[2], rect2[1], rect2[3] # coords of rect 2
  # only execute if the smaller x or y coord of the 2nd rectangle is between coords of the other rect
  # makes sure that this only executes when there is an overlap
  if r1x1 < r2x1 < r1x2 or r1y1 < r2y1 < r1y2:
    new_x1, new_x2, new_y1, new_y2 = max(r1x1, r2x1), min(r1x2, r2x2), max(r1y1, r2y1), min(r1y2, r2y2)
  return (new_x1, new_y1, new_x2, new_y2)


# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the unallocated
#         space in the office
def unallocated_space (bldg):
  area = 0
  # using both for loops to check each cell of the 2D array
  for row in range(len(bldg)):
    for col in range(len(bldg[row])):
      if bldg[len(bldg) - row - 1][col] == 0: # if no one wanted this cell
        area += 1 # then add one unrequested cell to the total unallocated area

  return area


# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the contested
#         space in the office
def contested_space (bldg):
  area = 0
  # using both for loops to check each cell of the 2D array
  for row in range(len(bldg)):
    for col in range(len(bldg[row])):
      if bldg[len(bldg) - row - 1][col] >= 2:
        area += 1

  return area

# Input: bldg is a 2-D array representing the whole office space
#        rect is a rectangle in the form of a tuple of 4 integers
#        representing the cubicle requested by an employee
# Output: a single integer denoting the area of the uncontested
#         space in the office that the employee gets
def uncontested_space (bldg, rect):
  x1, x2, y1, y2 = rect[0], rect[2], rect[1], rect[3]
  area = 0
  # using both for loops to check each cell of the 2D array
  for row in range(len(bldg)):
    for col in range(len(bldg[row])):
      # if the cell is within what was requested and they are the only people who requested it
      if x1 <= col < x2 and y1 <= row < y2 and bldg[len(bldg) - row - 1][col] == 1:
        area += 1
  return area

# Input: office is a rectangle in the form of a tuple of 4 integers
#        representing the whole office space
#        cubicles is a list of tuples of 4 integers representing all
#        the requested cubicles
# Output: a 2-D list of integers representing the office building and
#         showing how many employees want each cell in the 2-D list
def request_space (office, cubicles):
  office_grid = []
  o_x1, o_x2, o_y1, o_y2 = office[0], office[2], office[1], office[3]

  for col in range(o_y2):
    office_grid_line = []
    for row in range(o_x2):
      office_grid_line.append(0)
    office_grid.append(office_grid_line)

  for tuple in cubicles:
    # using both for loops to check each cell of the 2D array
    for row in range(len(office_grid)):
      for col in range(len(office_grid[row])):
        # if the cell is within the range of the request, add one
        if tuple[0] <= col < tuple[2] and tuple[1] <= row < tuple[3]:
          office_grid[len(office_grid) - row - 1][col] += 1


  return office_grid


# Input: no input
# Output: a string denoting all test cases have passed
def test_cases ():
  # assert area ((0, 0, 1, 1)) == 1
  # write your own test cases
  # test cases were written and deleted because they weren't needed anymore.
  return "all test cases passed"

def main():
  # read the data
  read_office_space = sys.stdin.readline()
  read_office_space = read_office_space.strip(' \n')
  read_num_employees = sys.stdin.readline()
  num_employees = int(read_num_employees.strip(' \n'))
  names = []
  space_requests = []

  # for the number of employees, read the lines and record their names and requests as strings and tuples respectively
  for i in range(num_employees):
    read_name_and_requests = sys.stdin.readline()
    read_name_and_requests = read_name_and_requests.strip(' \n')

    name_and_requests = read_name_and_requests.split()
    new_name = name_and_requests[0]
    names.append(new_name)
    new_tuple = (int(name_and_requests[1]), int(name_and_requests[2]), int(name_and_requests[3]), int(name_and_requests[4]))
    space_requests.append(new_tuple)

  read_office_space = read_office_space.split()
  office_space_tuple = (0, 0, int(read_office_space[0]), int(read_office_space[1]))

  # run your test cases
  '''
  print (test_cases())
  '''

  building = request_space(office_space_tuple, space_requests)

  # print the following results after computation
  # compute the total office space
  total_office_area = area(office_space_tuple)

  # compute the total unallocated space
  total_unallocated_space = unallocated_space(building)

  # compute the total contested space
  total_contested_space = contested_space(building)

  # compute the uncontested space that each employee gets
  uncontested_space_list = []
  # make a new list of the employees requested space that wasn't contested
  for i in range(num_employees):
    uncontested_space_list.append(uncontested_space(building, space_requests[i]))

  # print the results here:
  print('Total {}'.format(total_office_area))
  print('Unallocated {}'.format(total_unallocated_space))
  print('Contested {}'.format(total_contested_space))
  # for loop so that it prints all the employees and the requested space
  for i in range(num_employees):
    print('{} {}'.format(names[i], uncontested_space_list[i]))

if __name__ == "__main__":
  main()