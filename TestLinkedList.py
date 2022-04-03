#  File: TestLinkedList.py

#  Description:

#  Student Name: Jiaxi Wang

#  Student UT EID: jw53499  

#  Partner Name: Yilin Wen
 
#  Partner UT EID: yw22559

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: Mar 30

#  Date Last Modified: 

class Link (object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList (object):
  # create a linked list
  # you may add other attributes
  def __init__ (self):
    self.first = None

  # get number of links 
  def get_num_links (self):
  
  # add an item at the beginning of the list
  def insert_first (self, data): 

  # add an item at the end of a list
  def insert_last (self, data): 

  # add an item in an ordered list in ascending order
  # assume that the list is already sorted
  def insert_in_order (self, data): 

  # search in an unordered list, return None if not found
  def find_unordered (self, data): 

  # Search in an ordered list, return None if not found
  def find_ordered (self, data): 

  # Delete and return the first occurrence of a Link containing data
  # from an unordered list or None if not found
  def delete_link (self, data):

  # String representation of data 10 items to a line, 2 spaces between data
  def __str__ (self):

  # Copy the contents of a list and return new list
  # do not change the original list
  def copy_list (self):

  # Reverse the contents of a list and return new list
  # do not change the original list
  def reverse_list (self): 

  # Sort the contents of a list in ascending order and return new list
  # do not change the original list
  def sort_list (self): 

  # Return True if a list is sorted in ascending order or False otherwise
  def is_sorted (self):

  # Return True if a list is empty or False otherwise
  def is_empty (self): 

  # Merge two sorted lists and return new list in ascending order
  # do not change the original lists
  def merge_list (self, other): 

  # Test if two lists are equal, item by item and return True
  def is_equal (self, other):

  # Return a new list, keeping only the first occurence of an element
  # and removing all duplicates. Do not change the order of the elements.
  # do not change the original list
  def remove_duplicates (self):

def main():
  # Test methods insert_first() and __str__() by adding more than
  # 10 items to a list and printing it.

  # Test method insert_last()

  # Test method insert_in_order()

  # Test method get_num_links()

  # Test method find_unordered() 
  # Consider two cases - data is there, data is not there 

  # Test method find_ordered() 
  # Consider two cases - data is there, data is not there 

  # Test method delete_link()
  # Consider two cases - data is there, data is not there 

  # Test method copy_list()

  # Test method reverse_list()

  # Test method sort_list()

  # Test method is_sorted()
  # Consider two cases - list is sorted, list is not sorted

  # Test method is_empty()

  # Test method merge_list()

  # Test method is_equal()
  # Consider two cases - lists are equal, lists are not equal

  # Test remove_duplicates()

if __name__ == "__main__":
  main()
