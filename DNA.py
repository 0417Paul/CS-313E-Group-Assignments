#  File: DNA.py

#  Description: This Program compares two strands of DNA sequences and print out
#  the longest common sequence of each pair.

#  Student Name: Yilin Wen

#  Student UT EID: YW22559

#  Partner Name: Jiaxi Wang

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: 01/20/2022

#  Date Last Modified:

# Input: s1 and s2 are two strings that represent strands of DNA
# Output: returns a sorted list of substrings that are the longest 
#         common subsequence. The list is empty if there are no 
#         common subsequences.

from operator import countOf
import sys

def allsub(s):
    #  look for all the substrings in the string and return a list.
    substrings = []
    count = len (s)
    while (count != 0):
        n = 0
        while ((n + count) <= len(s)):
            sub = s[n:s + count]
            n += 1
            substrings.append(sub)
        count -= 1
    return substrings


def longest_subsequence (s1, s2):
    #  comparing two strings and output the longest subsequence
    #  of two strings in common.
    s1_substring = allsub(s1)

    #  finding all the common substrings
    common_strings = []
    for i in s1_substring:
        if i in s2:
            common_strings.append(i)
            continue

    #  getting the longest substrings from the common_strings list.
    if len(common_strings) == 0:
        print('No Common Sequence Found')
    else:
        l = []
        longest_length = len(max(common_strings, key = len))
        for i in common_strings:
            if len(i) == longest_length:
                l.append(i)
    return l


def main():
  # read the data
  num_pairs = int(sys.stdin.readline().strip())

  # for each pair
  for i in range(num_pairs):
      
      #  read the 2 sequence as strings
      s1 = sys.stdin.readline().strip().upper()
      s2 = sys.stdin.readline().strip().upper()
      
      # call longest_subsequence
      longest_common = longest_subsequence(s1, s2)
      longest_common.sort()
      
      # write out result(s)
      for i in longest_common:
          print(i)

	  # insert blank line
      print()

if __name__ == "__main__":
    main()