#  File: TestBinaryTree.py

#  Description: you will be adding to the classes Node and Tree that we developed in class and testing them. 
#  There are several short methods that you will have to write.

#  Student Name: Jiaxi Wang

#  Student UT EID: jw53499      

#  Partner Name: Yilin Wen

#  Partner UT EID: yw22559

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: Apr 14, 2022

#  Date Last Modified: Apr 14, 2022

import sys

class Node (object):
    def __init__ (self, data):
        self.data = data
        # lc and rc are left child and right child 
        self.lc = None
        self.rc = None


class Tree (object):

    def __init__ (self):
        self.root = None

    # from lecture notes
    # insert data into the tree
    def insert (self, data):
        new_node = Node (data)

        # if the tree is empty
        if (self.root == None):
            self.root = new_node
            return

        else:
            current = self.root
            parent = self.root
            while (current != None):
                parent = current
                # if the data is less than current data, go to left, otherwise go to right
                if (data < current.data):
                    current = current.lc
                else:
                    current = current.rc

            
            if (data < parent.data):
                parent.lc = new_node
            else:
                parent.rc = new_node

    # Returns true if two binary trees are similar
    def is_similar (self, pNode):
        def is_help (node1, node2):
            # if both trees are empty or no more child
            if node1 is None or node2 is None:
                if node1 is None and node2 is None:
                    return True
                else:
                    return False
            else:
                # compare the data
                if node1.data == node2.data:
                    return is_help(node1.lc, node2.lc) and is_help(node1.rc, node2.rc)
                else:
                    return False

        return is_help(self.root, pNode.root)

    # Returns a list of nodes at a given level from left to right
    def get_level (self, level): 
        lst = []

        def get_help (g_node, g_level, count = 0):
            if g_level == count and g_node is not None:
                lst.append(g_node)

            elif g_node is None:
                return

            else:
                get_help(g_node.lc, g_level, count + 1)
                get_help(g_node.rc, g_level, count + 1)

        get_help(self.root, level)
        return lst

    # Returns the height of the tree
    def get_height (self): 
        def get_help (g_node):
            if g_node is None:
                return -1
            else:
                return max(get_help(g_node.lc), get_help(g_node.rc)) + 1
        return get_help(self.root)

    # Returns the number of nodes in the left subtree and
    # the number of nodes in the right subtree and the root
    def num_nodes (self):
        def num_help (n_node):
            if n_node is None:
                return 0
            else:
                return num_help(n_node.lc) + num_help(n_node.rc) + 1
        return num_help(self.root)

def main():
    # Create three trees - two are the same and the third is different
	line = sys.stdin.readline()
	line = line.strip()
	line = line.split()
	tree1_input = list (map (int, line)) 	# converts elements into ints

	line = sys.stdin.readline()
	line = line.strip()
	line = line.split()
	tree2_input = list (map (int, line)) 	# converts elements into ints

	line = sys.stdin.readline()
	line = line.strip()
	line = line.split()
	tree3_input = list (map (int, line)) 	# converts elements into ints

    # Test your method is_similar()

    # Print the various levels of two of the trees that are different

    # Get the height of the two trees that are different

    # Get the total number of nodes a binary search tree

if __name__ == "__main__":
    main()