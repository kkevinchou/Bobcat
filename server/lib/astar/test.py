from astarplanner import AStarPlanner
from polygon import Polygon
from node import Node 

import numpy
from util import _compute_t_value

# planner = AStarPlanner()

# poly1 = Polygon()
# poly1.add_point(0, 0)
# poly1.add_point(0, 1)
# poly1.add_point(1, 1)
# poly1.add_point(1, 0)

# poly2 = Polygon()
# poly2.add_point(100, 0)
# poly2.add_point(100, 1)
# poly2.add_point(101, 1)
# poly2.add_point(101, 0)

# planner.add_polygon(poly1)
# planner.add_polygon(poly2)

# planner.find_path(0, 0, 1, 1)

a = [numpy.array([0, 0]), numpy.array([1, 1])]
# b = [numpy.array([0, 1]), numpy.array([1, 2])]
b = [numpy.array([1, 0]), numpy.array([0, 1])]
print _compute_t_value(a, b)