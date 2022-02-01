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

from audioop import reverse
import sys

# Input: tuples_list is an sorted list of tuples denoting intervals
# Output: a list of merged tuples sorted by the lower number of the
#         interval

def merge_tuples (tuples_list):
  merged_tuple_list = []
  i = 0
  min_value = tuples_list[0][0]
  max_value = tuples_list[0][1]
  count = len(tuples_list) - 1

  while count != 0:
    # if the end value of the second tuple is in the range (first tuple);
    if tuples_list[i + 1][i] in range(min_value, max_value + 1):

        # if the start value of the second tuple is also in the range of first tuple
      if tuples_list[i + 1][i + 1] in range(min_value, max_value + 1):
          tuples_list.remove(tuples_list[i + 1])
          count -= 1

        # if the start value's not in the range,
        # substitute the max number and update the list
      elif tuples_list[i + 1][i + 1] not in range(min_value, max_value + 1):
        max_value = tuples_list[i + 1][i + 1]
        tuples_list.remove(tuples_list[i])
        tuples_list.remove(tuples_list[i])
        tuples_list.insert(i, (min_value, max_value))
        count -= 1

      # if the end value of the second tuple is not in range(first tuple), 
      # append the tuple to the merged list
    elif tuples_list[i + 1][i] not in range(min_value, max_value + 1):
      min_value = tuples_list[i + 1][i]
      max_value = tuples_list[i + 1][i + 1]
      merged_tuple_list.append(tuples_list[0])
      tuples_list.remove(tuples_list[0])
      count -= 1

    # append the last pair of tuple to the merged list
  merged_tuple_list.append(tuples_list[0])
  return merged_tuple_list


# Input: tuples_list is a list of tuples of denoting intervals
# Output: a list of tuples sorted by ascending order of the size of
#         the interval
#         if two intervals have the size then it will sort by the
#         lower number in the interval

def sort_by_interval_size(tuples_list):
  # Passing lambda as key to sort list of tuple by the difference
  sorted_list = sorted(tuples_list, key = lambda x:x[1] - x[0])
  return sorted_list


def main():
  tuple_list = []
  # reading the number of pairs of tuples
  num_pair = int(sys.stdin.readline().strip())

  # read the input data and create a list of tuples
  for row in range(num_pair):
    t = sys.stdin.readline().strip().split(" ")
    tuple_list.append((int(t[0]), int(t[1])))
  tuple_list = sorted(tuple_list, key = lambda x:x[0])
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