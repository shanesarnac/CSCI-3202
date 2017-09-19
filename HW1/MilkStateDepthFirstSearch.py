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
		
	def expandMilkStateNode(milk_state_node):
		possible_nodes = []
		for i in range(3):
			new_state = milk_state_node.pourJug(0, i+1)
			possible_nodes.append(PathNode(milk_state_node, MilkStateNode(new_state)))
			
			new_state = milk_state_node.pourJug(3, 2-i)
			possible_nodes.append(PathNode(milk_state_node, MilkStateNode(new_state)))
			
		new_state = milk_state_node.pourJug(1,0)
		possible_nodes.append(PathNode(milk_state_node, MilkStateNode(new_state)))
		
		for i in range(2):
			new_state = milk_state_node.pourJug(1, i+2)
			possible_nodes.append(PathNode(milk_state_node, MilkStateNode(new_state)))
			
			new_state = milk_state_node.pourJug(2, i)
			possible_nodes.append(PathNode(milk_state_node, MilkStateNode(new_state)))
			
		
		
		
		
	def dfs(self, current_path):
		print("entered dfs")
		if self.goal_func(current_path.current):
			return current_path
		else:
			self.already_checked.append(current_path)
			# Expand current
			# DFS with Last in First Out
