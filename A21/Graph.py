#  File: Graph.py

#  Description: creating a graph from an input data file called graph.txt.

#  Student Name: Jiaxi Wang

#  Student UT EID: jw53499

#  Partner Name: Yilin Wen

#  Partner UT EID: yw22559

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: Apr 20, 2022

#  Date Last Modified: Apr 20, 2022

import sys

class Stack (object):
    def __init__ (self):
        self.stack = []

    # add an item to the top of the stack
    def push (self, item):
        self.stack.append (item)

    # remove an item from the top of the stack
    def pop (self):
        return self.stack.pop()

    # check the item on the top of the stack
    def peek (self):
        return self.stack[-1]

    # check if the stack if empty
    def is_empty (self):
        return (len (self.stack) == 0)

    # return the number of elements in the stack
    def size (self):
        return (len (self.stack))


class Queue (object):
    def __init__ (self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue (self, item):
        self.queue.append (item)

    # remove an item from the beginning of the queue
    def dequeue (self):
        return (self.queue.pop(0))

    # check if the queue is empty
    def is_empty (self):
        return (len (self.queue) == 0)

    # return the size of the queue
    def size (self):
        return (len (self.queue))


class Vertex (object):
    def __init__ (self, label):
        self.label = label
        self.visited = False

    # determine if a vertex was visited
    def was_visited (self):
        return self.visited

    # determine the label of the vertex
    def get_label (self):
        return self.label

    # string representation of the vertex
    def __str__ (self):
            return str (self.label)


class Graph (object):
    def __init__ (self):
        self.Vertices = []
        self.adjMat = []

    # print the adjMat
    def print_adj(self):
        if len(self.adjMat) != 0:
            out = []
            for row in self.adjMat:
                c_row = [str(i) for i in row]
                out.append(" ".join(c_row))
            print("\n".join(out))

    # check if a vertex is already in the graph
    def has_vertex (self, label):
        nVert = len (self.Vertices)
        for i in range (nVert):
            if (label == (self.Vertices[i]).get_label()):
                return True
        return False

    # given the label get the index of a vertex
    def get_index (self, label):
        nVert = len (self.Vertices)
        for i in range (nVert):
            if (label == (self.Vertices[i]).get_label()):
                return i
        return -1

    # add a Vertex with a given label to the graph
    def add_vertex (self, label):
        if (self.has_vertex (label)):
            return

        # add vertex to the list of vertices
        self.Vertices.append (Vertex (label))

        # add a new column in the adjacency matrix
        nVert = len (self.Vertices)
        for i in range (nVert - 1):
            (self.adjMat[i]).append (0)

        # add a new row for the new vertex
        new_row = []
        for i in range (nVert):
            new_row.append (0)
        self.adjMat.append (new_row)

    # add weighted directed edge to graph
    def add_directed_edge (self, start, finish, weight = 1):
        self.adjMat[start][finish] = weight

    # add weighted undirected edge to graph
    def add_undirected_edge (self, start, finish, weight = 1):
        self.adjMat[start][finish] = weight
        self.adjMat[finish][start] = weight

    # get edge weight between two vertices
    # return -1 if edge does not exist
    def get_edge_weight(self, fromVertexLabel, toVertexLabel):
        nVert = len(self.Vertices)
        if fromVertexLabel in range(nVert) and toVertexLabel in range(nVert):
            edge = self.adjMat[self.get_index(fromVertexLabel)][self.get_index(toVertexLabel)]
            if edge == 0:
                return -1
            return edge
        return -1

    # get a list of immediate neighbors that you can go to from a vertex
    # return a list of indices or an empty list if there are none
    def get_neighbors (self, vertexLabel):
        neighbors = []
        v = self.get_index(vertexLabel)
        for i in range(len(self.adjMat[v])):
            if self.adjMat[v][i] != 0:
                neighbors.append([v, i])
        return neighbors

    # return an unvisited vertex adjacent to vertex v (index)
    def get_adj_unvisited_vertex (self, v):
        nVert = len (self.Vertices)
        for i in range (nVert):
            if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):
                return i
        return -1

    # get a copy of the list of Vertex objects
    def get_vertices (self):
        return self.Vertices.copy()

    # do a depth first search in a graph
    def dfs (self, v):
        # create the Stack
        theStack = Stack ()

        # mark the vertex v as visited and push it on the Stack
        (self.Vertices[v]).visited = True
        print (self.Vertices[v])
        theStack.push (v)

        # visit all the other vertices according to depth
        # done when the stack is empty
        while (not theStack.is_empty()):
            # get an adjacent unvisited vertex
            u = self.get_adj_unvisited_vertex (theStack.peek())
            if (u == -1):
                u = theStack.pop()
            else:
                (self.Vertices[u]).visited = True
                print (self.Vertices[u])
                theStack.push (u)

        # the stack is empty, let us rest the flags
        nVert = len (self.Vertices)
        for i in range (nVert):
            (self.Vertices[i]).visited = False

        # do the breadth first search in a graph
        def bfs (self, v):
            return

    # do the breadth first search in a graph
    def bfs (self, v):
        frontier = Queue() # keep a queue for unvisited neighbors
        frontier.enqueue(v)
        self.Vertices[v].visited = True
        while not frontier.is_empty():
            cur = frontier.dequeue()
            print(self.Vertices[cur])
            # enqueue all unvisitied neighbors
            while self.get_adj_unvisited_vertex(cur) != -1:
                frontier.enqueue(self.get_adj_unvisited_vertex(cur))
                self.Vertices[self.get_adj_unvisited_vertex(cur)].visited = True

        # need to reset the .visited for each vertex
        for i in self.Vertices:
            i.visited = False
    
        return

    # delete an edge from the adjacency matrix
    # delete a single edge if the graph is directed
    # delete two edges if the graph is undirected
    def delete_edge(self, fromVertexLabel, toVertexLabel):
        # get the index of the two vertexes
        u = self.get_index(fromVertexLabel)
        v = self.get_index(toVertexLabel)
        # for undirected graph, set the both edge to 0
        if self.adjMat[u][v] == self.adjMat[v][u]:
            self.adjMat[u][v] = 0
            self.adjMat[v][u] = 0
        # for directed graph, set one edge to 0
        else:
            self.adjMat[u][v] = 0

    # delete a vertex from the vertex list and all edges from and
    # to it in the adjacency matrix
    def delete_vertex(self, vertexLabel):
        # get the index of the vertex and the length of the vertices list
        v = self.get_index(vertexLabel)
        nVert = len(self.Vertices)
        # delete the column
        for i in range(nVert):
            self.adjMat[i].pop(v)
        # delete the row
        self.adjMat.pop(v)
        # delete the vertices from the list
        self.Vertices.pop(v)



def main():
    # create the Graph object
    cities = Graph()

    # read the number of vertices
    line = sys.stdin.readline()
    line = line.strip()
    num_vertices = int (line)

    # read the vertices to the list of Vertices
    for i in range (num_vertices):
        line = sys.stdin.readline()
        city = line.strip()
        cities.add_vertex (city)

    # read the number of edges
    line = sys.stdin.readline()
    line = line.strip()
    num_edges = int (line)

    # read each edge and place it in the adjacency matrix
    for i in range (num_edges):
        line = sys.stdin.readline()
        edge = line.strip()
        edge = edge.split()
        start = int (edge[0])
        finish = int (edge[1])
        weight = int (edge[2])

        cities.add_directed_edge (start, finish, weight)

    # read the starting vertex for dfs and bfs
    line = sys.stdin.readline()
    start_vertex = line.strip()

    # get the index of the starting vertex
    start_index = cities.get_index (start_vertex)

    # test depth first search
    print("Depth First Search")
    cities.dfs(start_index)

    # test breadth first search
    print("\nBreadth First Search")
    cities.bfs(start_index)
    print()
    
    # test deletion of an edge
    print("Deletion of an edge\n")
    # read 2 vertices
    del_cities = sys.stdin.readline().strip().split(" ")
    cities.delete_edge(del_cities[0], del_cities[1])
    print("Adjacency Matrix")
    cities.print_adj()
    print()   

    # test deletion of a vertex
    print("Deletion of a vertex\n")
    # read deleted city
    del_city = sys.stdin.readline().strip()
    cities.delete_vertex(del_city)
    print("List of Vertices")
    for c in cities.Vertices:
        print(c)
    print()
    print("Adjacency Matrix")
    cities.print_adj()
    print()
  
    
if __name__ == "__main__":
  main()
