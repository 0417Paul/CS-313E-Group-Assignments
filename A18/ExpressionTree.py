#  File: ExpressionTree.py

#  Description:

#  Student Name: Yilin Wen

#  Student UT EID: yw22559

#  Partner Name: Jiaxi Wang

#  Partner UT EID: jw53499

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: 04/7/2022

#  Date Last Modified: 04/11/2022

import sys

operators = ['+', '-', '*', '/', '//', '%', '**']

class Stack (object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append (data)

    def pop(self):
        if(not self.is_empty()):
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

class Node (object):
    def __init__ (self, data = None, lChild = None, rChild = None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild

class Tree (object):
    def __init__ (self):
        self.root = None
    
    # this function takes in the input string expr and 
    # creates the expression tree
    def create_tree (self, expr):
        # initialize the expr tree and the stack to keep track of parent node
        self.root = Node()
        stack = Stack()
        cur = self.root
        # start parsing the expr
        expr_list = expr.split(' ')
        for item in expr_list:
            if item == '(':
                cur.lChild = Node()
                stack.push(cur)
                cur = cur.lChild
            elif item in operators:
                cur.data = item
                stack.push(cur)
                cur.rChild = Node()
                cur = cur.rChild
            elif item == ')':
                if not stack.is_empty():
                    cur = stack.pop()
            # now the item is an operand
            else:
                cur.data = float(item) if '.' in item else int(item)
                cur = stack.pop()
                
    # this function should evaluate the tree's expression
    # returns the value of the expression after being calculated
    def evaluate (self, aNode):
        # evaluate recursively
        if aNode.lChild.data in operators:
            left = self.evaluate(aNode.lChild)
        else:
            left = aNode.lChild.data
        if aNode.rChild.data in operators:
            right = self.evaluate(aNode.rChild)
        else:
            right = aNode.rChild.data
        return float(evaluate_op(left, right, aNode.data))

    # this function should generate the preorder notation of 
    # the tree's expression
    # returns a string of the expression written in preorder notation
    def pre_order (self, aNode):
        pre = []
        # recursively
        if aNode != None:
            pre.append(str(aNode.data))
            pre.append(self.pre_order(aNode.lChild).strip())
            pre.append(self.pre_order(aNode.rChild).strip())
        return ' '.join(pre)

    # this function should generate the postorder notation of 
    # the tree's expression
    # returns a string of the expression written in postorder notation
    def post_order (self, aNode):
        post = []
        # recursively
        if aNode != None:
            post.append(self.post_order(aNode.lChild).strip())
            post.append(self.post_order(aNode.rChild).strip())
            post.append(str(aNode.data))
        return ' '.join(post)

# this function evaluate 2 operands with an operator stored as a str
def evaluate_op(a1, a2, op):
    if op ==  '+':
        return a1 + a2
    if op == '-':
        return a1 - a2
    if op == '*':
        return a1 * a2
    if op == '/':
        return a1 / a2
    if op == '//':
        return a1 // a2
    if op == '%':
        return a1 % a2
    if op == '**':
        return a1 ** a2

# you should NOT need to touch main, everything should be handled for you
def main():
    # read infix expression
    line = sys.stdin.readline()
    expr = line.strip()
 
    tree = Tree()
    tree.create_tree(expr)
    
    # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))

    # get the prefix version of the expression and print
    print("Prefix Expression:", tree.pre_order(tree.root).strip())

    # get the postfix version of the expression and print
    print("Postfix Expression:", tree.post_order(tree.root).strip())

if __name__ == "__main__":
    main()