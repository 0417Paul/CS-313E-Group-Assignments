#  File: Geometry.py

#  Description:

#  Student Name: Yilin Wen

#  Student UT EID: yw22559

#  Partner Name: Jiaxi Wang

#  Partner UT EID: JW53499

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: 02/02/2022

#  Date Last Modified: 02/07/2022

import math
import sys


class Point (object):
    # constructor with default values
    def __init__(self, x=0, y=0, z=0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
    
    # create a string representation of a Point
    # returns a string of the form (x, y, z)
    def __str__(self):
        return("({}, {}, {})".format(self.x, self.y, self.z))
    
    # returns the distance as a floating point number
    # we assume distance == 0. is equivalent to equality, tol = 1.0e-6
    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        dz = self.z - other.z
        return math.sqrt(dx ** 2 + dy ** 2 + dz ** 2) 

    # returns a Boolean
    # test for equality between two points
    def __eq__(self, other):
        return is_equal(self.distance(other), 0.0)


class Sphere (object):
    # constructor with default values
    def __init__(self, x=0, y=0, z=0, radius=1):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.radius = float(radius)
        self.r = float(radius)
        self.center = Point(self.x, self.y, self.z)
    
    # returns string representation of a Sphere of the form:
    # Center: (x, y, z), Radius: value
    def __str__(self):
        return "Center: ({}, {}, {}), Radius: {}".format(self.x, self.y, self.z, self.r)
    
    # compute surface area of Sphere
    # returns a floating point number
    def area(self):
        return 4.0 * math.pi * self.r * self.r

    # returns a floating point number
    def volume(self):
        return self.area() * self.r / 3.0
    
    # determines if a Point is strictly inside the Sphere
    # returns a Boolean
    def is_inside_point(self, p):
        # sphere can be passed to distance() since it has x,y,z
        return p.distance(self) < self.r
    
    # determine if another Sphere is strictly inside this Sphere
    # returns a Boolean
    def is_inside_sphere(self, other):
        o_center = Point(other.x, other.y, other.z)
        dist = o_center.distance(self)
        return dist < self.r - other.r
   
    # determine if a Cube is strictly inside this Sphere
    # determine if the eight corners of the Cube are strictly
    # inside the Sphere
    # returns a Boolean
    def is_inside_cube(self, a_cube):
        is_inside = True
        for c in a_cube.corners:
            Point_c = Point(c[0], c[1], c[2])
            c_is_inside = Point_c.distance(self) < self.r
            is_inside = is_inside and c_is_inside
        return is_inside
    
    # determine if a Cylinder is strictly inside this Sphere
    # returns a Boolean
    def is_inside_cyl(self, a_cyl):
        # if the upper and lower disk of cyl are inside the cut disk of sphere at same z, then cylinder inside
        # on a plane, disk can be passed to sphere methods (as a sphere whose great circle is the disk)
        cyl_high = a_cyl.z + a_cyl.h / 2.0
        cyl_low = a_cyl.z - a_cyl.h / 2.0
        if cyl_high >= self.z + self.r or cyl_low <= self.z - self.r:
            return False
        # the intersection of sphere and the plane z = cyl_high (is a circle but equivalent to a sphere)
        sp_upper = Sphere(self.x, self.y, cyl_high, math.sqrt(
            self.r ** 2 - (cyl_high - self.z) ** 2))
        sp_lower = Sphere(self.x, self.y, cyl_low, math.sqrt(
            self.r ** 2 - (cyl_low - self.z) ** 2))
        # the upper and lower face of cyl
        cyl_upper = Sphere(a_cyl.x, a_cyl.y, cyl_high, a_cyl.r)
        cyl_lower = Sphere(a_cyl.x, a_cyl.y, cyl_low, a_cyl.r)
        # check if they both inside
        return sp_upper.is_inside_sphere(cyl_upper) and sp_lower.is_inside_sphere(cyl_lower)

    # determine if another Sphere intersects this Sphere
    # two spheres intersect if they are not strictly inside
    # or not strictly outside each other
    # returns a Boolean
    def does_intersect_sphere(self, other):
        point_o = Point(self.x, self.y, self.z)
        return point_o.distance(other) <= self.r + other.r and not(self.is_inside_sphere(other) or other.is_inside_sphere(self))

    # determine if a Cube intersects this Sphere
    # the Cube and Sphere intersect if they are not
    # returns a Boolean
    def does_intersect_cube(self, a_cube):
        if self.is_inside_cube(a_cube):
            return False

        center = (self.x, self.y, self.z)
        min_dist = 0  # notice it's the squared dist
        for i in range(3):
            if center[i] < a_cube.corners[0][i]:
                min_dist += (center[i] - a_cube.corners[0][i]) ** 2
            elif center[i] > a_cube.corners[7][i]:
                min_dist += (center[i] - a_cube.corners[7][i]) ** 2
        # if the min dist is larger than radius, then they are outside.
        is_outside = min_dist > self.r ** 2
        # note this covers the cube inside sphere situation!
        return not is_outside

    # return the largest Cube object that is circumscribed
    # by this Sphere
    # all eight corners of the Cube are on the Sphere
    # returns a Cube object
    def circumscribe_cube(self):
        # there is one and only one (up to rotation) inscribed cube of a sphere.
        return Cube(self.x, self.y, self.z, 2 * self.r / math.sqrt(3.0))


class Cube (object):
    # Cube is defined by its center (which is a Point object)
    # and side. The faces of the Cube are parallel to x-y, y-z,
    # and x-z planes.
    def __init__(self, x=0, y=0, z=0, side=1):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.s = abs(float(side))
        self.side = abs(float(side))
        self.center = Point(self.x, self.y, self.z)
        # make a list with coordinates of 8 corners
        # the 8 corners are (x +- d, y +- d, z +- d)
        d = self.s / 2.0
        self.corners = (
            (self.x - d, self.y - d, self.z - d),
            (self.x - d, self.y - d, self.z + d),
            (self.x - d, self.y + d, self.z - d),
            (self.x - d, self.y + d, self.z + d),
            (self.x + d, self.y - d, self.z - d),
            (self.x + d, self.y - d, self.z + d),
            (self.x + d, self.y + d, self.z - d),
            (self.x + d, self.y + d, self.z + d)
        )

    # string representation of a Cube of the form:
    # Center: (x, y, z), Side: value
    def __str__(self):
        return "Center: ({}, {}, {}), Side: {}".format(self.x, self.y, self.z, self.s)
    
    # compute the total surface area of Cube (all 6 sides)
    # returns a floating point number
    def area(self):
        return 6.0 * self.s * self.s
   
    # compute volume of a Cube
    # returns a floating point number
    def volume(self):
        return self.s ** 3
    
    # determines if a Point is strictly inside this Cube
    # returns a Boolean
    def is_inside_point(self, p):
        p_co = (p.x, p.y, p.z)
        is_inside = True
        for i in range(3):
            is_inside = is_inside and p_co[i] > self.corners[0][i] and p_co[i] < self.corners[7][i]
        return is_inside

    # determine if a Sphere is strictly inside this Cube
    # returns a Boolean
    def is_inside_sphere(self, a_sphere):
        # if the minimum cube wrapping the sphere is inside the cube
        w_cube = Cube(a_sphere.x, a_sphere.y, a_sphere.z, a_sphere.r * 2.0)
        return self.is_inside_cube(w_cube)

    # determine if another Cube is strictly inside this Cube
    # returns a Boolean
    def is_inside_cube(self, other):
        # we only need to check 2 corners, the "max" and "min"
        p_min = Point(other.corners[0][0],
                      other.corners[0][1], other.corners[0][2])
        p_max = Point(other.corners[7][0],
                      other.corners[7][1], other.corners[7][2])
        return self.is_inside_point(p_min) and self.is_inside_point(p_max)

    # determine if a Cylinder is strictly inside this Cube
    # returns a Boolean
    def is_inside_cylinder(self, a_cyl):
        # only need to check if the 2 cubes "representing" the upper and lower surface of the cyl are in self. (the cube whose upper face is the square wrapping cyl upper face)
        # further more, only need to check 2 corners as the cube setting.
        cyl_min = Point(a_cyl.x - a_cyl.r, a_cyl.y -
                        a_cyl.r, a_cyl.z - a_cyl.h / 2.0)
        cyl_max = Point(a_cyl.x + a_cyl.r, a_cyl.y +
                        a_cyl.r, a_cyl.z + a_cyl.h / 2.0)
        return self.is_inside_point(cyl_min) and self.is_inside_point(cyl_max)
    
    # determine if another Cube intersects this Cube
    # two Cube objects intersect if they are not strictly
    # inside and not strictly outside each other
    # returns a Boolean
    def does_intersect_cube(self, other):
        # it's convinient to use the intersection_volume(), since if there's no intersection, the fucntion output 0.
        return not is_equal(self.intersection_volume(other), 0.0)

    # determine the volume of intersection if this Cube
    # intersects with another Cube
    # returns a floating point number
    # If there's no intersection, the fucntion output 0.
    def intersection_volume(self, other):
        # the approach very similary to Sphere class's does_intercect_cube():
        # starting from 1d, then 2d, then 3d.
        # 1d: 2 intervals. the intersection is between the smaller of the right end and the larger of the left end. If no intersection, we can have negative number. To solve this, we use max(dist, 0) to turn the negative to 0.
        # 2d: 2 squares. looking at the 2 1-d problem and take product.
        # 3d: 2 cubes. looking at the 3 1-d problem and take product.
        volume = 1.0
        for i in range(3):
            lenth_intc = max(0.0, min(
                self.corners[7][i], other.corners[7][i]) - max(self.corners[0][i], other.corners[0][i]))
            volume *= lenth_intc
        return volume

    # return the largest Sphere object that is inscribed
    # by this Cube
    # returns a Sphere object

    def inscribe_sphere(self):
        # there is one and only one inscribed sphere of the cube
        return Sphere(self.x, self.y, self.z, self.s / 2.0)


class Cylinder (object):
    # Cylinder is defined by its center (which is a Point object),
    # radius and height. The main axis of the Cylinder is along the
    # z-axis and height is measured along this axis
    def __init__(self, x=0, y=0, z=0, radius=1, height=1):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.r = float(radius)
        self.h = float(height)
    # returns a string representation of a Cylinder of the form:
    # Center: (x, y, z), Radius: value, Height: value

    def __str__(self):
        return "Center: ({}, {}, {}), Radius: {}, Height: {}".format(self.x, self.y, self.z, self.r, self.h)
    # compute surface area of Cylinder
    # returns a floating point number

    def area(self):
        return 2.0 * math.pi * self.r * (self.r + self.h)

    # compute volume of a Cylinder
    # returns a floating point number
    def volume(self):
        return math.pi * self.r * self.r * self.h

    # determine if a Point is strictly inside this Cylinder
    # returns a Boolean
    def is_inside_point(self, p):
        # project to xy plane:
        xy_inside = (p.x - self.x) ** 2 + (p.y - self.y) ** 2 < self.r ** 2
        z_inside = p.z < self.z + self.h / 2.0 and p.z > self.z - self.h / 2.0
        return xy_inside and z_inside

    # determine if a Sphere is strictly inside this Cylinder
    # returns a Boolean
    def is_inside_sphere(self, a_sphere):
        # projection to xy plane passing through the center of a_sphere
        cyl_sphere = Sphere(self.x, self.y, a_sphere.z, self.r)
        xy_inside = cyl_sphere.is_inside_sphere(a_sphere)
        z_inside = a_sphere.z + a_sphere.r < self.z + self.h / \
            2.0 and a_sphere.z - a_sphere.r > self.z - self.h / 2.0
        return xy_inside and z_inside

    # determine if a Cube is strictly inside this Cylinder
    # determine if all eight corners of the Cube are inside
    # the Cylinder
    # returns a Boolean
    def is_inside_cube(self, a_cube):
        is_inside = True
        for c in a_cube.corners:
            p = Point(c[0], c[1], c[2])
            is_inside = is_inside and self.is_inside_point(p)
        return is_inside

    # determine if another Cylinder is strictly inside this Cylinder
    # returns a Boolean
    def is_inside_cylinder(self, other):
        # check the projection to xy panel and check the projection to yz panel(for height)
        # Project to xy0 plane
        s_circle = Sphere(self.x, self.y, 0, self.r)
        o_circle = Sphere(other.x, other.y, 0, other.r)
        xy_inside = s_circle.is_inside_sphere(o_circle)
        # check the projection to xz for height inclusion
        z_inside = other.z + other.h / 2.0 < self.z + self.h / \
            2.0 and other.z - other.h / 2.0 > self.z - self.h / 2.0
        return xy_inside and z_inside

    # determine if another Cylinder intersects this Cylinder

    # returns a Boolean
    def does_intersect_cylinder(self, other):
        # first check if they are totally outside each other
        # very similar to is_inside_cylinder().
        # Project to xy0 plane
        xy_outside = math.sqrt((self.x - other.x) ** 2 +
                               (self.y - other.y) ** 2) > self.r + other.r
        # check the projection to xz for height not inclusion
        z_outside = other.z + other.h / 2.0 < self.z - self.h / \
            2.0 or other.z - other.h / 2.0 > self.z + self.h / 2.0
        is_outside = xy_outside or z_outside

        return not is_outside and not (self.is_inside_cylinder(other) or other.is_inside_cylinder(self))


# If distance < tol, say the two floats are equal.
def is_equal(x, y):
    tol = 1.0e-6
    return abs(x - y) < tol


def main():
    # read data from standard input
    input_data = sys.stdin.readlines()
    # read the coordinates of the first Point p
    p_data = input_data[0].split(" ")
    # create a Point object
    Point_p = Point(p_data[0], p_data[1], p_data[2])
    # read the coordinates of the second Point q
    q_data = input_data[1].split(" ")
    # create a Point object
    Point_q = Point(q_data[0], q_data[1], q_data[2])
    # read the coordinates of the center and radius of sphereA
    sA_data = input_data[2].split(" ")
    # create a Sphere object
    Sphere_A = Sphere(sA_data[0], sA_data[1], sA_data[2], sA_data[3])
    # read the coordinates of the center and radius of sphereB
    sB_data = input_data[3].split(" ")
    # create a Sphere object
    Sphere_B = Sphere(sB_data[0], sB_data[1], sB_data[2], sB_data[3])
    # read the coordinates of the center and side of cubeA
    cA_data = input_data[4].split(" ")
    # create a Cube object
    Cube_A = Cube(cA_data[0], cA_data[1], cA_data[2], cA_data[3])
    # read the coordinates of the center and side of cubeB
    cB_data = input_data[5].split(" ")
    # create a Cube object
    Cube_B = Cube(cB_data[0], cB_data[1], cB_data[2], cB_data[3])
    # read the coordinates of the center, radius and height of cylA
    cylA_data = input_data[6].split(" ")
    # create a Cylinder object
    Cyl_A = Cylinder(cylA_data[0], cylA_data[1],
                     cylA_data[2], cylA_data[3], cylA_data[4])
    # read the coordinates of the center, radius and height of cylB
    cylB_data = input_data[7].split(" ")
    # create a Cylinder object
    Cyl_B = Cylinder(cylB_data[0], cylB_data[1],
                     cylB_data[2], cylB_data[3], cylB_data[4])

    # print if the distance of p from the origin is greater
    # than the distance of q from the origin
    origin = Point(0, 0, 0)
    is_p_ge_q = "is" if (Point_p.distance(origin) >
                         Point_q.distance(origin)) else "is not"
    print("Distance of Point p from the origin {} greater than the distance of Point q from the origin".format(is_p_ge_q))
    # print if Point p is inside sphereA
    # note that the Sphere can be an argument of distance()
    is_p_in_sA = "is" if Sphere_A.is_inside_point(Point_p) else "is not"
    print("Point p {} inside sphereA".format(is_p_in_sA))
    # print if sphereB is inside sphereA
    is_sB_in_sA = "is" if Sphere_A.is_inside_sphere(Sphere_B) else "is not"
    print("sphereB {} inside sphereA".format(is_sB_in_sA))
    # print if cubeA is inside sphereA
    is_cA_inside_sA = "is" if Sphere_A.is_inside_cube(Cube_A) else "is not"
    print("cubeA {} inside sphereA".format(is_cA_inside_sA))
    # print if cylA is inside sphereA
    is_cylA_inside_sA = "is" if Sphere_A.is_inside_cyl(Cyl_A) else "is not"
    print("cylA {} inside sphereA".format(is_cylA_inside_sA))
    # print if sphereA intersects with sphereB
    is_sA_int_sB = "does" if Sphere_A.does_intersect_sphere(
        Sphere_B) else "does not"
    print("sphereA {} intersect sphereB".format(is_sA_int_sB))
    # print if cubeB intersects with sphereB
    is_cB_int_sB = "does" if Sphere_B.does_intersect_cube(
        Cube_B) else "does not"
    print("cubeB {} intersect sphereB".format(is_cB_int_sB))
    # print if the volume of the largest Cube that is circumscribed
    # by sphereA is greater than the volume of cylA
    is_something = Sphere_A.circumscribe_cube().volume() > Cyl_A.volume()
    is_some_str = "is" if is_something else "is not"
    print("Volume of the largest Cube that is circumscribed by sphereA {} greater than the volume of cylA".format(is_some_str))

    # print if Point p is inside cubeA
    is_cube_thing = "is" if Cube_A.is_inside_point(Point_p) else "is not"
    print("Point p {} inside cubeA".format(is_cube_thing))
    # print if sphereA is inside cubeA
    is_cube_thing = "is" if Cube_A.is_inside_sphere(Sphere_A) else "is not"
    print("sphereA {} inside cubeA".format(is_cube_thing))
    # print if cubeB is inside cubeA
    is_cube_thing = "is" if Cube_A.is_inside_cube(Cube_B) else "is not"
    print("cubeB {} inside cubeA".format(is_cube_thing))
    # print if cylA is inside cubeA
    is_cube_thing = "is" if Cube_A.is_inside_cylinder(Cyl_A) else "is not"
    print("cylA {} inside cubeA".format(is_cube_thing))
    # print if cubeA intersects with cubeB
    is_cube_thing = "does" if Cube_B.does_intersect_cube(
        Cube_A) else "does not"
    print("cubeA {} intersect cubeB".format(is_cube_thing))
    # print if the intersection volume of cubeA and cubeB
    # is greater than the volume of sphereA
    is_cube_thing = "is" if Cube_A.intersection_volume(
        Cube_B) > Sphere_A.volume() else "is not"
    print("Intersection volume of cubeA and cubeB {} greater than the volume of sphereA".format(
        is_cube_thing))
    # print if the surface area of the largest Sphere object inscribed
    # by cubeA is greater than the surface area of cylA
    is_cube_thing = "is" if Cube_A.inscribe_sphere().area() > Cyl_A.area() else "is not"
    print("Surface area of the largest Sphere object inscribed by cubeA {} greater than the surface area of cylA".format(is_cube_thing))

    # print if Point p is inside cylA
    is_cyl_thing = "is" if Cyl_A.is_inside_point(Point_p) else "is not"
    print("Point p {} inside cylA".format(is_cyl_thing))
    # print if sphereA is inside cylA
    is_cyl_thing = "is" if Cyl_A.is_inside_sphere(Sphere_A) else "is not"
    print("sphereA {} inside cylA".format(is_cyl_thing))
    # print if cubeA is inside cylA
    is_cyl_thing = "is" if Cyl_A.is_inside_cube(Cube_A) else "is not"
    print("cubeA {} inside cylA".format(is_cyl_thing))
    # print if cylB is inside cylA
    is_cyl_thing = "is" if Cyl_A.is_inside_cylinder(Cyl_B) else "is not"
    print("cylB {} inside cylA".format(is_cyl_thing))
    # print if cylB intersects with cylA
    is_cyl_thing = "does" if Cyl_A.does_intersect_cylinder(
        Cyl_B) else "does not"
    print("cylB {} intersect cylA".format(is_cyl_thing))


if __name__ == "__main__":
    main()
