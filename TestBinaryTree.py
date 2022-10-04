#  File: TestBinaryTree.py

'''
 Description: Use get_height() function in programming assignment to determine the
balance factor of a node and then determine if the tree is balanced. Implement
get_balance_factor (self, aNode) returns the absolute value of difference in height of left and right subtree
is_balanced (self) returns true if balanced and false if not balanced. A balanced tree has a absolute difference no more than 1
'''
#  Student Name: Soomin Hyun

#  Student UT EID: sh52679

#  Course Name: CS 313E

#  Unique Number: 52600

#  Date Created: 12/3/2021

#  Date Last Modified: 12/3/2021

import sys
import random
class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lChild = None
    self.rChild = None
    # self.parent = None
    # self.visited = False

  def __str__ (self):
    s = ''
    return s

class Tree (object):
  def __init__ (self):
    self.root = None
    # self.size = 0

  # Insert a node in the tree
  def insert (self, val):
    newNode = Node (val)

    if (self.root == None):
      self.root = newNode
    else:
      current = self.root
      parent = self.root
      while (current != None):
        parent = current
        if (val < current.data):
                current = current.lChild
        else:
          current = current.rChild

      if (val < parent.data):
        parent.lChild = newNode
      else:
        parent.rChild = newNode

  # takes in the current node and the current height and returns the new height
  def height_helper(self, aNode):
    a = self.get_height_helper(aNode)
    if (a > 0):
      return a - 1
    return a - 1

  def get_height_helper(self, aNode):
    if (aNode == None):
      return 0
    else:
      return 1 + max(self.get_height_helper(aNode.lChild), self.get_height_helper(aNode.rChild))

  # returns the absolute value of difference in height of left and right subtree
  def get_balance_factor (self, aNode):
    l_child = aNode.lChild
    r_child = aNode.rChild
    lheight = self.height_helper(l_child)
    rheight = self.height_helper(r_child)
    return abs(lheight-rheight)

  # returns true if balanced and false if not balanced. A balanced tree has a balance factor no more than 1
  def is_balanced (self, aNode):
    balance_factor = self.get_balance_factor(aNode)
    return balance_factor <= 1
      

      

 
def main():
    # DO NOT MODIFY MAIN
    # Create three trees - two are the same and the third is different
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree1_input = list (map (int, line)) 	# converts elements into ints
    tree1 = Tree()
    for i in tree1_input:
        tree1.insert(i)
    print(tree1.is_balanced(tree1.root))

if __name__ == "__main__":
  main()