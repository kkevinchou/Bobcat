from node import Node
from Queue import PriorityQueue
from heapq import heappush, heappop

class Navmesh(object):
	def __init__(self):
		self.polygons = []
		self.nodes = []

	def add_polygon(self, polygon):
		self.polygons.append(polygon)
		
		polygon_points = polygoin.get_points()
		for point in polygon_points:
			self.nodes.add(Node(point.x, point.y))

	def compute_neighbours(self):
		for node_a in self.nodes:
			for node_b in self.nodes:
				if node_a == node_b:
					continue

				if not intersects(node, polygons):
					node_a.neighbours.append(node_b)

	def find_path(self, x1, y1, x2, y2):
		start_node = Node(x1, y1)
		goal_node = Node(x2, y2)

		# check for direct los from start_node to goal_node
		# Find closest nodes, sort by distance.
		# Find the first node that is in los

		closest_node = None

		open_queue = []
		heappush(open_queue, (0, closest_node))

		while len(open_queue) > 0:
			current_node = heappop(open_queue)



