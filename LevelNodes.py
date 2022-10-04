import sys

#  Student Name: Soomin Hyun

#  Student UT EID: sh52679

#  Course Name: CS 313E

#  Unique Number: 52600

#  Date Created: 12/3/2021

#  Date Last Modified: 12/3/2021

# A class to represent a single Node in the Tree
class Node:
    def __init__(self, lChild = None, rChild = None):
        self.lChild = lChild
        self.rChild = rChild

# Input -
#   root: a Node object that represents the root of the tree 
#   row: the row being examined. So, the row containing
#   the root is row 1. The row underneat is row 2. etc.
# Output - an int representing the number of nodes in a given row
def num_level_nodes(root, row):
  # TODO: Implement method to find number of nodes given a row number
  result = []
  get_level_helper(result, root, row)
  return len(result)

def get_level_helper(result, aNode, level):
    if (aNode == None):
        return
    elif (level == 1):
        result.append(aNode)
    elif (level > 1):
        get_level_helper(result, aNode.lChild, level - 1)
        get_level_helper(result, aNode.rChild, level - 1)


def main():
  # add any testing here if you would like
  pass

if __name__ == "__main__":
  main()  
