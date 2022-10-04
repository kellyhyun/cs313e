#  File: Tower.py

#  Description: Calculates the minimum number of moves to move certain number of disks from one peg
# to another following rules of the Tower of Hanoi but having four pegs.

#  Student's Name: Soomin Hyun

#  Student's UT EID: sh52679

#  Partner's Name: Joon Kim (Unique Number: 52595)

#  Partner's UT EID: jk45873

#  Course Name: CS 313E

#  Unique Number: 52600

#  Date Created: 10/7/2021

#  Date Last Modified: 10/8/2021
import sys
import math

# Input: n the number of disks
# Output: returns the number of transfers using four needles
def num_moves (n):
 return int(num_moves_helper(n, 4, 0))


def num_moves_helper(n, num_pegs_left, num_moves):
   if n == 0:
       return 0
   if n == 1:
       num_moves += 1
       return num_moves
   elif n == 2:
       num_moves += 3
       return num_moves

   else:
       if num_pegs_left == 4:
           k = (n - math.sqrt(2*n + 1) + 1)
           if (k * 10) % 10 >= 5:
               k += 1
               k //= 1
           else:
               k //= 1
           return 2 * num_moves_helper(k, 4, num_moves) + 2 * num_moves_helper(n-k-1, 3, num_moves) + num_moves_helper(1, 4, num_moves)

       else:
           num_moves += (2 ** n - 1) // 1
           return num_moves

def main():
 # read number of disks and print number of moves
 for line in sys.stdin:
   line = line.strip()
   num_disks = int (line)
   print (num_moves (num_disks))

if __name__ == "__main__":
 main()

