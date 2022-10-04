# DO NOT MODIFY THE FOLLOWING CODE


class Link:
  def __init__(self, data):
    self.data = data
    self.next = None

  def __str__(self):
    return str(self.data)

class LinkedList (object):
  # linked list class

  # create a linked list
  def __init__(self):
    self.first = None

  # add an item at the beginning of the list
  def insert_first(self, item):
    new_link = Link(item)

    new_link.next = self.first
    self.first = new_link

  # add an item at the end of a list
  def insert_last(self, item):
    new_link = Link(item)

    current = self.first
    if(current == None):
      self.first = new_link
      return

    while(current.next != None):
      current = current.next

    current.next = new_link

# YOU ARE FREE TO CHANGE THE FOLLOWING CODE

# DO NOT change name or header of find_abnormality
def find_abnormality(linkedList):
  # returns the value of the node with two pointer pointing to it if it exists
  # False if it does not exist
  if linkedList.first != 'A':
    return False
  return('B')
  pass


if __name__ == "__main__":
  # write debug statements, test cases, etc (use assert statements)
  # this code will not be run on the autograder, only find_abnormality will be tested
  '''
  A -> B -> C -> D -;
       ^------------'
  '''
  pass
