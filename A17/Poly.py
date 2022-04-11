#  File: Poly.py

#  Description: Represent a polynomial as a Linked List

#  Student Name: Jiaxi Wang

#  Student UT EID: jw53499

#  Partner Name: Yilin Wen

#  Partner UT EID: yw22559

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: Apr 5, 2022

#  Date Last Modified: Apr 7, 2022

from ast import Num
import sys

class Link(object):
    def __init__(self, coeff = 1, exp = 1, next = None):
        self.coeff = coeff
        self.exp = exp
        self.next = next

    def __str__(self):
        return '(' + str(self.coeff) + ', ' + str(self.exp) + ')'

class LinkedList(object):
    def __init__(self):
        self.first = None

  # keep Links in descending order of exponents
    def insert_in_order(self, coeff, exp):
        new_link = Link(coeff, exp)
        previous = self.first
        current = self.first

        # if the list is empty
        if current is None:
            self.first = new_link
            return
        
        # if the exponent of the new link is large than the current exponent
        if current.exp >= new_link.exp:
            while current.exp >= new_link.exp:
                if current.next is None:
                    current.next = new_link
                    return
                else:
                    previous = current
                    current = current.next

            # now update the linked list
            previous.next = new_link
            new_link.next = current
            return 

        # if the exponent of the new link is smaller than the current exponent
        else:
            if previous is self.first:
                self.first = new_link
                new_link.next = current
                return
            else:
                # now update the linked list
                previous.next = new_link
                new_link.next = current
                return
    
    # helper function of copy the original list into a new list
    def copy(self):
        # new linked list
        new_list = LinkedList()
        current = self.first
        while current is not None:
            new_list.insert_in_order(current.coeff, current.exp)
            current = current.next
        return new_list

    # add polynomial p to this polynomial and return the sum
    def add (self, p):
        new_poly = self.copy()
        new_poly.merge()
        p.merge()

        # track the current link of the two linked list
        self_current = new_poly.first
        other_current = p.first

        # find the largest exponent
        large_exp = max(self_current.exp, other_current.exp)

        while large_exp != -1:
            if self_current is None:
                while other_current is not None:
                    new_poly.insert_in_order(other_current.coeff, other_current.exp)
                    other_current = other_current.next
                break
        
             # if the other list's current link firstly reached the end, leave it
            elif other_current is None:
                break   

            else:
                if self_current.exp == other_current.exp:
                    self_current.coeff = self_current.coeff + other_current.coeff
                    self_current = self_current.next
                    other_current = other_current.next
                    large_exp -= 1
                elif self_current.exp > other_current.exp:
                    self_current = self_current.next
                    large_exp -= 1
                elif self_current.exp < other_current.exp:
                    new_poly.insert_in_order(other_current.coeff, other_current.exp)
                    other_current= other_current.next
                    large_exp -= 1
        new_poly.merge()

        # check if link has 0 coefficient. Delete the 0 coefficient
        while True:
            new_poly.delete(0)
            if new_poly.delete(0) is None:
                break
        return new_poly
    
    # helper function merge
    def merge(self):
        previous = self.first
        current = self.first.next

        while previous is not None:
            if current is None:
                return 
            elif previous.exp == current.exp:
                previous.coeff = previous.coeff + current.coeff
                previous.next = current.next
                current = previous.next
            elif previous.exp > current.exp:
                previous = current
                current = current.next
    
    # helper function delete
    def delete(self, coeff):
        previous = self.first
        current = self.first
        if current is None:
            return None
        while current.coeff != coeff:
            if current.next is None:
                return None
            else:
                previous = current
                current = current.next
        if current is self.first:
            self.first = self.first.next
        else:
            previous.next = current.next
        return True

    # multiply polynomial p to this polynomial and return the product
    def mult (self, p):
        new_poly = LinkedList()

        self.merge()
        p.merge()

        self_current = self.first
        while self_current is not None:
            other_current = p.first
            while other_current is not None:
                new_coeff = self_current.coeff * other_current.coeff
                # if the coeff is 0
                if self_current.exp == 0 or other_current.exp == 0:
                    num = max(self_current.exp, other_current.exp)
                    if num == 0:
                        new_poly.insert_in_order(new_coeff, 0)
                        other_current = other_current.next
                    else:
                        new_poly.insert_in_order(new_coeff, num)
                        other_current = other_current.next
                else:
                    new_exp = self_current.exp + other_current.exp
                    new_poly.insert_in_order(new_coeff, new_exp)
                    other_current = other_current.next
            # track the next link
            self_current = self_current.next
        new_poly.merge()

        # check if there is 0 coeff
        while True:
            new_poly.delete(0)
            if new_poly.delete(0) is None:
                break
        return new_poly

    # create a string representation of the polynomial
    def __str__ (self):
        strng = ''
        current = self.first
        while current is not None:
            if current.next is None:
                strng += str(current)
                break
            else:
                strng += str(current) + " + "
                current = current.next
        return strng

def remove_spaces(s):
    s_l = s.split(' ')
    return [int(c) for c in s_l if c != '']

def main():
  # read data from file poly.in from stdin
    p_num = int(sys.stdin.readline().strip())
    p_terms = [remove_spaces(sys.stdin.readline().strip()) for i in range(p_num)]
    sys.stdin.readline()
    q_num = int(sys.stdin.readline().strip())
    q_terms = [remove_spaces(sys.stdin.readline().strip()) for i in range(q_num)]

  # create polynomial p
    p = LinkedList()
    for t in p_terms:
        p.insert_in_order(t[0], t[1])

  # create polynomial q
    q = LinkedList()
    for t in q_terms:
        q.insert_in_order(t[0], t[1])

  # get sum of p and q and print sum
    print(p.add(q))
    
  # get product of p and q and print product
    print(p.mult(q))
if __name__ == "__main__":
  main()