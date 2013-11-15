from node import Node

class Polygon(object):
	def __init__(self):
		self.points = []

	def get_points(self):
		return self.points

	def add_point(self, x, y):
		self.points.append(Node(x, y))