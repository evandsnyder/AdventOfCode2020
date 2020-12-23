#!/usr/local/bin/python3
# import numpy as numpy
# from matplotlib import pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
import constraint as constraint

class Point3D():
    def __init__(self, x, y, z, w=0):
        self.x = x
        self.y = y
        self.z = z
        self.w = w
    
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

class Puzzle():
    def __init__(self):
        self.points = []
        self.readfile('input/puzzle17.txt')
    
    def readfile(self, file):
        with open(file) as f:
            i = 0
            for line in f:
                j = 0
                for c in line:
                    if c == '#':
                        self.points.append(Point3D(j, i, 0))
                    j += 1
                i += 1

    def problem1(self):
        # We need to iterate 6 times over our list of points
        # bounds should be 
        for _ in range(6):
            if len(self.points) == 0: break
            min_x = min([p.x for p in self.points]) - 1
            max_x = max([p.x for p in self.points]) + 1
            min_y = min([p.y for p in self.points]) - 1
            max_y = max([p.y for p in self.points]) + 1
            min_z = min([p.z for p in self.points]) - 1
            max_z = max([p.z for p in self.points]) + 1
            tmp_points = []
            
            for x in range(min_x, max_x + 1):
                for y in range(min_y, max_y + 1):
                    for z in range(min_z, max_z + 1):
                        neighbors = self.count_neighbors(x, y, z)
                        # print(f"({x}, {y}, {z}) has {neighbors} neighbors")
                        # does this point exist?
                        point = None
                        prob = constraint.Problem()
                        prob.addVariable('p', self.points)
                        prob.addConstraint(lambda p, x=x, y=y, z=z: p.x == x and p.y == y and p.z == z, ['p'])
                        if len(prob.getSolutions()) == 1:
                            point = prob.getSolutions()[0]['p']

                        # This point is active
                        if point is not None and 2 <= neighbors <= 3:
                            # print(f"Cell survived: {str(point)}")
                            tmp_points.append(point)
                        else:
                            if neighbors == 3:
                                # Create new point add it to buffer..
                                # print(f"Cell created: ({x}, {y}, {z})")
                                tmp_points.append(Point3D(x, y, z))
            self.points = tmp_points
            print(len(self.points))


    def problem2(self):
        print("Part 2")

        self.points = []
        self.readfile('input/puzzle17.txt')

        for _ in range(6):
            if len(self.points) == 0: break
            min_x = min([p.x for p in self.points]) - 1
            max_x = max([p.x for p in self.points]) + 1
            min_y = min([p.y for p in self.points]) - 1
            max_y = max([p.y for p in self.points]) + 1
            min_z = min([p.z for p in self.points]) - 1
            max_z = max([p.z for p in self.points]) + 1
            min_w = min([p.w for p in self.points]) - 1
            max_w = max([p.w for p in self.points]) + 1
            tmp_points = []
            
            for x in range(min_x, max_x + 1):
                for y in range(min_y, max_y + 1):
                    for z in range(min_z, max_z + 1):
                        for w in range(min_w, max_w +1):
                            neighbors = self.count_dimensional_neighbors(x, y, z, w)
                            # print(f"({x}, {y}, {z}) has {neighbors} neighbors")
                            # does this point exist?
                            point = None
                            prob = constraint.Problem()
                            prob.addVariable('p', self.points)
                            prob.addConstraint(lambda p, x=x, y=y, z=z, w=w: p.x == x and p.y == y and p.z == z and p.w == w, ['p'])
                            if len(prob.getSolutions()) == 1:
                                point = prob.getSolutions()[0]['p']

                            # This point is active
                            if point is not None and 2 <= neighbors <= 3:
                                # print(f"Cell survived: {str(point)}")
                                tmp_points.append(point)
                            else:
                                if neighbors == 3:
                                    # Create new point add it to buffer..
                                    # print(f"Cell created: ({x}, {y}, {z})")
                                    tmp_points.append(Point3D(x, y, z, w))
            self.points = tmp_points
            print(len(self.points))

    def count_neighbors(self, x, y, z):
        # Find all points in range (x-1, x+1)
        prob = constraint.Problem()
        prob.addVariable('p', self.points)
        a = x-1
        b = x+1
        c = y-1
        d = y+1
        e = z-1
        f = z+1
        prob.addConstraint(lambda p, a=a, b=b, c=c, d=d, e=e, f=f, x=x, y=y, z=z: \
            a <= p.x <= b and c <= p.y <= d and e <= p.z <= f \
                and not (p.x == x and p.y == y and p.z == z), ['p'])
        # print(f"({x}, {y}, {z}) Neighbors: {len(prob.getSolutions())}")
        return len(prob.getSolutions())
    
    def count_dimensional_neighbors(self, x, y, z, w):
        prob = constraint.Problem()
        prob.addVariable('p', self.points)
        a = x-1
        b = x+1
        c = y-1
        d = y+1
        e = z-1
        f = z+1
        g = w-1
        h = w+1
        prob.addConstraint(lambda p, a=a, b=b, c=c, d=d, e=e, f=f, g=g, h=h, x=x, y=y, z=z, w=w: \
            a <= p.x <= b and c <= p.y <= d and e <= p.z <= f and g <= p.w <= h \
                and not (p.x == x and p.y == y and p.z == z and p.w == w), ['p'])
        # print(f"({x}, {y}, {z}) Neighbors: {len(prob.getSolutions())}")
        return len(prob.getSolutions())

if __name__ == '__main__':
    puzzle = Puzzle()
    # puzzle.problem1()
    puzzle.problem2()