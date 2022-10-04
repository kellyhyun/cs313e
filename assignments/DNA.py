
#  File: DNA.py

#  Description:

#  Student Name:

#  Student UT EID:

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number:

#  Date Created:

#  Date Last Modified:

import sys

# Input: s1 and s2 are two strings that represent strands of DNA
# Output: returns a sorted list of substrings that are the longest
#         common subsequence. The list is empty if there are no
#         common subsequences.
def longest_subsequence (s1, s2):
  return

def main():
  # read the number of pairs
  num_pairs = sys.stdin.readline()
  num_pairs = num_pairs.strip()
  num_pairs = int (num_pairs)

  # for each pair call the longest_subsequence
  for i in range (num_pairs):
    st1 = sys.stdin.readline()
    st2 = sys.stdin.readline()

    st1 = st1.strip()
    st2 = st2.strip()

    st1 = st1.upper()
    st2 = st2.upper()

    # get the longest subsequences
    long_sub = longest_subsequence (st1, st2)

    # print the result
    print(long_sub)
    
    # insert blank line

if __name__ == "__main__":
  main()
