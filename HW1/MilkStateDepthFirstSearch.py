from MilkStateNode import MilkStateNode
from PathNode import PathNode

class DepthFirstSearch:
	frontier = []
	already_checked = []
	goal_func = 0
	
	def __init__(self, start, goal):
		print("entered DepthFirstSearch init")
		self.goal_func = goal
		self.dfs(PathNode([], start))
		
	def dfs(self, current_path):
		print("entered dfs")
		if self.goal_func(current_path.current):
			return current_path
		else:
			self.already_checked.append(current_path)
			# Expand current
			# DFS with Last in First Out
