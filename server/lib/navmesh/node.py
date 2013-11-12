class Node(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.neighbors = []

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.x == other.x and self.y == other.y

        return False
