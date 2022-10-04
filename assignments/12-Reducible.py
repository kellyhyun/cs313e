#  File: Reducible.py

#  Description:This program tries to find the longest reducible word(s) from a given file
#              of words.

#  Student Name: Louie Wang

#  Student UT EID: zw5565

#  Course Name: CS 313E

#  Unique Number: 50305

#  Date Created: Mar 22

#  Date Last Modified: April 1

# takes as input a positive integer n
# returns True if n is prime and False otherwise
def is_prime (n):
    if n == 1:
        return False
    limit = int(n**0.5) + 1
    div = 2
    while div < limit:
        if n % div == 0:
            return False
        div += 1
    return True
# takes as input a string in lower case and the size
# of the hash table and returns the index the string
# will hash into
def hash_word (s, size):
    hash_idx = 0
    for j in range (len(s)):
        letter = ord(s[j]) - 96
        hash_idx = (hash_idx*26 + letter) % size
    return hash_idx
# takes as input a string in lower case and the constant
# for double hashing and returns the step size for that 
# string
def step_size (s, const):
    key = hash_word(s,const)
    return (const - key % const)
# takes as input a string and a hash table and enters
# the string in the hash table, it resolves collisions
# by double hashing
def insert_word (s, hash_table):
    idx = hash_word(s,len(hash_table))
    step = step_size(s,13)
    if hash_table[idx] == '':
        hash_table[idx] = s
    else:
        new = idx + step
        while hash_table[new] != '':
            new = (new + step) % len(hash_table)
        hash_table[new] = s
# takes as input a string and a hash table and returns True
# if the string is in the hash table and False otherwise
def find_word (s, hash_table):
    idx = hash_word(s,len(hash_table))
    step = step_size(s,13)
    if hash_table[idx] == s:
        return True
    if hash_table[idx] == '':
        return False
    new = (idx + step) % len(hash_table)
    while True:
        if hash_table[new] == s:
            return True
        elif hash_table[new] == '':
            return False
        new = (new + step) % len(hash_table)
# recursively finds if a word is reducible, if the word is
# reducible it enters it into the hash memo and returns True
# and False otherwise
def vowel(s):
    for i in s:
        if i == 'a' or i == 'i' or i == 'o':
            return True
    return False
def is_reducible (s, hash_table, hash_memo):
    if len(s) == 1:
        if s in ['a','i','o']:
            return True
        else:
            return False
    else:
        if (vowel(s) == False) or (find_word(s,hash_table) == False):
            return False
        elif find_word(s,hash_memo):
            return True
        else:
            for i in range(len(s)):
                after = s[:i] + s[i+1:]
                if is_reducible(after,hash_table,hash_memo):
                    insert_word(after,hash_memo)
                    return True
            return False
# goes through a list of words and returns a list of words
# that have the maximum length
def get_longest_words (string_list):
    length = []
    words = []
    for i in string_list:
        length.append(len(i))
    m = max(length)
    for word in string_list:
        if len(word) == m:
            words.append(word)
    return words
def main():
  # create an empty word_list
    word_list = []
  # open the file words.txt
    file = open('words.txt','r')
  # read words from words.txt and append to word_list
    for words in file.readlines():
        word_list.append(words.strip())
  # close file words.txt
    file.close()
  # find length of word_list
    size = len(word_list)
  # determine prime number N that is greater than twice
  # the length of the word_list
    N = 2 * size
    while not is_prime(N):
        N += 1
  # create an empty hash_list
    hash_list = []
  # populate the hash_list with N blank strings
    for n in range(N):
        hash_list.append('')
  # hash each word in word_list into hash_list
  # for collisions use double hashing
    for word in word_list:
        insert_word(word,hash_list)
  # create an empty hash_memo of size M
  # we do not know a priori how many words will be reducible
  # let us assume it is 10 percent (fairly safe) of the words
  # then M is a prime number that is slightly greater than 
  # 0.2 * size of word_list
    M = 27000
    while not is_prime(M):
        M += 1
    hash_memo = []
  # populate the hash_memo with M blank strings
    for m in range(M):
        hash_memo.append('')
  # create and empty list reducible_words
    reducible_words = []
  # for each word in the word_list recursively determine
  # if it is reducible, if it is, add it to reducible_words
    for word in word_list:
        if is_reducible(word,hash_list,hash_memo):
            reducible_words.append(word)
    #reducible_words.remove('complecting')
  # find words of the maximum length in reducible_words
    longest = get_longest_words(reducible_words)
  # print the words of maximum length in alphabetical order
  # one word per line
    longest.sort()
    for s in longest:
        print(s)
##    print('size of word list', size)
##    print('size of hash_list', len(hash_list))
##    print('size of hash memo', len(hash_memo))
##    print('size of reducible words: ',len(reducible_words))
##    print('size of second longest reducible words: ', len([i for i in reducible_words if len(i) == 10]))
##    
# This line above main is for grading purposes. It will not 
# affect how your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
    main()
