#  File: TestCipher.py

#  Description:

#  Student Name: Soomin Hyun

#  Student UT EID: sh52679

#  Partner Name: Joon Kim (Unique Number: 52595)

#  Partner UT EID: jk45873

#  Course Name: CS 313E

#  Unique Number: 52600

#  Date Created: 9/10/21

#  Date Last Modified:

import sys


#  Input: strng is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of strng
#  Output: function returns a single string that is encoded with
#          rail fence algorithm
def rail_fence_encode(strng, key):
    append_this = []
    fence_to_fill = []
    list_of_char = list(strng)

    for i in range(key):
        empty_row = []
        for j in range(len(strng)):
            empty_row.append(0)
        fence_to_fill.append(empty_row)

    position = 0
    direction = 1
    for change_fence in range(len(list_of_char)):
        fence_to_fill[position][change_fence] = list_of_char[change_fence]

        if position == 0:
            direction = 1
        if position == key - 1:
            direction = -1

        position += direction

    print(fence_to_fill)

    encoded_string = ""

    for i in range(len(fence_to_fill)):
        for j in range(len(fence_to_fill[0])):
            if fence_to_fill[i][j] != 0:
                encoded_string += fence_to_fill[i][j]



    return encoded_string  # placeholder for the actual return statement


#  Input: strng is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of strng
#  Output: function returns a single string that is decoded with
#          rail fence algorithm
def rail_fence_decode(strng, key):

    return ""  # placeholder for the actual return statement


#  Input: strng is a string of characters
#  Output: function converts all characters to lower case and then
#          removes all digits, punctuation marks, and spaces. It
#          returns a single string with only lower case characters
def filter_string(strng):
    return ""  # placeholder for the actual return statement


#  Input: p is a character in the pass phrase and s is a character
#         in the plain text
#  Output: function returns a single character encoded using the
#          Vigenere algorithm. You may not use a 2-D list
def encode_character(p, s):
    return ""  # placeholder for actual return statement


#  Input: p is a character in the pass phrase and s is a character
#         in the plain text
#  Output: function returns a single character decoded using the
#          Vigenere algorithm. You may not use a 2-D list
def decode_character(p, s):
    return ""  # placeholder for actual return statement


#  Input: strng is a string of characters and phrase is a pass phrase
#  Output: function returns a single string that is encoded with
#          Vigenere algorithm
def vigenere_encode(strng, phrase):
    return ""  # placeholder for the actual return statement


#  Input: strng is a string of characters and phrase is a pass phrase
#  Output: function returns a single string that is decoded with
#          Vigenere algorithm
def vigenere_decode(strng, phrase):
    return ""  # placeholder for the actual return statement


def main():
# read the plain text from stdin
    encode_this_fence = sys.stdin.readline()
    encode_this_fence = encode_this_fence.strip(" \n")

# read the key from stdin
    fence_key = sys.stdin.readline()
    fence_key = int(fence_key.strip(" \n"))

# encrypt and print the encoded text using rail fence cipher
    encrypted_code = rail_fence_encode(encode_this_fence, fence_key)
    print(encrypted_code)

# read encoded text from stdin
    given_encoded_text = sys.stdin.readline()
    given_encoded_text = given_encoded_text.strip(" \n")

# read the key from stdin
    decryption_key = sys.stdin.readline()
    decryption_key = decryption_key.strip(" \n")

# decrypt and print the plain text using rail fence cipher

# read the plain text from stdin

# read the pass phrase from stdin

# encrypt and print the encoded text using Vigenere cipher

# read the encoded text from stdin

# read the pass phrase from stdin

# decrypt and print the plain text using Vigenere cipher

# The line above main is for grading purposes only.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
    main()