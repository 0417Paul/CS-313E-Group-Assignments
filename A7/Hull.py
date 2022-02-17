
#  File: Hull.py

#  Description: Find the convex hull and print all of its vertices. 

#  Student Name: Jiaxi Wang

#  Student UT EID: jw53499

#  Partner Name: Yilin Wen 

#  Partner UT EID: yw22559

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: Feb 15, 2022

#  Date Last Modified: Feb 16, 2022

import sys

import math

class Point (object):
  # constructor
  def __init__(self, x = 0, y = 0):
    self.x = x
    self.y = y

  # get the distance to another Point object
  def dist (self, other):
    return math.hypot (self.x - other.x, self.y - other.y)

  # string representation of a Point
  def __str__ (self):
    return '(' + str(self.x) + ', ' + str(self.y) + ')'

  # equality tests of two Points
  def __eq__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

  def __ne__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) >= tol) or (abs(self.y - other.y) >= tol))

  def __lt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y < other.y)
    return (self.x < other.x)

  def __le__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y <= other.y)
    return (self.x <= other.x)

  def __gt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y > other.y)
    return (self.x > other.x)

  def __ge__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y >= other.y)
    return (self.x >= other.x)

# Input: p, q, r are Point objects
# Output: compute the determinant and return the value
def det (p, q, r):
  determinant = p.x * q.y + q.x * r.y + r.x * p.y - p.y * q.x - q.y * r.x - r.y * p.x
  return determinant

# Input: sorted_points is a sorted list of Point objects
# Output: computes the convex hull of a sorted list of Point objects
#         convex hull is a list of Point objects starting at the
#         extreme left point and going clockwise in order
#         returns the convex hull
def convex_hull (sorted_points):
  # Create an empty list upper_hull that will store the vertices in the upper hull.
  # Append the first two points p_1 and p_2 in order into the upper_hull.
  upper_hull = [sorted_points[0], sorted_points[1]]
  # For i going from 3 to n 
  # Append p_i to upper_hull.
  for p in sorted_points[2:]:
    upper_hull.append(p)
  # test the determinate to make sure the points don't make a right turn, 
  # and delete the middle of the last three points from upper_hull
    while (len(upper_hull) >=3) and det(upper_hull[-3], upper_hull[-2], upper_hull[-1]) > 0:
      upper_hull.remove(upper_hull[-2])

  # Create an empty list lower_hull that will store the vertices in the lower hull.
  # Append the last two points p_n and p_n-1 in order into lower_hull with p_n as the first point.
  lower_hull = [sorted_points[-1], sorted_points[-2]]
  # For i going from n - 2 down to 1
  # Append p_i to lower_hull
  for i in range(len(sorted_points) - 3, -1, -1):
    lower_hull.append(sorted_points[i])

  # While lower_hull contains three or more points and the last three
  # points in the lower_hull do not make a right turn do
  # Delete the middle of the last three points from lower_hull
    while (len(lower_hull) >=3) and det(lower_hull[-3], lower_hull[-2], lower_hull[-1]) > 0:
      lower_hull.remove(lower_hull[-2])

  # Remove the first and last points for lower_hull to avoid duplication with points in the upper hull.
  lower_hull.remove(lower_hull[0])
  lower_hull.remove(lower_hull[-1])

  # Append the points in the lower_hull to the points in the upper_hull and call those points the convex_hull
  convex_hull = upper_hull
  for o in lower_hull:
    convex_hull.append(o)

  # Return the convex_hull.
  return convex_hull

# Input: convex_poly is  a list of Point objects that define the
#        vertices of a convex polygon in order
# Output: computes and returns the area of a convex polygon
def area_poly (convex_poly):
  sum1 = 0
  sum2 = 0

  # calcualte the 2 parts of det seperately
  for i in range(len(convex_poly)):
    sum1 += (convex_poly[i].x * convex_poly[i + 1 if (i != len(convex_poly)-1) else 0].y)
    sum2 += (convex_poly[i].y * convex_poly[i + 1 if (i != len(convex_poly)-1) else 0].x)

  # calculate area
  det = sum1 - sum2
  area = (1/2) * abs (det)
  return area

# Input: no input
# Output: a string denoting all test cases have passed
def test_cases():
  # write your own test cases
  lst = [Point(0, 0),  Point(4, 5), Point(2, 2), Point(8, 2), Point(8, 4),
         Point(2, 0), Point(-3, 2), Point(5, 3), Point(2, -2)]
  lst.sort()
  for p in lst:
    print(p)

  lst = [Point(2, 8), Point(5, 7), Point(8, 2), Point(8, 3),
         Point(3, 3), Point(-3, -2), Point(-5, -1)]
  lst.sort()
  for p in lst:
    print(p)

  return "all test cases passed"

def main():
  # create an empty list of Point objects
  points_list = []

  # read number of points
  line = sys.stdin.readline()
  line = line.strip()
  num_points = int (line)

  # read data from standard input
  for i in range (num_points):
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    x = int (line[0])
    y = int (line[1])
    points_list.append (Point (x, y))

  # sort the list according to x-coordinates
  sorted_points = sorted (points_list)

  '''
  # print the sorted list of Point objects
  for p in sorted_points:
    print (str(p))
  '''

  # get the convex hull
  convex = convex_hull(sorted_points)
  # run your test cases
  #test_cases()
  # print your results to standard output
  print("Convex Hull")
  # print the convex hull
  for p in convex:
    print(str(p))
  print()
  # get the area of the convex hull
  area = area_poly(convex)
  # print the area of the convex hull
  print("Area of Convex Hull = {}".format(area, ".1f"))
if __name__ == "__main__":
  main()