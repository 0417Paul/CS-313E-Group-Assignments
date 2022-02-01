#  File: Intervals.py

#  Description: take a set of intervals and collapse all the overlapping intervals 
#  and print the smallest set of non-intersecting intervals in ascending order of the 
#  lower end of the interval and then print the intervals in increasing order of the size of the interval.

#  Student Name:  Yilin Wen

#  Student UT EID: YW22559

#  Partner Name: Jiaxi Wang

#  Partner UT EID: JW53499

#  Course Name: CS 313E 

#  Unique Number: 51120

#  Date Created: 01/27/2022

#  Date Last Modified: 1/31/2022

import sys

# Input: tuples_list is an sorted list of tuples denoting intervals
# Output: a list of merged tuples sorted by the lower number of the
#         interval

# def is_overlapping(t1,t2):
#   new_list = [(t1),(t2)]
#   for i in range (len(new_list)):
#     if (new_list[i][0] <= new_list[i+1][0] and new_list[i+1][0] <= new_list[i][1]):
#       return True


def merge_tuples (tuples_list):
  merged_tuple_list = []

  for i in tuples_list:
    # if the list of merged intervals is empty, we will append this interval.
    if not merged_tuple_list:
      merged_tuple_list.append(i)
    else:
      lower = merged_tuple_list[-1]
      # test for intersection between the last tuple in merged_tuple_list and the next interval in the tuple list:
      if i[0] <= lower[1]:
        upperbound = max(lower[1],i[1])
        merged_tuple_list[-1] = (lower[0],upperbound)
      else:
        merged_tuple_list.append(i)

  return merged_tuple_list


# Input: tuples_list is a list of tuples of denoting intervals
# Output: a list of tuples sorted by ascending order of the size of
#         the interval
#         if two intervals have the size then it will sort by the
#         lower number in the interval


def sort_by_interval_size (tuples_list):
  for i in range(len(tuples_list)-1):
    for j in range(i, len(tuples_list)):
    # comparing the adjacent elements and calculate the difference of (y-x)
      dif1 = tuples_list[i][1]-tuples_list[i][0]
      dif2 = tuples_list[j][1]-tuples_list[j][0]
      if dif1 > dif2:
    # swapping if sum of the second tuple is greater than the first pair
        tuples_list[i], tuples_list[j] = tuples_list[j], tuples_list[i]
  return tuples_list


def main():
  tuple_list = []
  # reading the number of pairs of tuples
  num_pair = int(sys.stdin.readline().strip())

  # read the input data and create a list of tuples
  for row in range(num_pair):
    t = sys.stdin.readline().strip().split(" ")
    tuple_list.append((int(t[0]), int(t[1])))
  tuple_list = sorted(tuple_list, key = lambda x:x[0] + x[1])
  # merge the list of tuples
  new_list_tuples = merge_tuples (tuple_list)
  # print the merged list
  print(new_list_tuples)
  # sort the list of tuples according to the size of the interval
  sorted_tuples = sort_by_interval_size (new_list_tuples)
  # print the sorted list
  print(sorted_tuples)





if __name__ == "__main__":
  main()