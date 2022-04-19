#  File: BST_Cipher.py

#  Description:

#  Student Name: Yilin Wen

#  Student UT EID: yw22559

#  Partner Name: Jiaxi Wang

#  Partner UT EID: jw53499

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: 04/16/2022

#  Date Last Modified: 04/18/2022


import sys

class Node(object):
    def __init__(self, char):
        self.ch = char
        self.left = None
        self.right = None


class Tree (object):
    # the init() function creates the binary search tree with the
    # encryption string. If the encryption string contains any
    # character other than the characters 'a' through 'z' or the
    # space character drop that character.
    def __init__(self, encrypt_str):
        self.root = None
        encrypt_str = encrypt_str.lower()
        for ch in encrypt_str:
            if ord(ch) in range(97, 123) or ord(ch) == 32:
                self.insert(ch)

    # the insert() function adds a node containing a character in
    # the binary search tree. If the character already exists, it
    # does not add that character. There are no duplicate characters
    # in the binary search tree.
    def insert(self, ch):
        new_node = Node(ch)
        if self.root == None:
            self.root = new_node
            return
        #  if the character is already in the tree, do not add it
        #  if the character is not in the tree, add it
        if self.search_letter(ch) == None:
            current = self.root
            parent = self.root
            while current != None:
                parent = current
                if ch < current.ch:
                    current = current.left
                else:
                    current = current.right
            if ch < parent.ch:
                parent.left = new_node
            else:
                parent.right = new_node

    #  helper function to search for duplicates character in the tree
    def search_letter(self, ch):
        current = self.root
        while current != None and current.ch != ch:
            if ch < current.ch:
                current = current.left
            else:
                current = current.right
        return current

    # the search() function will search for a character in the binary
    # search tree and return a string containing a series of lefts
    # (<) and rights (>) needed to reach that character. It will
    # return a blank string if the character does not exist in the tree.
    # It will return * if the character is the root of the tree.
    def search(self, ch):
        current = self.root
        if ch is current.ch:
            return "*"
        else:
            str = ""
            if current is None:
                return ""
            while current is not None and current.ch != ch:
                if ch < current.ch:
                    str += "<"
                    current = current.left
                else:
                    str += ">"
                    current = current.right
            return str

    # the traverse() function will take string composed of a series of
    # lefts (<) and rights (>) and return the corresponding
    # character in the binary search tree. It will return an empty string
    # if the input parameter does not lead to a valid character in the tree.
    def traverse(self, st):
        current = self.root
        for ch in st:
            if ch == "*":
                return current.ch
            else:
                if current is not None:
                    if ch == "<":
                        current = current.left
                    else:
                        current = current.right
                else:
                    return ""
        return current.ch

    # the encrypt() function will take a string as input parameter, convert
    # it to lower case, and return the encrypted string. It will ignore
    # all digits, punctuation marks, and special characters.
    def encrypt(self, st):
        st = st.lower()
        new_str = ''
        for ch in st:
            if ord(ch) in range(97, 123) or ord(ch) == 32:
                new_str += ch
        encrypt_str = ''
        for ch in new_str:
            encrypt_str += self.search(ch) + "!"
        encrypt_str = encrypt_str[:-1]
        return encrypt_str

    # the decrypt() function will take a string as input parameter, and
    # return the decrypted string.
    def decrypt(self, st):
        lst_str = st.split("!")
        decrypt_str = ''
        for ch in lst_str:
            decrypt_str += self.traverse(ch)
        return decrypt_str


def main():
    # read encrypt string
    line = sys.stdin.readline()
    encrypt_str = line.strip()

    # create a Tree object
    the_tree = Tree(encrypt_str)

    # read string to be encrypted
    line = sys.stdin.readline()
    str_to_encode = line.strip()

    # print the encryption
    print(the_tree.encrypt(str_to_encode))

    # read the string to be decrypted
    line = sys.stdin.readline()
    str_to_decode = line.strip()

    # print the decryption
    print(the_tree.decrypt(str_to_decode))


if __name__ == "__main__":
    main()
