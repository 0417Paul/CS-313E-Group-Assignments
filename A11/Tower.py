#  File: Tower.py

#  Description: Compute the the total number of transfers using four needles where the priest can move only one disk at a time 
#  and must place each disk on a needle such that there is no smaller disk below it.

#  Student's Name: Jiaxi Wang

#  Student's UT EID: jw53499

#  Partner's Name: Yilin Wen

#  Partner's UT EID: yw22559

#  Course Name: CS 313E 

#  Unique Number: 51120

#  Date Created: March 1, 2022

#  Date Last Modified: March 3, 2022

import sys
import math

def num_hanoi(n):
  return 2 ** n - 1

# Input: n the number of disks
# Output: returns the number of transfers using four needles
def num_moves (n):
  # base case
  if n <= 2:
    return num_hanoi(n)

  # recursive steps
  else:
    k = int(n - math.sqrt(2 * n + 1) + 1)
    return 2 * num_moves(k) + 2 * num_hanoi(n - k - 1) + 1

def main():
  # read number of disks and print number of moves
  for line in sys.stdin:
    line = line.strip()
    num_disks = int (line)
    print (num_moves (num_disks))

if __name__ == "__main__":
  main()