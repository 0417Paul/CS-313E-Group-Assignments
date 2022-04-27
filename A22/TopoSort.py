#  File: TopoSort.py

#  Description:

#  Student Name: Yilin Wen

#  Student UT EID: yw22559

#  Partner Name: Jiaxi Wang

#  Partner UT EID: jw53499

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: 04/21/2022

#  Date Last Modified: 04/25/2022

import sys


class Stack (object):
    def __init__(self):
        self.stack = []

    # add an item to the top of the stack
    def push(self, item):
        self.stack.append(item)

    # remove an item from the top of the stack
    def pop(self):
        return self.stack.pop()

    # check the item on the top of the stack
    def peek(self):
        return self.stack[-1]

    # check if the stack if empty
    def is_empty(self):
        return (len(self.stack) == 0)

    # return the number of elements in the stack
    def size(self):
        return (len(self.stack))


class Queue (object):
    def __init__(self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)

    # remove an item from the beginning of the queue
    def dequeue(self):
        return (self.queue.pop(0))

    # check if the queue is empty
    def is_empty(self):
        return (len(self.queue) == 0)

    # return the size of the queue
    def size(self):
        return (len(self.queue))

    # only return the item at the end of the queue
    def get_next_item(self):
        if self.size() > 0:
            return self.queue[0]
        return None


class Vertex (object):
    def __init__(self, label):
        self.label = label
        self.visited = False
        self.in_degree = 0

    # determine if a vertex was visited
    def was_visited(self):
        return self.visited

    # determine the label of the vertex
    def get_label(self):
        return self.label

    # string representation of the vertex
    def __str__(self):
        return str(self.label)


class Graph (object):
    def __init__(self):
        self.Vertices = []
        self.adjMat = []

    # check if a vertex is already in the graph
    def has_vertex(self, label):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if (label == (self.Vertices[i]).get_label()):
                return True
        return False

    # given the label get the index of a vertex
    def get_index(self, label):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if (label == (self.Vertices[i]).get_label()):
                return i
        return -1

    # add a Vertex with a given label to the graph
    def add_vertex(self, label):
        if (self.has_vertex(label)):
            return

        # add vertex to the list of vertices
        self.Vertices.append(Vertex(label))

        # add a new column in the adjacency matrix
        nVert = len(self.Vertices)
        for i in range(nVert - 1):
            (self.adjMat[i]).append(0)

        # add a new row for the new vertex
        new_row = []
        for i in range(nVert):
            new_row.append(0)
        self.adjMat.append(new_row)

    # add weighted directed edge to graph
    def add_directed_edge(self, start, finish, weight=1):
        self.adjMat[start][finish] = weight
        self.Vertices[finish].in_degree += 1

    # add weighted undirected edge to graph
    def add_undirected_edge(self, start, finish, weight=1):
        self.adjMat[start][finish] = weight
        self.adjMat[finish][start] = weight

    # return an unvisited vertex adjacent to vertex v (index)
    def get_adj_unvisited_vertex(self, v):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):
                return i
        return -1

    # delete an edge from start index to end index
    def delete_directed_edge(self, start, finish):
        self.adjMat[start][finish] = 0

    # delete a vertex.
    def delete_vertex(self, label):
        v = self.get_index(label)
        for i in range(len(self.adjMat[v])):
            if self.adjMat[v][i] != 0:
                self.Vertices[i].in_degree -= 1
        for i in range(len(self.Vertices)):
            del self.adjMat[i][v]
        del self.Vertices[v]
        del self.adjMat[v]

    # determine if a directed graph has a cycle
    # this function should return a boolean and not print the result
    def has_cycle(self):
        numV = len(self.Vertices)
        if numV != 0:
            visited = Stack()
            self.Vertices[0].visited = True
            visited.push(0)
            while not visited.is_empty():
                next_v = self.get_adj_unvisited_vertex(visited.peek())
                if next_v == -1:
                    next_v = visited.pop()
                else:
                    self.Vertices[next_v].visited = True
                    visited.push(next_v)
                    for i in range(numV):
                        if self.adjMat[next_v][i] != 0:
                            if i in visited.stack:
                                return True
            return False
        return False

    # return a list of vertices after a topological sort
    # this function should not print the list.
    def topo_sort(self):
        final = []
        while len(self.Vertices) > 0:
            # print(len(self.Vertices))
            zero_list = []
            for ver in self.Vertices:
                if ver.in_degree == 0:
                    zero_list.append(ver)
            zero_list.sort(key=lambda x: x.label)
            for i in zero_list:
                self.delete_vertex(i.label)
                final.append(i.label)

        return final


def main():
    # create the Graph object
    gragh_1 = Graph()

# Read first line of the file.
    numV = int(sys.stdin.readline().strip())
    # Add vertices based on the give number.
    for i in range(numV):
        gragh_1.add_vertex(sys.stdin.readline().strip())
    numE = int(sys.stdin.readline().strip())
    for i in range(numE):
        edges_str = sys.stdin.readline().strip()
        gragh_1.add_directed_edge(gragh_1.get_index(edges_str[0]), gragh_1.get_index(edges_str[-1]))

    # test if a directed graph has a cycle
    if gragh_1.has_cycle():
        print("The Graph has a cycle.")
    else:
        print("The Graph does not have a cycle.")
        print("\nList of vertices after toposort")
        final_list = gragh_1.topo_sort()
        print(final_list)


if __name__ == "__main__":
    main()
