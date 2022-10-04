#  File: TestBinaryTree.py

#  Description: creating several trees than seeing if they are working

#  Student Name: Soomin Hyun

#  Student UT EID: sh52679

# Partner Name: Joon Kim (Unique Number: 52595)

# Partner UT EID: jk45873

# Course Name: CS 313E

# Unique Number: 52600

# Date Created: 11/14/21

# Date Last Modified: 11/15/21

import sys

class Node (object):
    def __init__(self, data=None, lchild=None, rchild=None):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild

    # printing statement to help me find the bugs
    def __str__(self):
        return ('{}'.format(self.data))


class Tree (object):
    def __init__(self):
        self.root = None
        # self.size = 0
        # insert data into the tree

    def insert(self, data):
        new_node = Node(data)
        if (self.root == None):
            self.root = new_node
            return
        else:
            current = self.root
            parent = self.root
            while (current != None):
                parent = current
                if (data < current.data):
                    current = current.lchild
                else:
                    current = current.rchild

            if (data < parent.data):
                parent.lchild = new_node
            else:
                parent.rchild = new_node

    # Returns true if two binary trees are similar
    def is_similar(self, pNode):
        return self.is_similar_helper(self.root, pNode.root)

    def is_similar_helper(self, sNode, aNode):
        if (sNode == None and aNode == None):
            return True
        if (sNode != None and aNode != None):
            return (sNode.data == aNode.data) and self.is_similar_helper(sNode.lchild, aNode.lchild) and self.is_similar_helper(sNode.rchild, aNode.rchild)
        return False

    # Returns a list of nodes at a given level from left to right
    def get_level(self, level):
        result = []
        self.get_level_helper(result, self.root, level + 1)
        return result

    def get_level_helper(self, result, aNode, level):
        if (aNode == None):
            return
        elif (level == 1):
            result.append(aNode)
        elif (level > 1):
            self.get_level_helper(result, aNode.lchild, level-1)
            self.get_level_helper(result, aNode.rchild, level-1)


    # Returns the height of the tree
    def get_height (self):
        a = self.get_height_helper(self.root)
        if (a > 0):
            return a - 1
        return a - 1

    def get_height_helper(self, aNode):
        if (aNode == None):
            return 0
        else:
            return 1 + max(self.get_height_helper(aNode.lchild), self.get_height_helper(aNode.rchild))


    # Returns the number of nodes in the left subtree and
    # the number of nodes in the right subtree and the root
    def num_nodes (self):
        return self.num_nodes_helper(self.root)

    def num_nodes_helper(self, aNode):
        if(aNode == None):
            return 0
        return 1 + self.num_nodes_helper(aNode.lchild) + self.num_nodes_helper(aNode.rchild)



def main():
  # Create three trees - two are the same and the third is different
  line = sys.stdin.readline()
  line = line.strip()
  line = line.split()
  tree1_input = list (map (int, line))
  # converts elements into ints

  line = sys.stdin.readline()
  line = line.strip()
  line = line.split()
  tree2_input = list (map (int, line))
  # converts elements into ints

  line = sys.stdin.readline()
  line = line.strip()
  line = line.split()
  # converts elements into ints
  tree3_input = list (map(int, line))

  tree1 = Tree()
  tree2 = Tree()
  tree3 = Tree()
  for i in range(len(tree1_input)):
    tree1.insert(tree1_input[i])
  for i in range(len(tree2_input)):
    tree2.insert(tree2_input[i])
  for i in range(len(tree3_input)):
    tree3.insert(tree3_input[i])

  # Test your method is_similar()
  # This first one should be true
  print('Tree 1 and Tree 2 are similar: {}'. format(tree1.is_similar(tree2)))
  # This one should be false
  print('Tree 1 and Tree 3 are similar: {}'.format(tree1.is_similar(tree3)))
  print()

  # Print the various levels of two of the trees that are different
  # This tests the 0 and 1 levels of trees 1 and 3 because they are different
  print('Tree 1\'s level 0 is:', end=' ')
  levelzero = tree1.get_level(0)
  for i in levelzero:
      print(i, end=' ')
  print()
  print('Tree 1\'s level 1 is:', end = ' ')
  levelone = tree1.get_level(1)
  for i in levelone:
      print(i, end = ' ')
  print()

  print('Tree 3\'s level 0 is:', end=' ')
  levelzero1 = tree3.get_level(0)
  for i in levelzero1:
      print(i, end=' ')
  print()
  print('Tree 3\'s level 1 is:', end=' ')
  levelone1 = tree3.get_level(1)
  for i in levelone1:
      print(i, end=' ')
  print()
  print()

  # Get the height of the two trees that are different
  emptytree = Tree()
  # The height of the first tree should be 3
  print('The height of Tree 1 is: {}'.format(tree1.get_height()))
  # the height of tree 3 is 5 although the number of nodes is the same as 1
  print('The height of Tree 3 is: {}'.format(tree3.get_height()))
  # the height of an empty tree should be -1
  print('The height of an empty tree is: {}'.format(emptytree.get_height()))
  print('The height of Tree 1 and Tree 2 are the same: {}'.format((tree1.get_height() == tree2.get_height())))
  print('The height of Tree 1 and Tree 3 are the same: {}'.format((tree1.get_height() == tree3.get_height())))
  print()

  # Get the total number of nodes a binary search tree
  # The number of nodes for Tree 1 should be 15
  print('The number of nodes for Tree 1 is: {}'.format(tree1.num_nodes()))

'''
Test Cases Print:

Tree 1 and Tree 2 are similar: True
Tree 1 and Tree 3 are similar: False

Tree 1's level 0 is: 50
Tree 1's level 1 is: 30 70
Tree 3's level 0 is: 58
Tree 3's level 1 is: 30 77

The height of Tree 1 is: 3
The height of Tree 3 is: 5
The height of an empty tree is: -1
The height of Tree 1 and Tree 2 are the same: True
The height of Tree 1 and Tree 3 are the same: False

The number of nodes for Tree 1 is: 15
'''

if __name__ == "__main__":
  main()
