#  File: Graph.py

#  Description: This code creates a graph, is able to modify it, and is also able to search it.

#  Student Name: Soomin Hyun

#  Student UT EID: sh52679

# Partner Name: Joon Kim (Unique Number: 52595)

# Partner UT EID: jk45873

# Course Name: CS 313E

# Unique Number: 52600

# Date Created: 11/20/21

# Date Last Modified: 11/21/21

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

  # get first item in the queue
  def first (self):
    return self.queue[0]

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
    self.Vertices.append(Vertex(label))

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
  def get_edge_weight (self, fromVertexLabel, toVertexLabel):
    weight = self.adjMat[self.get_index(fromVertexLabel)][self.get_index(toVertexLabel)]
    if (weight != 0):
      return weight
    else:
      return -1

  # get a list of immediate neighbors that you can go to from a vertex
  # return a list of indices or an empty list if there are none
  def get_neighbors (self, vertexLabel):
    neighbors = []
    vertex_index = self.get_index(vertexLabel)
    for i in range(len(self.adjMat[vertex_index])):
      if (self.adjMat[vertex_index][i] != 0):
        neighbors.append(self.Vertices[i])
    return neighbors

  # return an unvisited vertex adjacent to vertex v (index)
  def get_adj_unvisited_vertex (self, v):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):
        return i
    return -1

  # get a copy of the list of Vertex objects
  def get_vertices(self):
    return self.Vertices

  # do a depth first search in a graph
  def dfs (self, v):
    # create the Stack
    theStack = Stack ()

    # mark the vertex v as visited and push it on the Stack
    (self.Vertices[v]).visited = True
    print (self.Vertices[v])
    theStack.push (v)

    # visit all the other vertices according to depth
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
    vertex_queue = Queue()
    (self.Vertices[v]).visited = True
    print(self.Vertices[v])
    vertex_queue.enqueue(v)

    while (vertex_queue.is_empty() == False):
      next = self.get_adj_unvisited_vertex(vertex_queue.first())
      if (next == -1):
        next = vertex_queue.dequeue()
      else:
        (self.Vertices[next]).visited = True
        print(self.Vertices[next])
        vertex_queue.enqueue(next)

    # the stack is empty, let us rest the flags
    nVert = len(self.Vertices)
    for i in range(nVert):
      (self.Vertices[i]).visited = False
    return

  # delete an edge from the adjacency matrix
  # delete a single edge if the graph is directed
  # delete two edges if the graph is undirected
  def delete_edge (self, fromVertexLabel, toVertexLabel):
    start_index = self.get_index(fromVertexLabel)
    end_index = self.get_index(toVertexLabel)
    self.adjMat[start_index][end_index] = 0
    self.adjMat[end_index][start_index] = 0

  # delete a vertex from the vertex list and all edges from and
  # to it in the adjacency matrix
  def delete_vertex (self, vertexLabel):
    index = self.get_index(vertexLabel)
    del self.Vertices[index]
    for i in range(len(self.adjMat[0])):
      del self.adjMat[i][index]
    del self.adjMat[index]

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

  # get the labels of the vertices that connect the edge that will be removed
  line = sys.stdin.readline()
  line = line.strip()
  line = line.split()
  edge1 = line[0]
  edge2 = line[1]

  # get label of vertex that will be deleted
  line = sys.stdin.readline()
  vertex1 = str(line.strip())

  '''
  # Checking if the cities are correctly printing
  for i in range(len(cities.Vertices)):
    print(cities.Vertices[i])
  print()
  
  #checking edge weight
  print(cities.get_edge_weight('Houston', 'Dallas'))
  print(cities.get_edge_weight('Houston', 'Seattle'))
  print()
  
  # testing list of neighbors
  list_of_neighbors = cities.get_neighbors('Seattle')
  for i in range(len(list_of_neighbors)):
    print(list_of_neighbors[i])
  print()
  '''

  # do the depth first search
  print ("Depth First Search")
  cities.dfs(start_index)
  print ()

  # test breadth first search
  print("Breadth First Search")
  cities.bfs(start_index)
  print()

  # test deletion of an edge
  print("Deletion of an edge")
  print()
  cities.delete_edge(edge1, edge2)
  print('Adjacency Matrix')
  for i in range(len(cities.adjMat)):
    for j in range(len(cities.adjMat[i])):
      if j != len(cities.adjMat[i])-1:
        print(cities.adjMat[i][j], end = ' ')
      else:
        print(cities.adjMat[i][j])
  print()

  # test deletion of a vertex
  print("Deletion of a vertex")
  print()
  cities.delete_vertex(vertex1)
  print('List of Vertices')
  for i in range(len(cities.Vertices)):
    print(cities.Vertices[i])

  print()
  print('Adjacency Matrix')
  for i in range(len(cities.adjMat)):
    for j in range(len(cities.adjMat[i])):
      if j != len(cities.adjMat[i])-1:
        print(cities.adjMat[i][j], end = ' ')
      else:
        print(cities.adjMat[i][j])
  print()

if __name__ == "__main__":
  main()

