#  File: TestLinkedList.py

#  Description:

#  Student Name: Yilin Wen

#  Student UT EID: yw22559

#  Partner Name: Jiaxi Wang

#  Partner UT EID: jw53499

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: 04/02/2022

#  Date Last Modified: 04/04/2022

from sklearn.exceptions import NonBLASDotWarning


class Link (object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList (object):
    # create a linked list
    # you may add other attributes
    def __init__(self):
        self.first = None

    # get number of links
    def get_num_links(self):
        if self.first == None:
            return 0
        num = 1
        cur = self.first
        while cur.next != None:
            cur = cur.next
            num += 1
        return num

    # add an item at the beginning of the list
    def insert_first(self, data):
        new_link = Link(data)
        new_link.next = self.first
        self.first = new_link

    # add an item at the end of a list
    def insert_last(self, data):
        new_link = Link(data)
        cur = self.first
        if cur == None:
            self.first = new_link
            return
        while cur.next != None:
            cur = cur.next
        cur.next = new_link

    # add an item in an ordered list in ascending order
    # assume that the list is already sorted
    def insert_in_order(self, data):
        new_link = Link(data)
        cur = self.first
        if cur == None or cur.data >= new_link.data:
            new_link.next = self.first
            self.first = new_link
            return
        while cur.next != None and cur.next.data <= new_link.data:
            cur = cur.next
        new_link.next = cur.next
        cur.next = new_link

    # search in an unordered list, return None if not found
    def find_unordered(self, data):
        cur = self.first
        if cur == None:
            return None
        while cur.data != data:
            if cur.next == None:
                return None
            cur = cur.next
        return cur.data

    # Search in an ordered list, return None if not found
    def find_ordered(self, data):
        cur = self.first
        if cur == None:
            return None
        while cur.data != data:
            if cur.next == None:
                return None
            cur = cur.next
        return cur.data

    # Delete and return the first occurrence of a Link containing data
    # from an unordered list or None if not found
    def delete_link(self, data):
        prev = self.first
        cur = self.first
        if cur == None:
            return None
        while cur.data != data:
            if cur.next == None:
                return None
            prev = cur
            cur = cur.next

        if cur == self.first:
            self.first = self.first.next
        else:
            prev.next = cur.next
        return cur.data

    # String representation of data 10 items to a line, 2 spaces between data

    def __str__(self):
        cur = self.first
        s = ""
        while cur != None:
            s += str(cur.data) + "  "
            cur = cur.next
        return s

    # Copy the contents of a list and return new list
    # do not change the original list
    def copy_list(self):
        new_list = LinkedList()
        new_list.first = self.first
        return new_list

    # Reverse the contents of a list and return new list
    # do not change the original list
    def reverse_list(self):
        new_list = LinkedList()
        cur = self.first
        if cur == None:
            return None
        while cur != None:
            new_list.insert_first(cur.data)
            cur = cur.next
        return new_list

    # Sort the contents of a list in ascending order and return new list
    # do not change the original list
    def sort_list(self):
        new_list = LinkedList()
        cur = self.first
        if cur == None:
            return None
        while cur != None:
            new_list.insert_in_order(cur.data)
            cur = cur.next
        return new_list

    # Return True if a list is sorted in ascending order or False otherwise
    def is_sorted(self):
        final = True
        cur = self.first
        while cur.next != None:
            final = final and cur.data <= cur.next.data
            cur = cur.next
        return final

    # Return True if a list is empty or False otherwise
    def is_empty(self):
        return self.first == None

    # Merge two sorted lists and return new list in ascending order
    # do not change the original lists
    def merge_list(self, other):
        new_list = other.copy_list()
        cur = self.first
        while cur != None:
            new_list.insert_in_order(cur.data)
            cur = cur.next
        return new_list

    # Test if two lists are equal, item by item and return True

    def is_equal(self, other):
        cur = self.first
        cur2 = other.first
        if cur == None and cur2 == None:
            return True
        if cur == None or cur2 == None:
            return False
        while cur != None:
            if cur.data != cur2.data:
                return False
            cur = cur.next
            cur2 = cur2.next
        return True

    # Return a new list, keeping only the first occurence of an element
    # and removing all duplicates. Do not change the order of the elements.
    # do not change the original list
    def remove_duplicates(self):
        new_list = LinkedList()
        cur = self.first
        while cur != None:
            if new_list.find_unordered(cur.data) == None:
                new_list.insert_last(cur.data)
            cur = cur.next
        return new_list


def main():
    # Test methods insert_first() and __str__() by adding more than
    # 10 items to a list and printing it.
    my_list = LinkedList()
    for i in range(10):
        my_list.insert_first(i)
    print(my_list)

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
