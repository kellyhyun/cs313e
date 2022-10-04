#  File: Radix.py

#  Description: sorting a list of numbers and letters in a specific way

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
# Date Created: 10/27/21
#
# Date Last Modified: 10/27/21

import sys

class Queue (object):
  def __init__ (self):
    self.queue = []

  # add an item to the end of the queue
  def enqueue (self, item):
    self.queue.append (item)

  # remove an item from the beginning of the queue
  def dequeue (self):
    return (self.queue.pop(0))

  # check if the queue if empty
  def is_empty (self):
    return (len(self.queue) == 0)

  # return the size of the queue
  def size (self):
    return (len(self.queue))

  def __str__(self):
    return '({})'.format(self.queue)

# Input: a is a list of strings that have either lower case
#        letters or digits
# Output: returns a sorted list of strings
def radix_sort (a):
  que_list = []
  for i in range(37):
    que_list.append(Queue())

  # find the longest string and enque all elements in the last Que
  length_list = []
  for i in range(len(a)):
    que_list[-1].enqueue(a[i])
    length_list.append(len(a[i]))

  longest_string_length = max(length_list)

  alphabet_list = list('abcdefghijklmnopqrstuvwxyz')

  for i in range(longest_string_length):
    real_index = longest_string_length - i - 1
    while (que_list[-1].is_empty()) != True:
      current_element = que_list[-1].dequeue()
      if len(current_element) < longest_string_length - i:
        que_list[0].enqueue(current_element)

      elif current_element[real_index].isdigit():
        que_index = int(current_element[real_index]) // 1
        que_list[que_index].enqueue(current_element)

      else:
        for char in alphabet_list:
          if current_element[real_index] == char:
            que_index = alphabet_list.index(char)
            que_index += 10
            que_list[que_index].enqueue(current_element)

    for i in range(36):
      while (que_list[i].is_empty()) != True:
        temp = que_list[i].dequeue()
        que_list[-1].enqueue(temp)

  for i in range(len(que_list)):
    sorted_list = []

  while (que_list[-1].is_empty()) != True:
    current_element = que_list[-1].dequeue()
    sorted_list.append(current_element)

  return sorted_list


def main():
  # read the number of words in file
  line = sys.stdin.readline()
  line = line.strip()
  num_words = int(line)

  # create a word list
  word_list = []
  for i in range(num_words):
    line = sys.stdin.readline()
    word = line.strip()
    word_list.append(word)

  '''
  # print word_list
  print (word_list)
  '''

  # use radix sort to sort the word_list
  sorted_list = radix_sort(word_list)

  # print the sorted_list
  print(sorted_list)


if __name__ == "__main__":
  main()



