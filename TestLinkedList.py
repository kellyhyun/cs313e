#  File: TestLinkedList.py

#  Description: develop the LinkedList class, then write helper methods for it and test them

#  Student Name: Soomin Hyun

#  Student UT EID: sh52679

# Partner Name: Joon Kim (Unique Number: 52595)

# Partner UT EID: jk45873

# Course Name: CS 313E

# Unique Number: 52600

# Date Created: 10/30/21

# Date Last Modified: 11/1/21

class Link(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = None
    # string for the link obj
    def __str__ (self):
        return str(self.data)

class LinkedList(object):
 # create a linked list
 # you may add other attributes
 def __init__ (self):
   self.first = None
   self.last = None

 # get number of links
 def get_num_links (self):
   num_links = 0
   current = self.first

   if current == None:
     return num_links

   while current != None:
     num_links += 1
     current = current.next

   return num_links


 # add an item at the beginning of the list
 def insert_first (self, data):
   new_link = Link(data)
   new_link.next = self.first
   if (self.first == None):
       self.last = new_link
   self.first = new_link

 # add an item at the end of a list
 def insert_last (self, data):
   new_link = Link(data)
   current = self.first
   if current != None:
     self.last.next = new_link
   else:
     self.first = new_link
   self.last = new_link


 # add an item in an ordered list in ascending order
 # assume that the list is already sorted
 def insert_in_order (self, data):
   new_link = Link(data)
   # if the link is empty then insert the first and last as the new link
   if self.first == None:
     self.first = new_link
     self.last = new_link

   else:
    current = self.first
    previous = current
    if current != None:
      # while loop to insert the data when its greater than the current data
      while (current.data < data):
        previous = current
        current = current.next
        if (current == None) and (self.last != None):
          self.last.next = new_link
          self.last = new_link
          return
      # if current is the first list, the first is equal to the new link
      if current == self.first:
        self.first = new_link
      else:
        previous.next = new_link
      new_link.next = current

 # search in an unordered list, return None if not found
 def find_unordered (self, data):
     if (self.first == None):
         return None
     current = self.first
     # while the current data isnt equal to the data keep looking
     while (current.data != data):
         current = current.next
         if (current == None):
             return None
     return current


 # Search in an ordered list, return None if not found
 def find_ordered (self, data):
   current = self.first

   if current == None:
     return None
   # keep looking until you find the data
   while current.data != data:
     #if the data is greater than what we're trying to find then if the data is in order, the data isn't in the list
     if current.data > data:
       return None
     current = current.next
     # if the list is empty, then you won't find the data
     if current == None:
       return None

   return current


 # Delete and return the first occurrence of a Link containing data
 # from an unordered list or None if not found
 def delete_link (self, data):
   current = self.first
   # the list is empty, then return that there's nothing to delete
   if current == None:
     return None
   # else if the data equal to the current, delete it
   elif current.data == data:
     self.first = self.first.next
   # when the data doesnt equal the data, keep going and skipping
   while current.data != data:
     previous = current
     current = current.next
     # once the loop has gone through all and data hasnt been found, return none
     if current == None:
       return None
   if current == self.last:
     self.last = current.next

   return current


 # String representation of data 10 items to a line, 2 spaces between data
 def __str__ (self):
     data_list = []
     print_string = ''
     current = self.first
     if current == None:
         return ''
     # when the current doesn't equal none, append the data to a different list
     while current != None:
         data_list.append(current.data)
         current = current.next
     num_el_count = 0
     # for loop to append each data point into the result string
     for el in data_list:
         if num_el_count % 10 == 0:
             print_string += '\n'
         print_string += str(el)
         print_string += '  '
         num_el_count += 1

     return print_string


 # Copy the contents of a list and return new list
 # do not change the original list
 def copy_list (self):
   new_list = LinkedList()
   if (self.first == None):
       return None
   current = self.first
   # when the current isn't empty, insert the current to the end of a new list
   while (current != None):
     new_list.insert_last(current.data)
     current = current.next

   return new_list



 # Reverse the contents of a list and return new list
 # do not change the original list
 def reverse_list (self):
     new_list = LinkedList()
     if (self.first == None):
         return None
     current = self.first
     # when the current isn't empty, insert the current to the beginning of a new list
     while (current != None):
         new_list.insert_first(current.data)
         current = current.next

     return new_list



 # Sort the contents of a list in ascending order and return new list
 # do not change the original list
 def sort_list (self):
   new_list = LinkedList()
   current = self.first
   if current == None:
     return None
   # when the current isn't empty, insert that data in order
   while current != None:
     new_list.insert_in_order(current.data)
     current = current.next

   return new_list



 # Return True if a list is sorted in ascending order or False otherwise
 def is_sorted (self):
   current = self.first
   next = self.first
   if (self.get_num_links() < 2):
       return True
   while next != None:
     # if the next datapoint is less than the current, then return false
     if next.data < current.data:
       return False
     current = next
     next = next.next
   return True

 # Return True if a list is empty or False otherwise
 def is_empty (self):
   return self.first == None

 # Merge two sorted lists and return new list in ascending order
 # do not change the original lists
 def merge_list (self, other):
   new_list = LinkedList()
   current = self.first
   other_current = other.first
   # if the lists are both empty, then the merged list will be empty
   if current == None and other_current == None:
       return None
   #if neither of them are empty, then continue
   while current != None and other_current != None:
     # if else statement makes sure that we are merging the lists into the correct order
     if current.data < other_current.data:
       new_list.insert_last(current.data)
       current = current.next
     else:
       new_list.insert_last(other_current.data)
       other_current = other_current.next
   # when only current isnt none, then insert the current data
   while current != None:
       new_list.insert_last(current.data)
       current = current.next
   # when only other isnt none, then insert the other data
   while other_current != None:
       new_list.insert_last(other_current.data)
       other_current = other_current.next

   return new_list


 # Test if two lists are equal, item by item and return True
 def is_equal (self, other):
   current = self.first
   other_current = other.first
   if current == None and other_current == None:
     return True
   # when the current and other doesnt equal none, keep checking if all of the spaces are equal
   while current != None and other_current != None:
     # if any of the current data doesnt equal the other data, return false
     if current.data != other_current.data:
       return False
     current = current.next
     other_current = other_current.next
   return True

 # Return a new list, keeping only the first occurence of an element
 # and removing all duplicates. Do not change the order of the elements.
 # do not change the original list
 def remove_duplicates (self):
     new_list = LinkedList()
     current = self.first

     if current == None:
         return None
     #when the current doesnt equal none keep going through the list
     while current != None:
         # if statement takes out the duplicates
         if new_list.find_unordered(current.data) == None:
             new_list.insert_last(current.data)
         current = current.next

     return new_list



def main():
    # Test methods insert_first() and __str__() by adding more than
    # 10 items to a list and printing it.
    linked_list_1 = LinkedList()
    for i in range(11):
        linked_list_1.insert_first(i)
    print(linked_list_1)

    # Test method insert_last()
    linked_list_2 = LinkedList()
    for i in range(11):
        linked_list_2.insert_last(i)
    print(linked_list_2)

    # Test method insert_in_order()
    linked_list_1.insert_in_order(4)
    print(linked_list_1)

    # Test method get_num_links()
    num_links = linked_list_1.get_num_links()
    print(num_links)

    # Test method find_unordered()
    # Consider two cases - data is there, data is not there
    print(linked_list_1.find_unordered(2))

    # Test method find_ordered()
    # Consider two cases - data is there, data is not there
    print(linked_list_2.find_ordered(2))

    # Test method delete_link()
    # Consider two cases - data is there, data is not there
    print(linked_list_1.delete_link(5))

    # Test method copy_list()
    print(linked_list_1)
    print(linked_list_1.copy_list())

    # Test method reverse_list()
    print(linked_list_1.reverse_list())

    # Test method sort_list()
    sorted = linked_list_1.sort_list()
    print(sorted)

    # Test method is_sorted()
    # Consider two cases - list is sorted, list is not sorted
    print(linked_list_1.is_sorted())
    print(sorted.is_sorted())

    # Test method is_empty()
    print(linked_list_1.is_empty())

    # Test method merge_list()
    print(linked_list_1.merge_list(linked_list_2))

    # Test method is_equal()
    # Consider two cases - lists are equal, lists are not equal
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()
    for i in range(15):
        linked_list_3.insert_first(i)
        linked_list_4.insert_first(i)
    print(linked_list_3.is_equal(linked_list_4))
    print(linked_list_1.is_equal(linked_list_2))

    # Test remove_duplicates()
    linked_list_2 = LinkedList()
    list_for_2 = [0, 1, 1, 1, 3, 5, 5, 10, 12]
    for el in list_for_2:
        linked_list_2.insert_first(el)


    print(linked_list_2.remove_duplicates())


if __name__ == "__main__":
    main()