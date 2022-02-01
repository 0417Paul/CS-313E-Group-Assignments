#  File: TestCipher.py

#  Description: Input plain / encoded text to transform them into encoded / decoded text using two different methods.

#  Student's Name: Jiaxi Wang

#  Student's UT EID: jw53499
 
#  Partner's Name: Yilin Wen

#  Partner's UT EID: yw22559

#  Course Name: CS 313E 

#  Unique Number: 51120

#  Date Created: Jan 31

#  Date Last Modified:

import sys

#  Input: strng is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of strng
#  Output: function returns a single string that is encoded with
#          rail fence algorithm
def rail_fence_encode ( strng, key ):
  cipher_text = ""

  for row in range(key):

    # encode the first row
    # a shift is the stright distance the letters take from the top row all the way to bottom and came back
    shift = 2 * key - 2
    index = 0
    #while index < len(strng):
    if row == 0:
      while index < len(strng):
        # the difference between each index is a shift
        cipher_text += strng[index]
        index += shift
    
    # encode the last row
    elif row == key - 1:
      # the first letter in the last row always start at the index equals to key-1, and then it will goes through a shift and 
      # come back to the bottom row
      index = row
      while index < len(strng):
        cipher_text += strng[index]
        index += shift

    # encode the rest of the rows in-between
    else:
        # there will be left and right indexes for this case, they will be both on the next line & at the index next to the letter above
      lft = row
      rgt = shift - row
      while lft < len(strng):
        cipher_text += strng[lft]
        if rgt < len(strng):          
          cipher_text += strng[rgt]
        lft += shift
        rgt += shift 

  return cipher_text # placeholder for the actual return statement

#  Input: strng is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of strng
#  Output: function returns a single string that is decoded with
#          rail fence algorithm
def rail_fence_decode ( strng, key ):
  return "" # placeholder for the actual return statement

#  Input: strng is a string of characters
#  Output: function converts all characters to lower case and then
#          removes all digits, punctuation marks, and spaces. It
#          returns a single string with only lower case characters
def filter_string ( strng ):
  return "" # placeholder for the actual return statement

#  Input: p is a character in the pass phrase and s is a character
#         in the plain text
#  Output: function returns a single character encoded using the 
#          Vigenere algorithm. You may not use a 2-D list 
def encode_character (p, s):
  return "" # placeholder for actual return statement

#  Input: p is a character in the pass phrase and s is a character
#         in the plain text
#  Output: function returns a single character decoded using the 
#          Vigenere algorithm. You may not use a 2-D list 
def decode_character (p, s):
  return "" # placeholder for actual return statement

#  Input: strng is a string of characters and phrase is a pass phrase
#  Output: function returns a single string that is encoded with
#          Vigenere algorithm
def vigenere_encode ( strng, phrase ):
  return "" # placeholder for the actual return statement

#  Input: strng is a string of characters and phrase is a pass phrase
#  Output: function returns a single string that is decoded with
#          Vigenere algorithm
def vigenere_decode ( strng, phrase ):
  return "" # placeholder for the actual return statement

def main():
  # Does it need a blank line at the top?
  # read the plain text from stdin
  strng1 = sys.stdin.readline()
  # read the key from stdin
  key1 = int(sys.stdin.readline())
  # encrypt and print the encoded text using rail fence cipher
  print("Rail Fence Cipher")
  print()
  print("Plain Text: ", strng1)
  print("Key: ", key1)
  print("Encoded Text: ", rail_fence_encode ( strng1, key1 ))
  print()

  # read encoded text from stdin
  strng2 = sys.stdin.readline()
  # read the key from stdin
  key2 = int(sys.stdin.readline())
  # decrypt and print the plain text using rail fence cipher
  print("Encoded Text: ", strng2)
  print("Enter Key: ", key2)
  print("Decoded Text: ", rail_fence_decode ( strng2, key2 ))
  print()

  # read the plain text from stdin

  # read the pass phrase from stdin

  # encrypt and print the encoded text using Vigenere cipher

  # read the encoded text from stdin

  # read the pass phrase from stdin

  # decrypt and print the plain text using Vigenere cipher

# The line above main is for grading purposes only.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()