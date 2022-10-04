#  File: Triangles.py

#  Description: Find vertices on the graph that are not in a triangle

#  Student Name: Soomin Hyun

#  Student UT EID: sh52679

#  Course Name: CS 313E

#  Unique Number: 52600

#  Date Created: 12/3/2021

#  Date Last Modified: 12/3/2021


class Vertex(object):
    def __init__(self, label):
        self.label = label

    # determine the label of the vertex
    def get_label(self):
        return self.label

    # string representation of the vertex
    def __str__(self):
        return str(self.label)


class Graph(object):
    def __init__(self):
        self.Vertices = []
        self.adjMat = []

    # add a Vertex with a given label to the graph
    def add_vertex(self, label):
        # add vertex to the list of vertices
        self.Vertices.append(Vertex(label))

    # add weighted undirected edge to graph
    def set_adj_matrix(self, mat):
        self.adjMat = mat

    # finds vertices that are not in a triangle
    # returns an ordered list of the vertices that are not in triangles
    # if all vertices belong to triangles, return [-1]
    def find_non_triangle_vertices(self):
        not_in_triangle = []
        check_this = []

        for i in range(len(self.Vertices)):
            each_check = []
            for j in range(len(self.Vertices)):
                if self.adjMat[i][j] == 1:
                    each_check.append(j)
            check_this.append(each_check)

        for i in range(len(check_this)):
            boolean = False
            for each in check_this[i]:
                for each2 in check_this[each]:
                    if each2 != i:
                        for final in check_this[each2]:
                            if final == i:
                                boolean = True
            if boolean == False:
                not_in_triangle.append(i)

        if bool(not_in_triangle) == False:
            not_in_triangle.append(-1)

        return not_in_triangle


# DO NOT MODIFY THIS METHOD
def main():
    graph = Graph()
    num = 0
    matrix = []
    # read in the adjacency matrix
    n = int(input())
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
        # add vertex
        graph.add_vertex(num)
        num += 1
    # update adjMat
    graph.set_adj_matrix(matrix)

    # print result
    print(' '.join([str(i) for i in graph.find_non_triangle_vertices()]))


if __name__ == "__main__":
    main()
