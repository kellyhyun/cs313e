#  File: Geometry.py

#  Description: comparing different shapes to each other using classses in python

#  Student Name: Soomin Hyun

#  Student UT EID: sh52679

#  Partner Name: Joon Kim (Unique Number: 52595)

#  Partner UT EID: jk45873

#  Course Name: CS 313E

#  Unique Number: 52600

#  Date Created: 9/13/21

#  Date Last Modified:9/16/21

import math
import sys


class Point (object):
 # constructor with default values
 def __init__(self, x=0, y=0, z=0):
   self.x = x/1
   self.y = y/1
   self.z = z/1

 # create a string representation of a Point
 # returns a string of the form (x, y, z)
 def __str__(self):
   return '({}, {}, {})'.format(self.x, self.y, self.z)

 # get distance to another Point object
 # other is a Point object
 # returns the distance as a floating point number
 def distance(self, other):
   new_distance = math.sqrt((self.x - other.x)**2+(self.y - other.y)**2+(self.z - other.z)**2)
   return new_distance

 # test for equality between two points
 # other is a Point object
 # returns a Boolean
 def __eq__(self, other):
   tol = 1.0e-6
   return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol) and(abs(self.z - other.z) < tol))



class Sphere(object):
 # constructor with default values
 def __init__(self, x=0, y=0, z=0, radius=1):
   self.x = x/1
   self.y = y/1
   self.z = z/1
   self.radius = radius/1
   self.center = Point(x=self.x, y=self.y, z=self.z)

 # returns string representation of a Sphere of the form:
 # Center: (x, y, z), Radius: value
 def __str__(self):
   return 'Center: ({}, {}, {}), Radius: {}'.format(self.x, self.y, self.z, self.radius)

 # compute surface area of Sphere
 # returns a floating point number
 def area(self):
   return float(4*self.radius**2*math.pi)

 # compute volume of a Sphere
 # returns a floating point number
 def volume(self):
   return float(4/3*math.pi*self.radius**3)

 # determines if a Point is strictly inside the Sphere
 # p is Point object
 # returns a Boolean
 def is_inside_point(self, p):
   center = Point(x=self.x, y=self.y, z=self.z)
   check_distance = Point.distance(p, center)
   return check_distance < self.radius


 # determine if another Sphere is strictly inside this Sphere
 # other is a Sphere object
 # returns a Boolean
 def is_inside_sphere(self, other):
   boolean = False
   center_self = Point(x=self.x, y=self.y, z=self.z)
   center_other = Point(x=other.x, y=other.y, z=self.z)
   check_distance = Point.distance(center_self, center_other)
   if check_distance < self.radius:
     check_other_radius = other.radius + check_distance
     if check_other_radius < self.radius:
       boolean = True
   return boolean


 # determine if a Cube is strictly inside this Sphere
 # determine if the eight corners of the Cube are strictly
 # inside the Sphere
 # a_cube is a Cube object
 # returns a Boolean
 def is_inside_cube(self, a_cube):
   boolean = False
   center_self = Point(x=self.x, y=self.y, z=self.z)
   center_cube = Point(x=a_cube.x, y=a_cube.y, z=a_cube.z)
   check_distance = Point.distance(center_self, center_cube)
   new_coordinates = []

   if check_distance < self.radius:
     boolean = True
     each_coordinate = [0.0, 0.0, 0.0]
     for x in [-a_cube.side/2, a_cube.side/2]:
       for y in [-a_cube.side/2, a_cube.side/2]:
         for z in [-a_cube.side/2, a_cube.side/2]:
           each_coordinate = [a_cube.x + x, a_cube.y + y, a_cube.z + z]
           new_coordinates.append(each_coordinate)
     for i in range(len(new_coordinates)):
       new_point = Point(x = new_coordinates[i][0], y = new_coordinates[i][1], z = new_coordinates[i][2])
       check_distance_again = Point.distance(center_self, new_point)
       if check_distance_again > self.radius:
         boolean = False
   return boolean

 # determine if a Cylinder is strictly inside this Sphere
 # a_cyl is a Cylinder object
 # returns a Boolean
 def is_inside_cyl(self, a_cyl):
   boolean = False
   center_self = Point(x=self.x, y=self.y, z=self.z)
   center_cyl = Point(x=a_cyl.x, y=a_cyl.y, z=a_cyl.z)
   diff_centers = [abs(a_cyl.x - self.x), abs(a_cyl.y - self.y), abs(a_cyl.z - self.z)]

   return math.sqrt((math.sqrt(diff_centers[0]**2 + diff_centers[1]**2) + a_cyl.radius)**2 + (abs(diff_centers[2]) + a_cyl.height/2)**2) < self.radius


 # determine if another Sphere intersects this Sphere
 # other is a Sphere object
 # two spheres intersect if they are not strictly inside
 # or not strictly outside each other
 # returns a Boolean
 def does_intersect_sphere(self, other):
   boolean = False
   center_self = Point(x=self.x, y=self.y, z=self.z)
   center_other = Point(x=other.x, y=other.y, z=other.z)
   check_distance = Point.distance(center_self, center_other)
   if check_distance < self.radius:
     check_other_radius = other.radius + check_distance
     if check_other_radius > self.radius:
       boolean = True

   if Sphere.is_inside_point(self, center_other) == False and check_distance < (self.radius + other.radius):
     boolean = True

   return boolean

 # determine if a Cube intersects this Sphere
 # the Cube and Sphere intersect if they are not
 # strictly inside or not strictly outside the other
 # a_cube is a Cube object
 # returns a Boolean
 def does_intersect_cube(self, a_cube):
     center_point = Point(self.x, self.y, self.z)
     cube_point = Point(a_cube.x, a_cube.y, a_cube.z)
     if Sphere.is_inside_cube(self, a_cube) == False:
         if (Point.distance(center_point, cube_point) > self.radius + math.sqrt(3) * a_cube.side / 2) == False:
             return True

     return False

 # return the largest Cube object that is circumscribed
 # by this Sphere
 # all eight corners of the Cube are on the Sphere
 # returns a Cube object
 def circumscribe_cube(self):
   max_side = 2*self.radius/math.sqrt(3)
   return Cube(x=self.x, y=self.y, z=self.z, side=max_side)

class Cube (object):
 # Cube is defined by its center (which is a Point object)
 # and side. The faces of the Cube are parallel to x-y, y-z,
 # and x-z planes.
 def __init__ (self, x = 0, y = 0, z = 0, side = 1):
   self.x = x/1
   self.y = y/1
   self.z = z/1
   self.side = side/1
   self.center = Point(x=self.x, y=self.y, z=self.z)

 # string representation of a Cube of the form:
 # Center: (x, y, z), Side: value
 def __str__ (self):
   return 'Center: ({}, {}, {}), Side: {}'.format(self.x, self.y, self.z, self.side)

 # compute the total surface area of Cube (all 6 sides)
 # returns a floating point number
 def area (self):
   return(float(6*self.side**2))

 # compute volume of a Cube
 # returns a floating point number
 def volume (self):
   return(float(self.side**3))

 # determines if a Point is strictly inside this Cube
 # p is a point object
 # returns a Boolean
 def is_inside_point (self, p):
   x_min = self.x - self.side/2
   x_max = self.x + self.side/2
   y_min = self.y - self.side/2
   y_max = self.y + self.side/2
   z_min = self.z - self.side/2
   z_max = self.z + self.side/2
   return((x_min <p.x< x_max) and (y_min < p.y < y_max) and (z_min < p.z < z_max))

 # determine if a Sphere is strictly inside this Cube
 # a_sphere is a Sphere object
 # returns a Boolean
 def is_inside_sphere (self, a_sphere):
   boolean = False
   center_self = Point(x=self.x, y=self.y, z=self.z)
   center_sphere = Point(x=a_sphere.x, y=a_sphere.y, z=a_sphere.z)
   each_coord = [0.0, 0.0, 0.0]
   all_coord = []
   if Cube.is_inside_point(self, center_sphere):
     boolean = True
     for x in [-a_sphere.radius, a_sphere.radius]:
       for y in [-a_sphere.radius, a_sphere.radius]:
         for z in [-a_sphere.radius, a_sphere.radius]:
           each_coord = [center_sphere.x + x, center_sphere.y + y, center_sphere.z + z]
           all_coord.append(each_coord)
     for i in range(len(all_coord)):
       new_point = Point(x = all_coord[i][0], y = all_coord[i][1], z = all_coord[i][2])
       if Cube.is_inside_point(self, new_point) == False:
         boolean = False

   return boolean

 # determine if another Cube is strictly inside this Cube
 # other is a Cube object
 # returns a Boolean
 def is_inside_cube (self, other):
   boolean = False
   center_self = Point(x=self.x, y=self.y, z=self.z)
   center_other = Point(x=other.x, y=other.y, z=other.z)
   each_coord = [0.0, 0.0, 0.0]
   all_coord = []
   if Cube.is_inside_point(self, center_other):
     boolean = True
     for x in [-other.side/2, other.side/2]:
       for y in [-other.side/2, other.side/2]:
         for z in [-other.side/2, other.side/2]:
           each_coord = [center_other.x + x, center_other.y + y, center_other.z + z]
           all_coord.append(each_coord)
     for i in range(len(all_coord)):
       new_point = Point(x=all_coord[i][0], y=all_coord[i][1], z=all_coord[i][2])
       if Cube.is_inside_point(self, new_point) == False:
         boolean = False
   return boolean

 # determine if a Cylinder is strictly inside this Cube
 # a_cyl is a Cylinder object
 # returns a Boolean
 def is_inside_cylinder (self, a_cyl):
   boolean = False
   center_self = Point(x=self.x, y=self.y, z=self.z)
   center_cyl = Point(x=a_cyl.x, y=a_cyl.y, z=a_cyl.z)
   each_coord = [0.0, 0.0, 0.0]
   all_coord = []
   if Cube.is_inside_point(self, center_cyl):
     boolean = True
     for x in [-a_cyl.radius, a_cyl.radius]:
       for y in [-a_cyl.radius, a_cyl.radius]:
         for z in [-a_cyl.height/2, a_cyl.height/2]:
           each_coord = [center_cyl.x + x, center_cyl.y + y, center_cyl.z + z]
           all_coord.append(each_coord)
     for i in range(len(all_coord)):
       new_point = Point(x=all_coord[i][0], y=all_coord[i][1], z=all_coord[i][2])
       if Cube.is_inside_point(self, new_point) == False:
         boolean = False
   return boolean

 # determine if another Cube intersects this Cube
 # two Cube objects intersect if they are not strictly
 # inside and not strictly outside each other
 # other is a Cube object
 # returns a Boolean
 def does_intersect_cube (self, other):
   boolean = False
   center_self = Point(x=self.x, y=self.y, z=self.z)
   center_other = Point(x=other.x, y=other.y, z=other.z)
   each_coord = [0.0, 0.0, 0.0]
   all_coord = []
   if Cube.is_inside_point(self, center_other):
     boolean = True
     for x in [-other.side / 2, other.side / 2]:
       for y in [-other.side / 2, other.side / 2]:
         for z in [-other.side / 2, other.side / 2]:
           each_coord = [center_other.x + x, center_other.y + y, center_other.z + z]
           all_coord.append(each_coord)
     for i in range(len(all_coord)):
       new_point = Point(x=all_coord[i][0], y=all_coord[i][1], z=all_coord[i][2])
       if Cube.is_inside_point(self, new_point) == False:
         boolean = True
   return boolean

 # determine the volume of intersection if this Cube
 # intersects with another Cube
 # other is a Cube object
 # returns a floating point number
 def intersection_volume (self, other):
   volume = 0
   if Cube.does_intersect_cube(self, other):
     self_coord = []
     other_coord = []

     intersect_coord = []

     center_self = Point(x=self.x, y=self.y, z=self.z)
     center_other = Point(x=other.x, y=other.y, z=other.z)
     each_coord = [0.0, 0.0, 0.0]

     x_coords = []
     y_coords = []
     z_coords = []

     x_coords.append(self.x - self.side/2)
     x_coords.append(self.x + self.side/2)
     y_coords.append(self.y - self.side/2)
     y_coords.append(self.y + self.side/2)
     z_coords.append(self.z - self.side/2)
     z_coords.append(self.z + self.side/2)

     x_coords.append(other.x - other.side/2)
     x_coords.append(other.x + other.side/2)
     y_coords.append(other.y - other.side/2)
     y_coords.append(other.y + other.side/2)
     z_coords.append(other.z - other.side/2)
     z_coords.append(other.z + other.side/2)

     max_coords = []
     min_coords = []

     for coord in [x_coords, y_coords, z_coords]:
       for value in coord:
         if value == x_coords[0]:
           max_value = value
           min_value = value

         if value > max_value:
           max_value = value

         if value < min_value:
           min_value = value

       max_coords.append(max_value)
       min_coords.append(min_value)
     for i in range(3):
       volume *= (self.side + other.side - (max_coords[i] - min_coords[i]))




   return volume


 # return the largest Sphere object that is inscribed
 # by this Cube
 # Sphere object is inside the Cube and the faces of the
 # Cube are tangential planes of the Sphere
 # returns a Sphere object
 def inscribe_sphere (self):
     new_radius = self.side/2
     inscribed_sphere = Sphere(x=self.x, y=self.y, z=self.z, radius=new_radius)
     return inscribed_sphere




class Cylinder (object):
 # Cylinder is defined by its center (which is a Point object),
 # radius and height. The main axis of the Cylinder is along the
 # z-axis and height is measured along this axis
 def __init__ (self, x = 0, y = 0, z = 0, radius = 1, height = 1):
   self.x = x/1
   self.y = y/1
   self.z = z/1
   self.radius = radius/1
   self.height = height/1
   self.center = Point(x=self.x, y=self.y, z=self.z)

 # returns a string representation of a Cylinder of the form:
 # Center: (x, y, z), Radius: value, Height: value
 def __str__ (self):
   return 'Center: ({}, {}, {}), Radius: {}, Height: {}'.format(self.x, self.y, self.z, self.radius, self.height)

 # compute surface area of Cylinder
 # returns a floating point number
 def area (self):
   return(float((math.pi*2*self.radius*self.height) + (2*math.pi*self.radius**2)))

 # compute volume of a Cylinder
 # returns a floating point number
 def volume (self):
   return(float(math.pi*self.radius**2*self.height))

 # determine if a Point is strictly inside this Cylinder
 # p is a Point object
 # returns a Boolean
 def is_inside_point (self, p):
   return (self.z - self.height/2 < p.z < self.z + self.height/2) and math.sqrt((p.x - self.x)**2 + (p.y - self.y)**2) < self.radius

 # determine if a Sphere is strictly inside this Cylinder
 # a_sphere is a Sphere object
 # returns a Boolean
 def is_inside_sphere (self, a_sphere):
   boolean = False
   center_self = Point(x=self.x, y=self.y, z=self.z)
   center_sphere = Point(x=a_sphere.x, y=a_sphere.y, z=a_sphere.z)
   each_coord = [0.0, 0.0, 0.0]
   all_coord = []
   if Cylinder.is_inside_point(self, center_sphere):
     boolean = True
     for x in [-a_sphere.radius, a_sphere.radius]:
       for y in [-a_sphere.radius, a_sphere.radius]:
         for z in [-a_sphere.radius, a_sphere.radius]:
           each_coord = [a_sphere.radius + x, a_sphere.radius + y, a_sphere.radius + z]
           all_coord.append(each_coord)
     for i in range(len(all_coord)):
       new_point = Point(x=all_coord[i][0], y=all_coord[i][1], z=all_coord[i][2])
       if Cylinder.is_inside_point(self, new_point) == False:
         boolean = False
   return boolean


  # determine if a Cube is strictly inside this Cylinder
  # determine if all eight corners of the Cube are inside
  # the Cylinder
  # a_cube is a Cube object
  # returns a Boolean
 def is_inside_cube (self, a_cube):
   boolean = False
   center_self = Point(x=self.x, y=self.y, z=self.z)
   center_other = Point(x=a_cube.x, y=a_cube.y, z=a_cube.z)
   each_coord = [0.0, 0.0, 0.0]
   all_coord = []

   if Cylinder.is_inside_point(self, center_other):
     boolean = True
     for x in [-a_cube.side/2, a_cube.side/2]:
       for y in [-a_cube.side/2, a_cube.side/2]:
         for z in [-a_cube.side/2, a_cube.side/2]:
           each_coord = [center_other.x + x, center_other.y + y, center_other.z + z]
           all_coord.append(each_coord)



     for i in range(len(all_coord)):
       new_point = Point(x=all_coord[i][0], y=all_coord[i][1], z=all_coord[i][2])

       if Cylinder.is_inside_point(self, new_point) == False:
         boolean = False

   return boolean


 # determine if another Cylinder is strictly inside this Cylinder
 # other is Cylinder object
 # returns a Boolean
 def is_inside_cylinder (self, other):
     boolean = False
     center_other = Point(x=other.x, y=other.y, z=other.z)


     if Cylinder.is_inside_point(self, center_other):
         if self.z - self.height/2 < other.z - other.height/2 < self.z + self.height/2:
             if self.z - self.height/2 < other.z + other.height/2 < self.z + self.height/2:
                if (math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2) + other.radius) < self.radius:
                    boolean = True

     return boolean




 # determine if another Cylinder intersects this Cylinder
 # two Cylinder object intersect if they are not strictly
 # inside and not strictly outside each other
 # other is a Cylinder object
 # returns a Boolean
 def does_intersect_cylinder (self, other):
     if Cylinder.is_inside_cylinder(self, other) == False:
         if (math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2) > self.radius + other.radius or abs(other.z - self.z) > self.height/2 + other.height/2) == False:
             return True

     return False



def main():
 # read data from standard input
 p_coords = sys.stdin.readline()
 p_coords = p_coords.strip(" \n")
 q_coords = sys.stdin.readline()
 q_coords = q_coords.strip(" \n")
 sphere_a = sys.stdin.readline()
 sphere_a = sphere_a.strip(" \n")
 sphere_b = sys.stdin.readline()
 sphere_b = sphere_b.strip(" \n")
 cube_a = sys.stdin.readline()
 cube_a = cube_a.strip(" \n")
 cube_b = sys.stdin.readline()
 cube_b = cube_b.strip(" \n")
 cyl_a = sys.stdin.readline()
 cyl_a = cyl_a.strip(" \n")
 cyl_b = sys.stdin.readline()
 cyl_b = cyl_b.strip(" \n")

 # read the coordinates of the first Point p
 p_coords = p_coords.split()
 p_coord_x = float(p_coords[0])
 p_coord_y = float(p_coords[1])
 p_coord_z = float(p_coords[2])

 # create a Point object
 obj_point_p = Point(x=p_coord_x, y=p_coord_y, z=p_coord_z)
 # read the coordinates of the second Point q
 q_coords = q_coords.split()
 q_coord_x = float(q_coords[0])
 q_coord_y = float(q_coords[1])
 q_coord_z = float(q_coords[2])

 # create a Point object
 obj_point_q = Point(x=q_coord_x, y=q_coord_y, z=q_coord_z)

 # read the coordinates of the center and radius of sphereA
 sphere_a = sphere_a.split()
 sphere_a_x = float(sphere_a[0])
 sphere_a_y = float(sphere_a[1])
 sphere_a_z = float(sphere_a[2])
 sphere_a_r = float(sphere_a[3])

 # create a Sphere object
 obj_sphere_a = Sphere(x=sphere_a_x, y=sphere_a_y, z=sphere_a_z, radius=sphere_a_r)

 # read the coordinates of the center and radius of sphereB
 sphere_b = sphere_b.split()
 sphere_b_x = float(sphere_b[0])
 sphere_b_y = float(sphere_b[1])
 sphere_b_z = float(sphere_b[2])
 sphere_b_r = float(sphere_b[3])

 # create a Sphere object
 obj_sphere_b = Sphere(x=sphere_b_x, y=sphere_b_y, z=sphere_b_z, radius=sphere_b_r)

 # read the coordinates of the center and side of cubeA
 cube_a = cube_a.split()

 cube_a_x = float(cube_a[0])
 cube_a_y = float(cube_a[1])
 cube_a_z = float(cube_a[2])
 cube_a_s = float(cube_a[3])
 # create a Cube object
 obj_cube_a = Cube(x=cube_a_x, y=cube_a_y, z=cube_a_z, side=cube_a_s)

 # read the coordinates of the center and side of cubeB
 cube_b = cube_b.split()
 cube_b_x = float(cube_b[0])
 cube_b_y = float(cube_b[1])
 cube_b_z = float(cube_b[2])
 cube_b_s = float(cube_b[3])

 # create a Cube object
 obj_cube_b = Cube(x=cube_b_x, y=cube_b_y, z=cube_b_z, side=cube_b_s)

 # read the coordinates of the center, radius and height of cylA
 cyl_a = cyl_a.split()
 cyl_a_x = float(cyl_a[0])
 cyl_a_y = float(cyl_a[1])
 cyl_a_z = float(cyl_a[2])
 cyl_a_r = float(cyl_a[3])
 cyl_a_h = float(cyl_a[4])

 # create a Cylinder object
 obj_cyl_a = Cylinder(x=cyl_a_x, y=cyl_a_y, z=cyl_a_z, radius=cyl_a_r, height=cyl_a_h)

 # read the coordinates of the center, radius and height of cylB
 cyl_b = cyl_b.split()
 cyl_b_x = float(cyl_b[0])
 cyl_b_y = float(cyl_b[1])
 cyl_b_z = float(cyl_b[2])
 cyl_b_r = float(cyl_b[3])
 cyl_b_h = float(cyl_b[4])

 # create a Cylinder object
 obj_cyl_b = Cylinder(x=cyl_b_x, y=cyl_b_y, z=cyl_b_z, radius=cyl_b_r, height=cyl_b_h)

 # print if the distance of p from the origin is greater
 # than the distance of q from the origin
 origin = Point(x=0,y=0,z=0)
 distance_p_origin = Point.distance(obj_point_p, origin)
 distance_q_origin = Point.distance(obj_point_q, origin)
 decide = 'is'
 if distance_p_origin > distance_q_origin:
   decide = 'is'
 else:
   decide = 'is not'
 print('Distance of Point p from the origin {} greater than the distance of Point q from the origin'.format(decide))

 # print if Point p is inside sphereA
 decide_boolean = Sphere.is_inside_point(obj_sphere_a, obj_point_p)
 if decide_boolean == True:
   decide = 'is'
 elif decide_boolean == False:
   decide = 'is not'
 print('Point p {} inside sphereA'.format(decide))

 # print if sphereB is inside sphereA
 decide_boolean = Sphere.is_inside_sphere(obj_sphere_a, obj_sphere_b)
 if decide_boolean == True:
   decide = 'is'
 elif decide_boolean == False:
   decide = 'is not'
 print('sphereB {} inside sphereA'.format(decide))

 # print if cubeA is inside sphereA
 decide_boolean = Sphere.is_inside_cube(obj_sphere_a, obj_cube_a)
 if decide_boolean == True:
   decide = 'is'
 elif decide_boolean == False:
   decide = 'is not'
 print('cubeA {} inside sphereA'.format(decide))

 # print if cylA is inside sphereA
 decide_boolean = Sphere.is_inside_cyl(obj_sphere_a, obj_cyl_a)
 if decide_boolean == True:
   decide = 'is'
 elif decide_boolean == False:
   decide = 'is not'
 print('cylA {} inside sphereA'.format(decide))

 # print if sphereA intersects with sphereB
 decide_boolean = Sphere.does_intersect_sphere(obj_sphere_a, obj_sphere_b)
 if decide_boolean == True:
   decide = 'does'
 elif decide_boolean == False:
   decide = 'does not'
 print('sphereA {} intersect sphereB'.format(decide))

 # print if cubeB intersects with sphereB
 decide_boolean = Sphere.does_intersect_cube(obj_sphere_b, obj_cube_b)
 if decide_boolean == True:
   decide = 'does'
 elif decide_boolean == False:
   decide = 'does not'
 print('cubeB {} intersect sphereB'.format(decide))

 # print if the volume of the largest Cube that is circumscribed
 # by sphereA is greater than the volume of cylA
 circumscribed_cube = Sphere.circumscribe_cube(obj_sphere_a)
 vol_circumscribed_cube = Cube.volume(circumscribed_cube)
 vol_cylA = Cylinder.volume(obj_cyl_a)
 decide_boolean = (vol_circumscribed_cube > vol_cylA)
 if decide_boolean == True:
   decide = 'is'
 elif decide_boolean == False:
   decide = 'is not'
 print('Volume of the largest Cube that is circumscribed by sphereA {} greater than the volume of cylA'.format(decide))

 # print if Point p is inside cubeA
 decide_boolean = Cube.is_inside_point(obj_cube_a, obj_point_p)
 if decide_boolean == True:
   decide = 'is'
 elif decide_boolean == False:
   decide = 'is not'
 print('Point p {} inside cubeA'.format(decide))

 # print if sphereA is inside cubeA
 decide_boolean = Cube.is_inside_sphere(obj_cube_a, obj_sphere_a)
 if decide_boolean == True:
   decide = 'is'
 elif decide_boolean == False:
   decide = 'is not'
 print('sphereA {} inside cubeA'.format(decide))

 # print if cubeB is inside cubeA
 decide_boolean = Cube.is_inside_cube(obj_cube_a, obj_cube_b)
 if decide_boolean == True:
   decide = 'is'
 elif decide_boolean == False:
   decide = 'is not'
 print('cubeB {} inside cubeA'.format(decide))

 # print if cylA is inside cubeA
 decide_boolean = Cube.is_inside_cylinder(obj_cube_a, obj_cyl_a)
 if decide_boolean == True:
   decide = 'is'
 elif decide_boolean == False:
   decide = 'is not'
 print('cylA {} inside cubeA'.format(decide))

 # print if cubeA intersects with cubeB
 decide_boolean = Cube.does_intersect_cube(obj_cube_a, obj_cube_b)
 if decide_boolean == True:
   decide = 'does'
 elif decide_boolean == False:
   decide = 'does not'
 print('cubeA {} intersect cubeB'.format(decide))

 # print if the intersection volume of cubeA and cubeB
 # is greater than the volume of sphereA
 intersection_cube = Cube.intersection_volume(obj_cube_a, obj_cube_b)
 vol_sphereA = Sphere.volume(obj_sphere_a)
 decide_boolean = intersection_cube > vol_sphereA
 if decide_boolean == True:
   decide = 'is'
 elif decide_boolean == False:
   decide = 'is not'
 print('Intersection volume of cubeA and cubeB {} greater than the volume of sphereA'.format(decide))

 # print if the surface area of the largest Sphere object inscribed
 # by cubeA is greater than the surface area of cylA
 circumscribed_sphere = Cube.inscribe_sphere(obj_cube_a)
 sa_of_circumscribed = Sphere.area(circumscribed_sphere)
 sa_of_cylA = Cylinder.area(obj_cyl_a)
 decide_boolean = sa_of_circumscribed > sa_of_cylA
 if decide_boolean == True:
   decide = 'is'
 elif decide_boolean == False:
   decide = 'is not'
 print('Surface area of the largest Sphere object inscribed by cubeA {} greater than the surface area of cylA'.format(decide))

 # print if Point p is inside cylA
 decide_boolean = Cylinder.is_inside_point(obj_cyl_a, obj_point_p)
 if decide_boolean == True:
   decide = 'is'
 elif decide_boolean == False:
   decide = 'is not'
 print('Point p {} inside cylA'.format(decide))

 # print if sphereA is inside cylA
 decide_boolean = Cylinder.is_inside_sphere(obj_cyl_a, obj_sphere_a)
 if decide_boolean == True:
   decide = 'is'
 elif decide_boolean == False:
   decide = 'is not'
 print('sphereA {} inside cylA'.format(decide))

 # print if cubeA is inside cylA
 decide_boolean = Cylinder.is_inside_cube(obj_cyl_a, obj_cube_a)
 if decide_boolean == True:
   decide = 'is'
 elif decide_boolean == False:
   decide = 'is not'
 print('cubeA {} inside cylA'.format(decide))

 # print if cylB is inside cylA
 decide_boolean = Cylinder.is_inside_cylinder(obj_cyl_a, obj_cyl_b)
 if decide_boolean == True:
   decide = 'is'
 elif decide_boolean == False:
   decide = 'is not'
 print('cylB {} inside cylA'.format(decide))

 # print if cylB intersects with cylA
 decide_boolean = Cylinder.does_intersect_cylinder(obj_cyl_a, obj_cyl_b)
 if decide_boolean == True:
   decide = 'does'
 elif decide_boolean == False:
   decide = 'does not'
 print('cylB {} intersect cylA'.format(decide))
 print()

if __name__ == "__main__":
 main()
