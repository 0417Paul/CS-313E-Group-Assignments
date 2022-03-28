
#  File: Radix.py

#  Description:

#  Student Name: Yilin Wen

#  Student UT EID: yw22559

#  Partner Name: Jiaxi Wang

#  Partner UT EID: jw53499

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: 03/25/2022

#  Date Last Modified: 03/28/2022

import sys

class Queue (object):
  def __init__ (self):
    self.queue = []

  # add an item to the end of the queue
  def enqueue (self, item):
    self.queue.append (item)

  # remove an item from the beginning of the queue
  def dequeue (self):
    return (self.queue.pop(0))

  # check if the queue if empty
  def is_empty (self):
    return (len(self.queue) == 0)

  # return the size of the queue
  def size (self):
    return (len(self.queue))

# Input: a is a list of strings that have either lower case
#        letters or digits
# Output: returns a sorted list of strings
def radix_sort (a):
  # make a list of queues: we need 26 + 10 + 1 = 37 queues
  # we use the last queue to merge.
  my_queues = [Queue() for i in range(37)]
  
  # make a dictionary to map char to index of my_queues:
  my_dict = {}
  for i in range(10):
    my_dict[chr(ord('0') + i)] = i # insert '0' to '9' to the dict
  for j in range(26):
    my_dict[chr(ord('a') + j)] = j + 10 # 'a' to 'z', taking up 10~35 of our list
  
  # determine num of passes, i.e. the largest lenth of strings in a
  num_pass = len(max(a, key = lambda x: len(x)))

  # do the passes, starting at the last index of the string
  # if a string has lenth smaller than current index, take the chr there as the smallest, i.e. '0'
  for s in a:
    my_queues[-1].enqueue(s)

  for idx in range(num_pass-1, -1, -1):
    # dump things in last queue to corresponding queues
    while not my_queues[-1].is_empty():
      s = my_queues[-1].dequeue()
      char = s[idx] if idx < len(s) else '0'
      my_queues[my_dict[char]].enqueue(s)
    # merge each queue to the last and go to next pass
    for q in my_queues[:-1]:
      while not q.is_empty():
        my_queues[-1].enqueue(q.dequeue())

  # now we output the last queue
  sorted_a = []
  while not my_queues[-1].is_empty():
    sorted_a.append(my_queues[-1].dequeue())
  return sorted_a

def main():
  # read the number of words in file
  line = sys.stdin.readline()
  line = line.strip()
  num_words = int (line)

  # create a word list
  word_list = []
  for i in range (num_words):
    line = sys.stdin.readline()
    word = line.strip()
    word_list.append (word)

  '''
  # print word_list
  print (word_list)
  '''

  # use radix sort to sort the word_list
  sorted_list = radix_sort (word_list)

  # print the sorted_list
  print (sorted_list)

if __name__ == "__main__":
  main()

    
