
#  File: Boxes.py

#  Description: finding how many boxes fit inside each other

#  Student Name: Soomin Hyun

#  Student UT EID: sh52679

#  Partner Name: Joon Kim (Unique Number: 52595)

#  Partner UT EID: jk45873

#  Course Name: CS 313E

#  Unique Number: 52600

#  Date Created: 10/12/21

#  Date Last Modified: 10/12/21


import sys

# Input: 2-D list of boxes. Each box of three dimensions is sorted
#        box_list is sorted
# Output: function returns two numbers, the maximum number of boxes
#         that fit inside each other and the number of such nesting
#         sets of boxes
def nesting_boxes (box_list):
  max_list = []
  max_indeces = []
  num_sets = 0

  for i in range(len(box_list)):
    max_list.append([0, 1])

  # go through each box and determine its N(i) value and the number of subsets of nested boxes it has
  for i in range(len(box_list)):
    each_max_list = []
    max_list[i][0], max_list[i][1] = helper_nesting_function(box_list, i, i, max_list, each_max_list)

  # determines the largest number of nested boxes
  max_value = max(max_list, key=lambda x: x[0])[0]

  # stores the index value of the boxes that have a N(i) value equal to the largest number of nested boxes
  for i in range(len(max_list)):
    if max_list[i][0] == max_value:
      max_indeces.append(i)

  # adds the number of subsets of each of the box that has the largest number of nested boxes
  for ind in max_indeces:
    num_sets += max_list[ind][1]

  return max_value, num_sets

# nesting boxes helper function for recursion
def helper_nesting_function(box_list, box_1, box_2, max_list, each_max_list):
  # determine maximum number of nested boxes and number of subsets when went through all boxes
  if box_2 < 0:
    max_num = max(each_max_list)
    max_num_indeces = []
    num_subsets = 0

    # if the box fits none of the other boxes, return N(i) = 1 and number of subsets = 1
    if max_num == 1:
      return 1,1

    # stores index values of the boxes that have the largest number of nested boxes
    for i in range(len(each_max_list)):
      if each_max_list[i] == max_num:
        max_num_indeces.append(box_1 - i)

    for ind in max_num_indeces:
      num_subsets += max_list[ind][1]

    return max_num, num_subsets

  # second box fits n the first box, then have the function run again
  elif does_fit(box_list[box_2], box_list[box_1]):
    each_max_list.append(max_list[box_2][0] + 1)
    return helper_nesting_function(box_list, box_1, box_2 - 1, max_list, each_max_list)

  # if the box doesn't fit then the list run through the fuction once more to the next box
  else:
    each_max_list.append(1)
    return helper_nesting_function(box_list, box_1, box_2 - 1, max_list, each_max_list)








# returns True if box1 fits inside box2
def does_fit (box1, box2):
  return (box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2])

def main():
  # read the number of boxes
  line = sys.stdin.readline()
  line = line.strip()
  num_boxes = int (line)

  # create an empty list for the boxes
  box_list = []

  # read the boxes from the file
  for i in range (num_boxes):
    line = sys.stdin.readline()
    line = line.strip()
    box = line.split()
    for j in range(len(box)):
      box[j] = int(box[j])
    box.sort()
    box_list.append(box)

  '''
  # print to make sure that the input was read in correctly
  print (box_list)
  print()
  '''

  # sort the box list
  box_list.sort()

  '''
  # print the box_list to see if it has been sorted.
  print (box_list)
  print()
  '''

  # get the maximum number of nesting boxes and the
  # number of sets that have that maximum number of boxes
  max_boxes, num_sets = nesting_boxes (box_list)

  # print the largest number of boxes that fit
  print (max_boxes)

  # print the number of sets of such boxes
  print (num_sets)

if __name__ == "__main__":
  main()