
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

#  Date Last Modified: Mar 11

import sys

# Input: 2-D list of boxes. Each box of three dimensions is sorted
#        box_list is sorted
# Output: function returns two numbers, the maximum number of boxes
#         that fit inside each other and the number of such nesting
#         sets of boxes
def nesting_boxes (box_list):
  # construct the memo from box_list, line by line
  box_list.insert(0,[0,0,0,0,0,0])
  for i in range(1,len(box_list)):
    fit_i = []
    for j in range(i):
      if does_fit(box_list[j], box_list[i]):
        fit_i.append(j)
    fit_boxes = [box_list[k][3] for k in fit_i]
    box_list[i].append(max(fit_boxes) + 1) # N(i) = N(j) + 1
    
    max_now = max([box_list[k][3] for k in range(i+1)]) # max of N(i) for i from 0 to i
    box_list[i].append(max_now)
    
    k = i
    while k > 0 and box_list[k][3] != max_now:
      k -= 1
    # now k is R(i)
    box_list[i].append(k)
  max_boxes = box_list[-1][4]

  # now we find all 3-boxes that can fit in the 4-boxes, then the 2-boxes fit in the 3 boxes, ...
  # we use a recursive approach

  num_sets = 0
  for box in range(len(box_list)):
    if box_list[box][3] == max_boxes:
      num_sets += all_fit(box_list, box)

  #for row in box_list:
  #  print(row)

  return max_boxes, num_sets

# recursively find how many possible ways boxes can fit in this n-box (whose N(i) = n)
def all_fit(box_list, n_box):
  n = box_list[n_box][3]
  # base case
  if n == 1:
    return 1
  # recursive step
  num = 0
  for box in range(len(box_list)): 
    if box_list[box][3] == n-1 and does_fit(box_list[box], box_list[n_box]):
      # now box is a (n-1)-box that can fit in n_box
      num += all_fit(box_list, box)
  return num

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
  #print (box_list)
  #print()

  # sort the box list
  box_list.sort()

  # print the box_list to see if it has been sorted.
  #print (box_list)
  #print()

  # # get the maximum number of nesting boxes and the
  # # number of sets that have that maximum number of boxes
  # max_boxes, num_sets = nesting_boxes (box_list)

  # # print the largest number of boxes that fit
  # print (max_boxes)

  # # print the number of sets of such boxes
  # print (num_sets)

  memo = nesting_boxes(box_list)
  for row in memo:
    print(row)

if __name__ == "__main__":
  main()

