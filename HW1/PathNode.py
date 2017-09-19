from MilkStateNode import MilkStateNode

class PathNode:
	def __init__(self, parent_node, current_node):
		self.parent = parent_node
		self.current = current_node
