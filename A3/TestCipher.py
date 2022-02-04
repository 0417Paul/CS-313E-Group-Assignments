#  File: TestCipher.py

#  Description: Input plain / encoded text to transform them into encoded / decoded text using two different methods.

#  Student's Name: Jiaxi Wang

#  Student's UT EID: jw53499
 
#  Partner's Name: Yilin Wen

#  Partner's UT EID: yw22559

#  Course Name: CS 313E 

#  Unique Number: 51120

#  Date Created: Jan 31

#  Date Last Modified: Feb 3

from curses.ascii import isdigit
from re import I
import sys
import string

#  Input: strng is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of strng
#  Output: function returns a single string that is encoded with
#          rail fence algorithm
def rail_fence_encode ( strng, key ):
  cipher_text = ""
  inner_step = (key - 2) * 2
  step = inner_step + 2

  for i in range(key):
    index = i

    # for the 1st and last row
    # a step is the stright distance the letters take from the top row all the way to bottom and came back
    while index < len(strng):
      cipher_text += strng[index]

      # for the rows in-between
      # inner step is the space between 2 letters on these rows
      if 0 < i < key - 1:
        if index + inner_step < len(strng):
          cipher_text += strng[index + inner_step]
      
      index += step
    
    # inner step for the next in-between row is always the inner step of current row - 2
    if 0 < i < key - 1:
      inner_step -= 2

  return cipher_text # placeholder for the actual return statement

#  Input: strng is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of strng
#  Output: function returns a single string that is decoded with
#          rail fence algorithm
def rail_fence_decode ( strng, key ):
  cipher_len = len(strng)
  lst = [["0"] * cipher_len for i in range(key)]
  inner_step = (key - 2) * 2
  step = inner_step + 2

  # we start from replacing all places we think there is a letter for "1"
  for i in range(key):
    index = i

    # same logics as above encoding function
    while index < len(strng):
      lst[i][index] = "1"

      if 0 < i < key - 1:
        if index + inner_step < len(strng):
          lst[i][index + inner_step] = "1"
      
      index += step

    if 0 < i < key - 1:
      inner_step -= 2 

  # plug in the characters into the list where we marked "1"
  count = 0

  for i in range(key):
    for j in range(cipher_len):
      if lst[i][j] == "1":
        lst[i][j] = strng[count]
        count += 1

  # collect all the characters through the zig-zag line we created 
  plain_text = ""

  for j in range(cipher_len):
    for i in range(key):
      if lst[i][j] != "0":
        plain_text += lst[i][j]

  return plain_text # placeholder for the actual return statement

#  Input: strng is a string of characters
#  Output: function converts all characters to lower case and then
#          removes all digits, punctuation marks, and spaces. It
#          returns a single string with only lower case characters
def filter_string ( strng ):
  s_fliter_punc = strng.translate(str.maketrans('', '', string.punctuation))
  s_filter_digit = ''.join([ch for ch in s_fliter_punc if not ch.isdigit()])
  s_filter_space_lower = s_filter_digit.strip().lower()
  s_filter_space_lower = "".join(s_filter_space_lower.split())
  
  return s_filter_space_lower  # placeholder for the actual return statement

#  Input: p is a character in the pass phrase and s is a character
#         in the plain text
#  Output: function returns a single character encoded using the 
#          Vigenere algorithm. You may not use a 2-D list 
def encode_character (p, s):

  # use the ASCII table to calculate the reponding letter # in the 2-d list
  encoded_num = ord(p) - 97 + ord(s) 

  # if the number go beyond the z # in the table, we calculate the distance from z and let it restart from a
  if encoded_num > ord('z'):
    encoded_num = encoded_num - ord('z') + 96

  # tranfer it back to character
  encoded_chr = chr(encoded_num)

  return encoded_chr # placeholder for actual return statement

#  Input: p is a character in the pass phrase and s is a character
#         in the plain text
#  Output: function returns a single character decoded using the 
#          Vigenere algorithm. You may not use a 2-D list 
def decode_character (p, s):
  decoded_num = 0

  # use the ASCII table to calculate the reponding letter # in the 2-d list
  if ord(p) <= ord(s):
      decoded_num = abs(ord(p) - ord(s)) + 97
  elif ord(p) > ord(s):
      decoded_num = 123 - (ord(p) - ord(s)) 
    
  # tranfer it back to character
  decode_character = chr(decoded_num)

  return decode_character # placeholder for actual return statement

#  Input: strng is a string of characters and phrase is a pass phrase
#  Output: function returns a single string that is encoded with
#          Vigenere algorithm
def vigenere_encode ( strng, phrase ):
  ph = ""

  # first make the phrase as the same length as string
  for i in range(len(strng)):
    ph += phrase[i % len(phrase)]
  
  # use the function wrote above to encode the plain string
  encoded_str = ""
  for ch in range(len(strng)):
    encoded_str += encode_character(ph[ch], strng[ch])

  return encoded_str # placeholder for the actual return statement

#  Input: strng is a string of characters and phrase is a pass phrase
#  Output: function returns a single string that is decoded with
#          Vigenere algorithm
def vigenere_decode ( strng, phrase ):
  ph = ""

  # first make the phrase as the same length as string
  for i in range(len(strng)):
    ph += phrase[i % len(phrase)]
  
  # use the function wrote above to encode the plain string
  decoded_str = ""
  for ch in range(len(strng)):
    decoded_str += decode_character(ph[ch], strng[ch])

  return decoded_str # placeholder for the actual return statement

def main():
  # Does it need a blank line at the top?
  # read the plain text from stdin
  strng1 = sys.stdin.readline()
  # read the key from stdin
  key1 = int(sys.stdin.readline())
  # encrypt and print the encoded text using rail fence cipher
  print("Rail Fence Cipher")
  print()
  print("Plain Text:", strng1, end = "")
  print("Key:", key1)
  print("Encoded Text:", rail_fence_encode ( strng1, key1 ))

  # read encoded text from stdin
  strng2 = sys.stdin.readline()
  # read the key from stdin
  key2 = int(sys.stdin.readline())
  # decrypt and print the plain text using rail fence cipher
  print("Encoded Text:", strng2, end = "")
  print("Enter Key:", key2)
  print("Decoded Text:", rail_fence_decode ( strng2, key2 ))

  # read the plain text from stdin
  strng3 = filter_string(sys.stdin.readline())
  # read the pass phrase from stdin
  phrase1 = filter_string(sys.stdin.readline())
  # encrypt and print the encoded text using Vigenere cipher
  print("Vigenere Cipher")
  print()
  print("Plain Text:", strng3, end = "")
  print("Pass Phrase:", phrase1, end = "")
  print("Encoded Text:", vigenere_encode ( strng3, phrase1 ))

  # read the encoded text from stdin
  strng4 = filter_string(sys.stdin.readline())
  # read the pass phrase from stdin
  phrase2 = filter_string(sys.stdin.readline())
  # decrypt and print the plain text using Vigenere cipher
  print("Encoded Text:", strng4, end = "")
  print("Pass Phrase:", phrase2, end = "")
  print("Decoded Text:", vigenere_decode ( strng4, phrase2 ))
  print()
# The line above main is for grading purposes only.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()