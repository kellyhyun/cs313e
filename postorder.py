'''
# Python3 program to print postorder
# traversal from preorder and inorder
# traversals

# A utility function to search x in
# arr[] of size n
def search(arr, x, n):
    for i in range(n):
        if (arr[i] == x):
            return i

    return -1


# Prints postorder traversal from
# given inorder and preorder traversals
def printPostOrder(In, pre, n):
    # The first element in pre[] is always
    # root, search it in in[] to find left
    # and right subtrees
    root = search(In, pre[0], n)

    # If left subtree is not empty,
    # print left subtree
    if (root != 0):
        printPostOrder(In, pre[1:n], root)

    # If right subtree is not empty,
    # print right subtree
    if (root != n - 1):
        printPostOrder(In[root + 1: n],
                       pre[root + 1: n],
                       n - root - 1)

    # Print root
    print(pre[0], end=" ")


# Driver code
#4 2 8 5 3 1 6 7
In = [4, 2, 8, 5, 3, 1, 6, 7]
#  8 2 4 3 5 1 6 7
pre = [8, 2, 4, 3, 5, 1, 6, 7]
n = len(In)

print("Postorder traversal ")

printPostOrder(In, pre, n)

# This code is contributed by avanitrachhadiya2155



###################################################################

import sys


class MaxHeap:

	def __init__(self, maxsize):

		self.maxsize = maxsize
		self.size = 0
		self.Heap = [0] * (self.maxsize + 1)
		self.Heap[0] = sys.maxsize
		self.FRONT = 1

	# Function to return the position of
	# parent for the node currently
	# at pos
	def parent(self, pos):

		return pos // 2

	# Function to return the position of
	# the left child for the node currently
	# at pos
	def leftChild(self, pos):

		return 2 * pos

	# Function to return the position of
	# the right child for the node currently
	# at pos
	def rightChild(self, pos):

		return (2 * pos) + 1

	# Function that returns true if the passed
	# node is a leaf node
	def isLeaf(self, pos):

		if pos >= (self.size // 2) and pos <= self.size:
			return True
		return False

	# Function to swap two nodes of the heap
	def swap(self, fpos, spos):

		self.Heap[fpos], self.Heap[spos] = (self.Heap[spos],
											self.Heap[fpos])

	# Function to heapify the node at pos
	def maxHeapify(self, pos):

		# If the node is a non-leaf node and smaller
		# than any of its child
		if not self.isLeaf(pos):
			if (self.Heap[pos] < self.Heap[self.leftChild(pos)] or
					self.Heap[pos] < self.Heap[self.rightChild(pos)]):

				# Swap with the left child and heapify
				# the left child
				if (self.Heap[self.leftChild(pos)] >
						self.Heap[self.rightChild(pos)]):
					self.swap(pos, self.leftChild(pos))
					self.maxHeapify(self.leftChild(pos))

				# Swap with the right child and heapify
				# the right child
				else:
					self.swap(pos, self.rightChild(pos))
					self.maxHeapify(self.rightChild(pos))

	# Function to insert a node into the heap
	def insert(self, element):

		if self.size >= self.maxsize:
			return
		self.size += 1
		self.Heap[self.size] = element

		current = self.size

		while (self.Heap[current] >
			   self.Heap[self.parent(current)]):
			self.swap(current, self.parent(current))
			current = self.parent(current)

	# Function to print the contents of the heap
	def Print(self):

		for i in range(1, (self.size // 2) + 1):
			print(" PARENT : " + str(self.Heap[i]) +
				  " LEFT CHILD : " + str(self.Heap[2 * i]) +
				  " RIGHT CHILD : " + str(self.Heap[2 * i + 1]))

	# Function to remove and return the maximum
	# element from the heap
	def extractMax(self):

		popped = self.Heap[self.FRONT]
		self.Heap[self.FRONT] = self.Heap[self.size]
		self.size -= 1
		self.maxHeapify(self.FRONT)

		return popped


# Driver Code
if __name__ == "__main__":
	print('The maxHeap is ')

	maxHeap = MaxHeap(15)
	maxHeap.insert(78)
	maxHeap.insert(101)
	maxHeap.insert(119)
	maxHeap.insert(89)
	maxHeap.insert(111)
	maxHeap.insert(114)
	maxHeap.insert(107)
	maxHeap.insert(69)
	maxHeap.insert(105)
	maxHeap.insert(116)
	maxHeap.insert(121)

	maxHeap.Print()

	print("The Max val is " + str(maxHeap.extractMax()))
'''

# A Python program to print topological sorting of a graph
# using indegrees
from collections import defaultdict


# Class to represent a graph
class Graph:
	def __init__(self, vertices):
		self.graph = defaultdict(list)  # dictionary containing adjacency List
		self.V = vertices  # No. of vertices

	# function to add an edge to graph
	def addEdge(self, u, v):
		self.graph[u].append(v)

	# The function to do Topological Sort.
	def topologicalSort(self):

		# Create a vector to store indegrees of all
		# vertices. Initialize all indegrees as 0.
		in_degree = [0] * (self.V)

		# Traverse adjacency lists to fill indegrees of
		# vertices. This step takes O(V + E) time
		for i in self.graph:
			for j in self.graph[i]:
				in_degree[j] += 1

		# Create an queue and enqueue all vertices with
		# indegree 0
		queue = []
		for i in range(self.V):
			if in_degree[i] == 0:
				queue.append(i)

		# Initialize count of visited vertices
		cnt = 0

		# Create a vector to store result (A topological
		# ordering of the vertices)
		top_order = []

		# One by one dequeue vertices from queue and enqueue
		# adjacents if indegree of adjacent becomes 0
		while queue:

			# Extract front of queue (or perform dequeue)
			# and add it to topological order
			u = queue.pop(0)
			top_order.append(u)

			# Iterate through all neighbouring nodes
			# of dequeued node u and decrease their in-degree
			# by 1
			for i in self.graph[u]:
				in_degree[i] -= 1
				# If in-degree becomes zero, add it to queue
				if in_degree[i] == 0:
					queue.append(i)

			cnt += 1

		# Check if there was a cycle
		if cnt != self.V:
			print
			"There exists a cycle in the graph"
		else:
			# Print topological order
			print(top_order)


g = Graph(9)
g.addEdge(0, 3)
g.addEdge(0, 4)
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 4)
g.addEdge(2, 6)
g.addEdge(3, 4)
g.addEdge(3, 5)
g.addEdge(4, 8)
g.addEdge(6, 7)
g.addEdge(8, 7)
g.addEdge(7, 5)


print("Following is a Topological Sort of the given graph")
g.topologicalSort()

# This code is contributed by Neelam Yadav


# Python program to print topological sorting of a DAG
from collections import defaultdict


# Class to represent a graph
class Graph:
	def __init__(self, vertices):
		self.graph = defaultdict(list)  # dictionary containing adjacency List
		self.V = vertices  # No. of vertices

	# function to add an edge to graph
	def addEdge(self, u, v):
		self.graph[u].append(v)

	# A recursive function used by topologicalSort
	def topologicalSortUtil(self, v, visited, stack):

		# Mark the current node as visited.
		visited[v] = True

		# Recur for all the vertices adjacent to this vertex
		for i in self.graph[v]:
			if visited[i] == False:
				self.topologicalSortUtil(i, visited, stack)

		# Push current vertex to stack which stores result
		stack.insert(0, v)

	# The function to do Topological Sort. It uses recursive
	# topologicalSortUtil()
	def topologicalSort(self):
		# Mark all the vertices as not visited
		visited = [False] * self.V
		stack = []

		# Call the recursive helper function to store Topological
		# Sort starting from all vertices one by one
		for i in range(self.V):
			if visited[i] == False:
				self.topologicalSortUtil(i, visited, stack)

		# Print contents of stack
		print(stack)


g = Graph(9)
g.addEdge(0, 3)
g.addEdge(0, 4)
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 4)
g.addEdge(2, 6)
g.addEdge(3, 4)
g.addEdge(3, 5)
g.addEdge(4, 8)
g.addEdge(6, 7)
g.addEdge(8, 7)
g.addEdge(7, 5)


print("Following is a Topological Sort of the given graph")
g.topologicalSort()