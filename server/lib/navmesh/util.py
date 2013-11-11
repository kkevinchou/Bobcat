import math

def distance_between(point_a, point_b):
	return math.sqrt((point_a.x - point_b.x) ** 2 + (point_a.y - point_b.y) ** 2)