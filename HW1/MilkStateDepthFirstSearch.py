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
		
	def expandMilkStateNode(self, milk_state_path_node):
		current_node = milk_state_path_node.current
		possible_nodes = []
		for i in range(3):
			new_state = current_node.pourJug(0, i+1)
			possible_nodes.append(PathNode(current_node, MilkStateNode(new_state)))
			
			new_state = current_node.pourJug(3, 2-i)
			possible_nodes.append(PathNode(current_node, MilkStateNode(new_state)))
			
		new_state = current_node.pourJug(1,0)
		possible_nodes.append(PathNode(current_node, MilkStateNode(new_state)))
		
		for i in range(2):
			new_state = current_node.pourJug(1, i+2)
			possible_nodes.append(PathNode(current_node, MilkStateNode(new_state)))
			
			new_state = current_node.pourJug(2, i)
			possible_nodes.append(PathNode(current_node, MilkStateNode(new_state)))
		
		for path in possible_nodes:
			if path in self.already_checked:
				possible_nodes.remove(path)
		
		for path in possible_nodes:
			if path.current.state is not None:
				self.frontier.append(path)
			

	def printFrontier(self):
		print("Frontier:")
		for path in self.frontier:
			print("Parent = " + str(path.parent.state))
			print("Current = " + str(path.current.state))
			print("\n")
			
	def printAlreadyChecked(self):
		print("Already Checked:")
		if (len(self.already_checked) == 0):
			print("No items checked")
			return
		for path in self.already_checked:
			if path.parent == []:
				print("Parent = []")
			else:
				print("Parent = " + str(path.parent.state))
			print("Current = " + str(path.current.state))
			print("\n")
		
		
	def dfs(self, current_path):
		print("entered dfs")
		if self.goal_func(current_path.current):
			return current_path
		else:
			self.already_checked.append(current_path)
			# Expand current
			self.expandMilkStateNode(current_path)
			self.printFrontier()
			self.printAlreadyChecked()
			# DFS with Last in First Out
