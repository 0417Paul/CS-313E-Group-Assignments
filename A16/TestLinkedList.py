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
        current = self.first
        while current.next != None:
            current = current.next
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
        current = self.first
        if current == None:
            self.first = new_link
            return
        while current.next != None:
            current = current.next
        current.next = new_link

    # add an item in an ordered list in ascending order
    # assume that the list is already sorted
    def insert_in_order(self, data):
        new_link = Link(data)
        current = self.first
        if current == None or current.data >= new_link.data:
            new_link.next = self.first
            self.first = new_link
            return
        while current.next != None and current.next.data <= new_link.data:
            current = current.next
        new_link.next = current.next
        current.next = new_link

    # search in an unordered list, return None if not found
    def find_unordered(self, data):
        current = self.first
        if current == None:
            return None
        while current.data != data:
            if current.next == None:
                return None
            current = current.next
        return current.data

    # Search in an ordered list, return None if not found
    def find_ordered(self, data):
        current = self.first
        if current == None:
            return None
        while current.data != data:
            if current.next == None:
                return None
            current = current.next
        return current.data

    # Delete and return the first occurrence of a Link containing data
    # from an unordered list or None if not found
    def delete_link(self, data):
        previous = self.first
        current = self.first
        if current == None:
            return None
        while current.data != data:
            if current.next == None:
                return None
            previous = current
            current = current.next

        if current == self.first:
            self.first = self.first.next
        else:
            previous.next = current.next
        return current.data

    # String representation of data 10 items to a line, 2 spaces between data
    def __str__(self):
        current = self.first
        if current == None:
            return ""
        string = ""
        num = 0
        while current != None:
            string += str(current.data)
            string += "  "
            if num == 9:
                string += "\n"
            num = (num + 1) % 10
            current = current.next
        return string

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
        current = self.first
        if current == None:
            return None
        while current != None:
            new_list.insert_first(current.data)
            current = current.next
        return new_list

    # Sort the contents of a list in ascending order and return new list
    # do not change the original list
    def sort_list(self):
        new_list = LinkedList()
        current = self.first
        if current == None:
            return None
        while current != None:
            new_list.insert_in_order(current.data)
            current = current.next
        return new_list

    # Return True if a list is sorted in ascending order or False otherwise
    def is_sorted(self):
        is_s = True
        current = self.first
        while current.next != None:
            is_s = is_s and current.data <= current.next.data
            current = current.next
        return is_s

    # Return True if a list is empty or False otherwise
    def is_empty(self):
        return self.first == None

    # Merge two sorted lists and return new list in ascending order
    # do not change the original lists
    def merge_list(self, other):
        new_list = other.copy_list()
        current = self.first
        while current != None:
            new_list.insert_in_order(current.data)
            current = current.next
        return new_list

    # Test if two lists are equal, item by item and return True
    def is_equal(self, other):
        current1 = self.first
        current2 = other.first
        if current1 == None:
            return current2 == None
        is_same = True
        while current1 != None:
            if current2 == None:
                return False
            is_same = is_same and (current1.data == current2.data)
            current1 = current1.next
            current2 = current2.next
        return is_same

    # Return a new list, keeping only the first occurence of an element
    # and removing all duplicates. Do not change the order of the elements.
    # do not change the original list

    def remove_duplicates(self):
        new_list = LinkedList()
        current = self.first
        while current != None:
            if new_list.find_unordered(current.data) == None:
                new_list.insert_last(current.data)
            current = current.next
        return new_list


def main():
    # Test methods insert_first() and __str__() by adding more than
    # 10 items to a list and printing it.
    my_list = LinkedList()
    for i in range(3, 15):
        my_list.insert_first(i)
    print(my_list)

    # Test method insert_last()
    for i in range(3):
        my_list.insert_last(i)
    print("my_list:", my_list)

    # Test method insert_in_order()
    ordered_list = LinkedList()
    for i in range(5):
        ordered_list.insert_last(i)
    ordered_list.insert_last(10)
    print("ordered_list:", ordered_list)
    ordered_list.insert_in_order(7)
    print("after insert 7:", ordered_list)

    # Test method get_num_links()
    print(ordered_list.get_num_links())
    empty_list = LinkedList()
    print("Empty:", empty_list.get_num_links())

    # Test method find_unordered()
    # Consider two cases - data is there, data is not there
    print("find 7:", my_list.find_unordered(7))
    print("find something not there:", my_list.find_unordered(20))

    # Test method find_ordered()
    # Consider two cases - data is there, data is not there
    print("ordered find 7:", ordered_list.find_ordered(7))
    print("ordered find not there:", ordered_list.find_ordered(6))

    # Test method delete_link()
    # Consider two cases - data is there, data is not there
    print("delete 11:", my_list.delete_link(11))
    print(my_list)
    print("delete 20:", my_list.delete_link(11))
    print(my_list)

    # Test method copy_list()
    copied = ordered_list.copy_list()
    print("copied:", copied)

    # Test method reverse_list()
    reverse_list = ordered_list.reverse_list()
    print("reversed:", reverse_list)

    # Test method sort_list()
    sorted_list = my_list.sort_list()
    print("sorted:", sorted_list)

    # Test method is_sorted()
    # Consider two cases - list is sorted, list is not sorted
    print("is sorted", sorted_list.is_sorted())
    print("is not sorted", my_list.is_sorted())

    # Test method is_empty()
    print("is empty", empty_list.is_empty())
    print("not is empty", my_list.is_empty())

    # Test method merge_list()
    print("merge:", ordered_list.merge_list(sorted_list))

    # Test method is_equal()
    # Consider two cases - lists are equal, lists are not equal
    print("is equal", sorted_list.is_equal(sorted_list.copy_list()))
    print("is not equal", sorted_list.is_equal(my_list))

    # Test remove_duplicates()
    dup = LinkedList()
    for i in range(10):
        dup.insert_last(i)
    for i in range(10):
        dup.insert_last(i)
    print("dup", dup)
    print("removed:", dup.remove_duplicates())


if __name__ == "__main__":
    main()
