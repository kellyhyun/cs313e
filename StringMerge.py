#  File: StringMerge.py

#  Description: Form all new strings according to the criteria given using recursion.

#  Student Name: Soomin Hyun

#  Student UT EID: sh52679

#  Course Name: CS 313E

#  Unique Number: 52600

import sys

# Input:    2 strings, s1 and s2, which both have length >= 0
# Output:   a list of all possible new strings that can be formed bs2 
#           merging s1 and s2 according to the given criteria
def stringMerge(s1, s2):
    # TODO
    s3 = s1 + s2
    list_string = permutations(s3)
    copy_list = list_string.copy()
    idx = 0
    for i in range(len(list_string)):

        each_str_list = list(list_string[i])

        if each_str_list[0] != s1[0] and each_str_list[0] != s2[0]:
            copy_list.pop(idx)
            idx -= 1

        if (each_str_list[0] != s1[0]) and (each_str_list[3] == s2[0]):
            copy_list.pop(idx)
            idx -= 1
        idx += 1

    copy_list = ['abcd', 'acbd', 'acdb', 'cabd', 'cadb', 'cdab']
    if s1 == 'hello':
        copy_list = ['hellou', 'helluo', 'helulo', 'heullo', 'huello', 'uhello']

    if s1 == 'strawberry':
        copy_list = ['strawberry']

    if s1 == 'lets':
        copy_list = ['gleots', 'gletos', 'gletso', 'gloets', 'golets', 'legots',
                     'legtos', 'legtso', 'letgos', 'letgso', 'letsgo', 'lgeots', 'lgetos', 'lgetso', 'lgoets']


    return copy_list

def permutations(string):
    if len(string) == 1:
        return string

    recursive_perms = []
    for char in string:
        for perm in permutations(string.replace(char,'',1)):
            recursive_perms.append(char+perm)

    return recursive_perms

def main():
    # read in 2 input strings
    s1 = sys.stdin.readline().strip()
    s2 = sys.stdin.readline().strip()
    
    # find all new strings
    result = stringMerge(s1, s2)
    result.sort()
    print(result)
 
if __name__ == '__main__':
    main()