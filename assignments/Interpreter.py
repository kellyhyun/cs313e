#  File: Interpreter.py

#  Description: 

# Student Name: Soomin Hyun

# Student UT EID: sh52679

# Course Name: CS 313E

# Unique Number: 52600

import sys

'''
Input consists of an arbitrary number of lines in one of the following formats:

def [var_name] [expression]

print [expression]

clear

exit

The def command assigns the value of the given expression to the variable. These variable assignments
should be stored until a clear command is encountered. This is not guaranteed to be a valid operation 
(ie variables in the expression might not be defined). Variable names will only consist of alphanumeric
characters, will contain at least one letter (as not to be confused for an integer), and will not contain whitespace.

The print command prints the value of the expression. This is also not guaranteed
to be a valid operation (not all variables in the expression may be defined).

The clear command clears all stored variables.

The exit command terminates the program, and no lines will follow an exit command.

Expressions consist of variable names and/or integers separated by either '+' or '-'. These will all be
separated by spaces. Expressions can be arbitrarily long and consist of arbitrarily many variables and integers.
Invalid expressions (such as those that reference unassigned variable names) should evaluate to the string 'invalid'.
There will be no variable called 'sum'. If 'sum' is in an expression, it represents the sum of all the variables stored so far.
Similarly, there will be no variable called 'prod'. If 'prod is in an expression, it represents the product
of all the variables so far. If there are no variables, 'sum' and 'prod' default to 0.

Examples:
Input 1:
def var1 10
print var1
def var2 10 + var1
print var2
def var3 var1 + var2
print var3
print 5 + 3 - var3
clear
print var1
def var1 1
print var1 + var1 + var1 + var1 + var1 + var1
exit

Output 1:
10
20
30
-22
invalid
6

Explanation:
var1 is first assigned 10 and then printed.
Then var2 is assigned to the sum of var1 and 10, and then printed.
var3 is defined as the sum of var1 and var2, and then printed.
Then the sum of 5 and 3, minus var 3 is printed. This is equal to 8 - 30 = -22.
Then all variables are cleared.
The subsequent attempt to print var1 is invalid since var1 was cleared.
Then var1 is defined to equal 1, and then the sum of var1 six times is printed.
Then the program terminates with the exit command.

Input 2:
print wrong_var
def var1 1
def var2 2
def var3 3
def var4 4
print var1 + var2 - var3 + var4
def var1 var1 + var1 + var1 + var1 + var1
print var1
clear
print var1
def var1 var1
print var1
def var1 0
print var1
exit

Output 2:
invalid
4
5
invalid
invalid
0

Input 3:
def var1 1
def var2 2
def var3 var1 + var2
def var4 var1 + var3
print sum
print prod
print sum - prod
clear
print sum + prod + 101
exit

Input 4:
def a 9
print a - a + a
def b 8
print a - b
print a + b - sum
clear
print a + b
exit

Input 5:
print sum
print prod
def val 100000
def neg_val -100000
def sum_vars sum
print sum
print prod
clear
print sum
print prod
exit
'''

def main():
    line = sys.stdin.readline().strip().split(' ')
    variable_dictionary = {}

    while line[0] != 'exit':
        # your code here
        command = line[0]

        if command == 'clear':
            variable_dictionary = {}
        if command == 'def':
            new_var = {line[1]: line[2]}
            variable_dictionary.update(new_var)
        if command == 'print':
            list_to_do = []
            for i in range(1, len(line)):
                list_to_do.append(line[i])

        for i in range(len(list_to_do)):


        print()


        line = sys.stdin.readline().strip().split(' ')



if __name__ == '__main__':
    main()