from MilkStateNode import MilkStateNode
from PathNode import PathNode
	

class DepthFirstSearch:
	frontier = []
	already_checked = []
	solution = []
	goal_func = 0
	max_iter = 1000
	current_iter = 0
	
	def __init__(self, start, goal):
		self.goal_func = goal
		self.solution = self.dfs(PathNode([], start))
		
	def addToFrontier(self, milk_state_path_node):
		for node in self.already_checked:
			if node.state == milk_state_path_node.current.state:
				return
		for node in self.frontier:
			if node.current.state == milk_state_path_node.current.state:
				return
		if milk_state_path_node.current.state is None:
			return
		self.frontier.append(milk_state_path_node)
		
		
	def expandMilkStateNode(self, milk_state_path_node):
		current_node = milk_state_path_node.current
		possible_nodes = []
		for i in range(3):
			new_state = current_node.pourJug(0, i+1)
			self.addToFrontier(PathNode(milk_state_path_node, MilkStateNode(new_state)))
			new_state = current_node.pourJug(3, 2-i)
			self.addToFrontier(PathNode(milk_state_path_node, MilkStateNode(new_state)))
			
		new_state = current_node.pourJug(1,0)
		self.addToFrontier(PathNode(milk_state_path_node, MilkStateNode(new_state)))
		
		for i in range(2):
			new_state = current_node.pourJug(1, i+2)
			self.addToFrontier(PathNode(milk_state_path_node, MilkStateNode(new_state)))
			new_state = current_node.pourJug(2, i)
			self.addToFrontier(PathNode(milk_state_path_node, MilkStateNode(new_state)))


	def printFrontier(self):
		print("Frontier:")
		for path in self.frontier:
			if path.parent == []:
				print("Parent = []")
			else:
				print("Parent = " + str(path.parent.current.state))
			print("Current = " + str(path.current.state))
			print("\n")
			
	def printAlreadyChecked(self):
		print("Already Checked:")
		if (len(self.already_checked) == 0):
			print("No items checked")
			return
		for state in self.already_checked:
			print("Current = " + str(state.state))
			print("\n")
		
	def printFrontierSize(self):
		print("Frontier Size: " + str(len(self.frontier)))
		
	def printAlreadyCheckedSize(self):
		print("Already Checked Size: " + str(len(self.already_checked)))
		
	def printSolutionPath(self):
		def printPath(path):
			if path.parent != []:
				printPath(path.parent)
			print(path.current.state)
		if self.solution is not None:
			printPath(self.solution)
		else:
			print("No solution.")
		
	def dfs(self, current_path):
		if self.current_iter == self.max_iter:
			return
		self.current_iter += 1
		if self.goal_func(current_path.current):
			return current_path
		else:
			self.already_checked.append(current_path.current)
			# Expand current
			self.expandMilkStateNode(current_path)
			if len(self.frontier) == 0:
				self.printAlreadyCheckedSize()
				return
			# DFS with Last in First Out
			return self.dfs(self.frontier.pop())
