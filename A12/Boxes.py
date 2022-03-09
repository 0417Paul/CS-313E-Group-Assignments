
#  File: Boxes.py

#  Description: Finding the largest number of boxes that can fit inside each other 
#  and give the number of such sets of boxes that do fit.

#  Student Name: Jiaxi Wang

#  Student UT EID: jw53499

#  Partner Name: Yilin Wen

#  Partner UT EID: yw22559

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: Mar 5

#  Date Last Modified:

import sys


# Input: 2-D list of boxes. Each box of three dimensions is sorted
#        box_list is sorted
# Output: function returns two numbers, the maximum number of boxes
#         that fit inside each other and the number of such nesting
#         sets of boxes
def nesting_boxes (box_list):
  return


# returns True if box1 fits inside box2
def does_fit (box1, box2):
  return (box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2])

def main():
  # read the number of boxes 
  line = sys.stdin.readline()
  line = line.strip()
  num_boxes = int (line)

  # create an empty list for the boxes
  box_list = []

  # read the boxes from the file
  for i in range (num_boxes):
    line = sys.stdin.readline()
    line = line.strip()
    box = line.split()
    for j in range (len(box)):
      box[j] = int (box[j])
    box.sort()
    box_list.append (box)

  # print to make sure that the input was read in correctly
  print (box_list)
  print()

  # sort the box list
  box_list.sort()

  # print the box_list to see if it has been sorted.
  print (box_list)
  print()

  # get the maximum number of nesting boxes and the
  # number of sets that have that maximum number of boxes
  # max_boxes, num_sets = nesting_boxes (box_list)

  # # print the largest number of boxes that fit
  # print (max_boxes)

  # # print the number of sets of such boxes
  # print (num_sets)

if __name__ == "__main__":
  main()

