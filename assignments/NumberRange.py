#  File: NumberRange.py

#  Description: Combine the close ranges of numbers to save space

# Student Name: Soomin Hyun

# Student UT EID: sh52679

# Course Name: CS 313E

# Unique Number: 52600

import sys

# Input:    An list of unique postive integers
# Output:   An sorted list of string of the combined ranges
def combine_into_ranges(number_list):
    # TODO complete the function
    sorted_list = sorted(number_list)
    new_list = []
    here_range = []
    ranges_list = []
    range_boolean = False
    no_range = []
    range_string = []

    for i in range(len(sorted_list)):
        if i != len(sorted_list):
            if sorted_list[i] + 1 == sorted_list[i + 1]:
                here_range.append(sorted_list[i])
                range_boolean = True
        if sorted_list[i] - 1 == sorted_list[i - 1]:
            here_range.append(sorted_list[i + 1])
            if len(here_range) >= 3:
                ranges_list.append(here_range)
                range_boolean = True
            here_range = []
            range_boolean = False
        if range_boolean == False:
            no_range.append(sorted_list[i])

    for i in range(len(ranges_list)):
        range_string.append('{} - {}'.format(ranges_list[i][0], ranges_list[i][len(ranges_list[i]) - 1]))

    for num in range(len(no_range)):
        for i in range(len(ranges_list)):
            if no_range[num] < ranges_list[i][0]:
                new_list.append(str(no_range[num]))

            if no_range[num] > ranges_list[i][0]:
                new_list.append(range_string[i])


    return new_list



# NO NEED TO CHANGE main()
def main():
    # Read the list of numbers
    number_list = [*map(int, sys.stdin.readline().split())]    
    # print the answer
    ans = combine_into_ranges(number_list)
    
    # TODO print
    print(ans)

if __name__ == "__main__":
    main()