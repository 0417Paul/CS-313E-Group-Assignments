#  File: Reducible.py

#  Description: Find the list of the longest words that are reducible.

#  Student Name: Jiaxi Wang

#  Student UT EID: jw53499

#  Partner Name: Yilin Wen

#  Partner UT EID: yw22559

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: Mar 22

#  Date Last Modified: Mar 22

import sys
import math

# Input: takes as input a positive integer n
# Output: returns True if n is prime and False otherwise
def is_prime ( n ):
    if (n == 1):
        return False

    limit = int (n ** 0.5) + 1
    div = 2
    while (div < limit):
        if (n % div == 0):
            return False
        div += 1
    return True

# Input: takes as input a string in lower case and the size
#        of the hash table 
# Output: returns the index the string will hash into
def hash_word(s, size):
    hash_idx = 0
    for j in range(len(s)):
        letter = ord(s[j]) - 96
        hash_idx = (hash_idx * 26 + letter) % size
    return hash_idx

# Input: takes as input a string in lower case and the constant
#        for double hashing 
# Output: returns the step size for that string 
def step_size (s, const):
    step = 0
    for i in range (len(s)):
        letter = ord (s[i]) - 96
        # using the hash function to calculate the step size
        step = (step * 26 + letter) % const
    s_size = const - (step % const)
    return s_size

# Input: takes as input a string and a hash table 
# Output: no output; the function enters the string in the hash table, 
#         it resolves collisions by double hashing
def insert_word (s, hash_table):
    # determine the index that string is supposed to fit in
    size = len(hash_table)
    idx = hash_word(s, size)

  # test if that position of the index is empty
    if hash_table[idx] == '':
        hash_table[idx] = s
    
  # if the position has been taken, find a new index for the string
    else:
        step = step_size(s, 13)
        # use the new index to find a position, test that position again until we find an empty space
        for i in range (size):
            if hash_table[(idx + i * step) % size] != '':
                if hash_table[(idx + i * step) % size] == s:
                    return None
            else:
                hash_table[(idx + i * step) % size] = s
                return None

# Input: takes as input a string and a hash table 
# Output: returns True if the string is in the hash table 
#         and False otherwise
def find_word (s, hash_table):
    size = len(hash_table)
    idx = hash_word(s, size)

  # test if the given string is in the hash table
    if hash_table[idx] == s:
        return True
    else:
        # find that string using double hashing
        step = step_size(s, 13)
        for i in range (size):
            if hash_table[(idx + i * step) % size] == '':
                return False
            elif hash_table[(idx + i * step) % size] == s:
                return True
        return False

# Input: string s, a hash table, and a hash_memo 
#        recursively finds if the string is reducible
# Output: if the string is reducible it enters it into the hash memo 
#         and returns True and False otherwise
def is_reducible (s, hash_table, hash_memo):
    # if the string is "a" or "i" or "o", or we find it in hash memo
    if (s == 'a') or (s == 'i') or (s == 'o') or find_word(s, hash_memo):
        return True
    elif find_word (s, hash_table) is False or 'a' not in s and 'i' not in s and 'o' not in s:
        return False
    else:
        # slicing the string using index one by one
        for i in range (len(s)):
            s_new = s[:i] + s[i + 1:]
            if s_new == 'a' or s_new == 'i' or s_new == 'o':
                return True
            if find_word (s_new, hash_table) is False:
                continue
            if is_reducible (s_new, hash_table, hash_memo):
                insert_word (s_new, hash_memo)
                insert_word(s, hash_memo)
                return True
        return False

# Input: string_list a list of words
# Output: returns a list of words that have the maximum length
def get_longest_words (string_list):
    # sort the string list and find the length of the longest word in it
    string_list.sort(key = len)
    string_list.reverse()
    max_length = len(string_list[0])
    # create a max length words list to append the longest words into it
    max_length_lst = []
    for word in string_list:
        if len(word) == max_length:
            max_length_lst.append(word)
    return max_length_lst

def main():
    # create an empty word_list
    word_list = []

    # read words from words.txt and append to word_list
    for line in sys.stdin:
        line = line.strip()
        word_list.append (line)

    # find length of word_list
    length = len(word_list)

    # determine prime number N that is greater than twice
    # the length of the word_list
    N = 2 * length
    while N != 0:
        if is_prime(N):
            break
        else:
            N += 1

    # create an empty hash_list
    hash_list = []

    # populate the hash_list with N blank strings
    for i in range (N):
        hash_list.append('')

    # hash each word in word_list into hash_list
    # for collisions use double hashing 
    for word in word_list:
        insert_word (word, hash_list)

  # create an empty hash_memo of size M
  # we do not know a priori how many words will be reducible
  # let us assume it is 10 percent (fairly safe) of the words
  # then M is a prime number that is slightly greater than 
  # 0.2 * size of word_list
    hash_memo = []
    M = math.ceil (0.2 * length + 1)
    while is_prime(M) is False:
        M += 1

  # populate the hash_memo with M blank strings
    for i in range (M):
        hash_memo.append('')

  # create an empty list reducible_words
    reducible_words = []

  # for each word in the word_list recursively determine
  # if it is reducible, if it is, add it to reducible_words
  # as you recursively remove one letter at a time check
  # first if the sub-word exists in the hash_memo. if it does
  # then the word is reducible and you do not have to test
  # any further. add the word to the hash_memo.
    for word in word_list:
    # if word in hash_memo:
    #   return None
    # else:
        if is_reducible (word, hash_list, hash_memo):
            reducible_words.append(word)

  # find the largest reducible words in reducible_words
    max_lst = get_longest_words(reducible_words)
  # print the reducible words in alphabetical order
  # one word per line
    max_lst.sort()
    for word in max_lst:
        print(word)

if __name__ == "__main__":
  main()