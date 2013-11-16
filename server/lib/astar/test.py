from astarplanner import AStarPlanner
from polygon import Polygon

import numpy
from util import intersect_single

def basic_intersection_test():
    poly = Polygon()
    poly.add_point(0, 0)
    poly.add_point(0, 1)
    poly.add_point(-1, 1)
    poly.add_point(-1, 0)

    line = [numpy.array([0, 0]), numpy.array([0, 1])]
    assert(intersect_single(line, poly) == True)

    line = [numpy.array([0, 1]), numpy.array([-1, 1])]
    assert(intersect_single(line, poly) == True)

    line = [numpy.array([-1, 1]), numpy.array([-1, 0])]
    assert(intersect_single(line, poly) == True)

    line = [numpy.array([-1, 0]), numpy.array([0, 0])]
    assert(intersect_single(line, poly) == True)

tests = [
    basic_intersection_test,
]

for test in tests:
    test()

# poly2 = Polygon()
# poly2.add_point(100, 0)
# poly2.add_point(100, 1)
# poly2.add_point(101, 1)
# poly2.add_point(101, 0)

# planner.add_polygon(poly1)
# planner.add_polygon(poly2)

# planner.find_path(0, 0, 1, 1)

# b = [numpy.array([0, 0]), numpy.array([1, 1])]

# c = numpy.array([0, 1])
# d = numpy.array([1, 0])

# print numpy.array_equal(c, d)
# b = [numpy.array([0, 0]), numpy.array([1, 1])]
# print _compute_t_value(a, b)
