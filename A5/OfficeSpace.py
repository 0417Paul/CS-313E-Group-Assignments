#  File: OfficeSpace.py

#  Description: Set up a system to let employees request the working areas they want. 

#  Student Name: Jiaxi Wang

#  Student UT EID: jw53499

#  Partner Name: Yilin Wen

#  Partner UT EID: yw22559

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: Feb 7, 2022

#  Date Last Modified: Feb 9, 2022

import sys
# Input: a rectangle which is a tuple of 4 integers (x1, y1, x2, y2)
# Output: an integer giving the area of the rectangle
def area (rect):
  # the area is (x2-x1)*(y2-y1)
  return (rect[2] - rect[0]) * (rect[3] - rect[1])

# Input: two rectangles in the form of tuples of 4 integers
# Output: a tuple of 4 integers denoting the overlapping rectangle.
#         return (0, 0, 0, 0) if there is no overlap
def overlap (rect1, rect2):
  # if the 2 rectangles don't have areas overlapping
  if (rect2[2] < rect1[0] or rect2[0] > rect1[2]) or (rect2[3] < rect1[1] or rect2[1] > rect1[3]):
    return (0, 0, 0, 0)
  # if the 2 rectangles have areas overlapping
  else:
    return (max(rect1[0], rect2[0]), max(rect1[1], rect2[1]),min(rect1[2], rect2[2]), min(rect1[3], rect2[3]))

# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the unallocated 
#         space in the office
def unallocated_space (bldg):
  unallocated = 0
  # if the space has a number of 0, it is recognized as an unallocated space
  for i in bldg:
       for j in i:
           if j == 0:
               unallocated += 1
  return unallocated

# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the contested 
#         space in the office
def contested_space (bldg):
  contested = 0
  # if the space has a value greater than 1, it has been requested by more than 1 employees and thus considered as contested space
  for i in bldg:
    for j in i:
      if j > 1:
        contested += 1      
  return contested

# Input: bldg is a 2-D array representing the whole office space
#        rect is a rectangle in the form of a tuple of 4 integers
#        representing the cubicle requested by an employee
# Output: a single integer denoting the area of the uncontested 
#         space in the office that the employee gets
def uncontested_space (bldg, rect):
  guaranteed = 0
  # loop through the given requested area and add 1
  # if after the iterance the value representing the area is 1, it means there's only this employee has requested this area
  for x in range(rect[0], rect[2]):
    for y in range(rect[1], rect[3]):
      if bldg[y][x] == 1:
        guaranteed += 1
  return guaranteed

# Input: office is a rectangle in the form of a tuple of 4 integers
#        representing the whole office space
#        cubicles is a list of tuples of 4 integers representing all
#        the requested cubicles
# Output: a 2-D list of integers representing the office building and
#         showing how many employees want each cell in the 2-D list
def request_space (office, cubicles):
  # define a 2-d list to represent the whole office area
  requested_cell = [[0] * office[3] for i in range(office[2])]
  # loop through cubicles and add up all requests for each cell
  for i in cubicles:
    for x in range(i[0], i[2]):
      for y in range(i[1], i[3]):
        requested_cell[y][x] += 1
  return requested_cell

# Input: no input
# Output: a string denoting all test cases have passed
def test_cases ():

  assert area ((0, 0, 1, 1)) == 1
  # not overlapping cases
  # rect2 is on the right side of the rect1
  assert overlap([0,0,3,2], [4,2,5,8]) == (0, 0, 0, 0)
  # rect2 is on the left side of the rect1
  assert overlap([5,5,8,8], [2,2,4,7]) == (0, 0, 0, 0)
  # rect2 overlaps rect1
  assert overlap([5,5,8,8], [2,2,6,7]) == (5, 5, 6, 7)
  # test unallocated space func
  assert unallocated_space([[2,3], [0,0]]) == 2
  assert unallocated_space([[0,0], [0,0]]) == 4
  # test contested space func
  assert contested_space([[2,3], [1,0]]) == 2
  assert contested_space([[2,0], [0,0]]) == 1
  # test the area of the uncontested space in the office that the employee gets
  assert uncontested_space ([[2, 1], [1, 0]],  (0, 0, 2, 1)) == 1
  assert uncontested_space ([[2, 1], [1, 0]],  (1, 1, 2, 2)) == 0
  # test how many employees want each cell in the 2-D list
  assert request_space((0,0,4,4), [(0,0,2,1), (2,1,4,2),(0,0,1,2)]) == [[2, 1, 0, 0], [1, 0, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0]]
  
  return "all test cases passed"

def main():
  # read the data
  # w is the number of feet west-to-east(x), h is the number of feet south-to-north(y)
  w, h = map(int, sys.stdin.readline().split())

  # n is the number of employees you have. Following this are n cubicle placement requests, one per line.
  n = int(sys.stdin.readline()) 

  # read the employees' requests
  # loop through the employee list
  employee_di = {}
  for num in range(n):
    employee = sys.stdin.readline().split()
    for i in range(1, len(employee)):
      employee[i] = int(employee[i])
      name = employee[0]
      cubicle = (employee[1], employee[2], employee[3], employee[4])
    employee_di[name] = cubicle

  # run your test cases
  #print (test_cases())
  # print the following results after computation

  # compute the total office space
  whole_office = (0,0,h,w)
  print("Total", area(whole_office))

  # compute the total unallocated space
  cubes = list(employee_di.values())
  office_list = request_space (whole_office, cubes)
  print("Unallocated", unallocated_space(office_list))

  # compute the total contested space
  print("Contested", contested_space(office_list))

  # compute the uncontested space that each employee gets
  name_list = list(employee_di.keys())

  for na in name_list:
    print(na, uncontested_space(office_list, employee_di[na]))
  #uncontested_space (bldg, rect)
if __name__ == "__main__":
  main()