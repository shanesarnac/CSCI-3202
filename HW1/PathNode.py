from MilkStateNode import MilkStateNode

class PathNode:
	def __init__(self, parent_node, current_node):
		self.parent = parent_node
		self.current = current_node
		
	def isPathEqual(self, path):
		if set(self.parent) != set(path.parent):
			return False
		if set(self.current) != set(path.current):
			return False
		return True
