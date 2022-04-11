#  File: Poly.py

#  Description: Represent a polynomial as a Linked List

#  Student Name: Jiaxi Wang

#  Student UT EID: jw53499

#  Partner Name: Yilin Wen

#  Partner UT EID: yw22559

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: Apr 5, 2022

#  Date Last Modified:

import sys

class Link(object):
    def __init__(self, coeff = 1, exp = 1, next = None):
        self.coeff = coeff
        self.exp = exp
        self.next = next

    def __str__(self):
        return '(' + str(self.coeff) + ', ' + str(self.exp) + ')'

class LinkedList (object):
    def __init__(self):
        self.first = None

  # keep Links in descending order of exponents
    def insert_in_order (self, coeff, exp):

  # add polynomial p to this polynomial and return the sum
    def add (self, p):

  # multiply polynomial p to this polynomial and return the product
    def mult (self, p):

  # create a string representation of the polynomial
    def __str__ (self):

def main():
  # read data from file poly.in from stdin

  # create polynomial p

  # create polynomial q

  # get sum of p and q and print sum

  # get product of p and q and print product

if __name__ == "__main__":
    main()