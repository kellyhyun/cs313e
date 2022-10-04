#  File: Hull.py

#  Description: determines a convex hull and prints its vertices starting from the left most vertex and going clockwise around the convex hull

#  Student Name: Soomin Hyun

#  Student UT EID: sh52679

#  Partner Name: Joon Kim (Unique Number: 52595)

#  Partner UT EID: jk45873

#  Course Name: CS 313E

#  Unique Number: 52600

#  Date Created:9/24/21

#  Date Last Modified:9/27/21

import sys

import math


class Point(object):
    # constructor
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # get the distance to another Point object
    def dist(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)

    # string representation of a Point
    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    # equality tests of two Points
    def __eq__(self, other):
        tol = 1.0e-8
        return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

    def __ne__(self, other):
        tol = 1.0e-8
        return ((abs(self.x - other.x) >= tol) or (abs(self.y - other.y) >= tol))

    def __lt__(self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return False
            else:
                return (self.y < other.y)
        return (self.x < other.x)

    def __le__(self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return True
            else:
                return (self.y <= other.y)
        return (self.x <= other.x)

    def __gt__(self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return False
            else:
                return (self.y > other.y)
        return (self.x > other.x)

    def __ge__(self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return True
            else:
                return (self.y >= other.y)
        return (self.x >= other.x)


# Input: p, q, r are Point objects
# Output: compute the determinant and return the value
def det(p, q, r):
    return (p.x * q.y + q.x * r.y + r.x * p.y - p.y * q.x - q.y * r.x - r.y * p.x)#forward_sum - backward_sum


# Input: sorted_points is a sorted list of Point objects
# Output: computes the convex hull of a sorted list of Point objects
#         convex hull is a list of Point objects starting at the
#         extreme left point and going clockwise in order
#         returns the convex hull
def convex_hull(sorted_points):
    upper_hull = []
    upper_hull.append(sorted_points[0])
    upper_hull.append(sorted_points[1])


    # go from the third point on the list to the end to determine the upper hull
    for i in range(2, len(sorted_points)):
        upper_hull.append(sorted_points[i])

        # delete the middle of the last three points if the last three points do not make a right turn
        while len(upper_hull) >= 3 and det(upper_hull[-3], upper_hull[-2], upper_hull[-1]) > 0:
            upper_hull.pop(-2)


    lower_hull = []
    lower_hull.append(sorted_points[-1])
    lower_hull.append(sorted_points[-2])
    # go from the third last point on the list to the first to determine the lower hull
    for i in range(len(sorted_points) - 3, -1, -1):
        lower_hull.append(sorted_points[i])
        # if the last three points do not make a right turn, delete the middle of the last three points
        while len(lower_hull) >= 3 and det(lower_hull[-3], lower_hull[-2], lower_hull[-1]) > 0:
            lower_hull.pop(-2)


    # delete the first and last point to remove points that are already in the upper hull
    lower_hull.pop(0)
    lower_hull.pop(-1)

    return upper_hull + lower_hull


# Input: convex_poly is  a list of Point objects that define the
#        vertices of a convex polygon in order
# Output: computes and returns the area of a convex polygon
def area_poly(convex_poly):
    forward_sum = 0
    backward_sum = 0

    # calculates the sum of multiplied terms that are in diagonals starting from higher left term
    for i in range(len(convex_poly)):
        # multiply the last x coodinate to the first y coordinate and add to the forward_sum
        if i == len(convex_poly) - 1:
            forward_sum += convex_poly[i].x * convex_poly[0].y
        else:
            forward_sum += convex_poly[i].x * convex_poly[i + 1].y

    # caculates the sum of multiplied terms that are in diagonals starting from higher right term
    for i in range(len(convex_poly)):
        # multiply the last y coordinate to the first x coordinate and add to the backward_sum
        if i == len(convex_poly) - 1:
            backward_sum += convex_poly[i].y * convex_poly[0].x

        else:
            backward_sum += convex_poly[i].y * convex_poly[i + 1].x
            new_backward_sum = convex_poly[i].y * convex_poly[i + 1].x


    return .5 * abs(forward_sum - backward_sum)


# Input: no input
# Output: a string denoting all test cases have passed
def test_cases():
    return "all test cases passed"


def main():
    # create an empty list of Point objects
    points_list = []

    # read number of points
    line = sys.stdin.readline()
    line = line.strip()
    num_points = int(line)

    # read data from standard input
    for i in range(num_points):
        line = sys.stdin.readline()
        line = line.strip()
        line = line.split()
        x = int(line[0])
        y = int(line[1])
        points_list.append(Point(x, y))

    # sort the list according to x-coordinates
    sorted_points = sorted(points_list)

    '''
    # print the sorted list of Point objects
    for p in sorted_points:
      print (str(p))
    '''

    # get the convex hull
    convex = convex_hull(sorted_points)

    # run your test cases

    # print your results to standard output

    # print the convex hull
    print('Convex Hull')
    for i in range(len(convex)):
        print(str(convex[i]))

    # get the area of the convex hull
    area = area_poly(convex)

    # print the area of the convex hull
    print()
    print('Area of Convex Hull = {}'.format(area))


if __name__ == "__main__":
    main()
