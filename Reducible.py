#  File: Reducible.py

#  Description: finding the largest words that can be the most reduced into smaller words

#  Student Name: Soomin Hyun
#
# #  Student UT EID: sh52679
#
# #  Partner Name: Joon Kim (Unique Number: 52595)
#
# #  Partner UT EID: jk45873
#
# #  Course Name: CS 313E
#
# #  Unique Number: 52600
#
# #  Date Created: 10/22/21
#
# #  Date Last Modified: 10/22/21

import sys

# Input: takes as input a positive integer n
# Output: returns True if n is prime and False otherwise
def is_prime ( n ):
  if (n == 1):
    return False

  limit = int (n ** 0.5) + 1
  div = 2
  while (div < limit):
    if (n % div == 0):
      return False
    div += 1
  return True


# Input: takes as input a string in lower case and the size
#        of the hash table
# Output: returns the index the string will hash into
def hash_word (s, size):
  hash_idx = 0
  for j in range (len(s)):
    letter = ord (s[j]) - 96
    hash_idx = (hash_idx * 26 + letter) % size

  return hash_idx


# Input: takes as input a string in lower case and the constant
#        for double hashing
# Output: returns the step size for that string
def step_size (s, const):
  return const - (hash_word(s, const) % const)


# Input: takes as input a string and a hash table
# Output: no output; the function enters the string in the hash table,
#         it resolves collisions by double hashing
def insert_word (s, hash_table):
  hash_index = hash_word(s, len(hash_table))
  if hash_table[hash_index] != '':
    stepsize = step_size(s, 13)
    new_hash_index = hash_index
    while hash_table[new_hash_index] != '':
      new_hash_index = (new_hash_index + stepsize) % len(hash_table)

    hash_table[new_hash_index] = s

  else:
    hash_table[hash_index] = s


# Input: takes as input a string and a hash table
# Output: returns True if the string is in the hash table
#         and False otherwise
def find_word (s, hash_table):
  hash_index = hash_word(s, len(hash_table))
  if hash_table[hash_index] != s:
    stepsize = step_size(s, 13)
    new_hash_index = hash_index
    while hash_table[new_hash_index] != s:
      if hash_table[new_hash_index] == '':
        return False
      new_hash_index = (new_hash_index + stepsize) % len(hash_table)

  return True

def a_i_o(s):
   for i in s:
     if i == 'a' or i == 'i' or i == 'o':
       return True
   return False


# Input: string s, a hash table, and a hash_memo
#        recursively finds if the string is reducible
# Output: if the string is reducible it enters it into the hash memo
#         and returns True and False otherwise
def is_reducible (s, hash_table, hash_memo):
  if len(s) == 1:
    if (s == 'a' or s == 'i' or s == 'o'):
      return True
    return False

  if (a_i_o(s) == False) or (find_word(s,hash_table) == False):
    return False

  if find_word(s, hash_memo):
    return True

  for i in range(len(s)):
    if is_reducible(s[:i]+s[i+1:], hash_table, hash_memo):
      insert_word(s, hash_memo)
      return True



# Input: string_list a list of words
# Output: returns a list of words that have the maximum length
def get_longest_words (string_list):
  max_len_string_list = []

  len_string_list = []
  for el in string_list:
    len_string_list.append(len(el))

  for el in string_list:
    if len(el) == max(len_string_list):
      max_len_string_list.append(el)

  return max_len_string_list


def main():
  # create an empty word_list
  word_list = []

  # read words from words.txt and append to word_list
  for line in sys.stdin:
    line = line.strip()
    word_list.append (line)

  # find length of word_list
  len_word_list = len(word_list)

  # determine prime number N that is greater than twice
  # the length of the word_list
  N = 2 * len_word_list + 1
  contin_loop = True
  while contin_loop:
    if is_prime(N):
      contin_loop = False
    else:
      N += 1


  # create an empty hash_list
  hash_list = []

  # populate the hash_list with N blank strings
  for i in range(N):
    hash_list.append('')

  # hash each word in word_list into hash_list
  # for collisions use double hashing
  for i in range(len_word_list):
    insert_word(word_list[i], hash_list)



  # create an empty hash_memo of size M
  # we do not know a priori how many words will be reducible
  # let us assume it is 10 percent (fairly safe) of the words
  # then M is a prime number that is slightly greater than
  # 0.2 * size of word_list
  hash_memo = []

  M = 27000
  contin_loop_3 = True
  while contin_loop_3:
    if is_prime(M):
      contin_loop_3 = False
    else:
      M += 1


  # populate the hash_memo with M blank strings
  for i in range(M):
    hash_memo.append('')


  # create an empty list reducible_words
  reducible_words = []


  # for each word in the word_list recursively determine
  # if it is reducible, if it is, add it to reducible_words
  # as you recursively remove one letter at a time check
  # first if the sub-word exists in the hash_memo. if it does
  # then the word is reducible and you do not have to test
  # any further. add the word to the hash_memo.
  for word in word_list:
    if is_reducible(word, hash_list, hash_memo):
      reducible_words.append(word)


  # find the largest reducible words in reducible_words
  longest_reducible_words = get_longest_words(reducible_words)


  # print the reducible words in alphabetical order
  # one word per line
  for word in longest_reducible_words:
    print(word)


if __name__ == "__main__":
  main()
