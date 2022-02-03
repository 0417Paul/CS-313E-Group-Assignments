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
  cipher_len = len(strng)
  lst = [["0"] * cipher_len for i in range(key)]
  plain_len = 0
  plain_num = 0

  # when the decoding process haven't been done
  while plain_len < cipher_len:
    
    # going through a zig-zag line in the list starting from [0, 0] and mark these places as "1"
    while plain_num <= key - 1:
      lst[plain_num][plain_len] = "1"
      plain_len += 1
      plain_num += 1

      # break the loop after the last chr has been reached
      if plain_len >= cipher_len:
        break
    # break the loop after the last chr has been reached
    if plain_len >= cipher_len:
      break
    # go back to row 0 after passing the last line
    plain_num -= 2

    while plain_num > 0:
      lst[plain_num][plain_len] = "1"
      # go back to the line above and move 1 unit to the right
      plain_num -= 1
      plain_len += 1
      
      # break the loop after the last chr has been reached
      if plain_len >= cipher_len:
        break

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
  strng3 = sys.stdin.readline()
  # read the pass phrase from stdin
  phrase1 = sys.stdin.readline()
  # encrypt and print the encoded text using Vigenere cipher
  print("Vigenere Cipher")
  print()
  print("Plain Text:", strng3, end = "")
  print("Pass Phrase:", phrase1, end = "")
  print("Encoded Text:", vigenere_encode ( strng3, phrase1 ))
  print()

  # read the encoded text from stdin
  strng4 = sys.stdin.readline()
  # read the pass phrase from stdin
  phrase2 = sys.stdin.readline()
  # decrypt and print the plain text using Vigenere cipher
  print("Encoded Text:", strng4, end = "")
  print("Pass Phrase:", phrase2, end = "")
  print("Decoded Text:", vigenere_decode ( strng4, phrase2 ))
  print()
# The line above main is for grading purposes only.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()