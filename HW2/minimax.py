# Shane Sarnac
# Minimax Tree Algorithm
# October 2017
# This code should not be used by anyone besides myself without my permission


		
		
class MiniMaxLeaf:
	value = 0
	
	def __init__(self, val):
		self.value = val
	
	def getValue(self):
		return self.value
		
		
class MiniMaxNode:
	branches = []
	branching_factor = 0
	
	def __init__(self, bf):
		self.branching_factor = bf
		
	def addBranch(self, node):
		if self.getBranchCount() < self.branching_factor:
			print("Adding node to branch: " + str(node.getValue()))
			self.branches.append(node)
		else:
			new_branch = self.branches
			self.branches = [MiniMaxNode(self.branching_factor)]
			for node in new_branch:
				self.branches[0].addBranch(node)
		
	
	def getBranchCount(self):
		return len(self.branches)
		
		
class MiniMax:
	tree = []
	branching_factor = 0
	height = 0
	alpha = 0
	beta = 0
	
	def __init__(self, bf, leaves):
		self.branching_factor = bf
		self.setHeight(leaves)
		self.buildTree(leaves)
		
	def setHeight(self, leaves):
		num_count = len(leaves)
		while num_count >= 1:
			num_count = num_count/self.branching_factor
			self.height = self.height + 1
		
	def addLeaf(self, leaf):
		if len(self.tree) == 0:
			self.tree.append(MiniMaxNode(self.branching_factor))
		for branch in self.tree:
			branch.addBranch(leaf)
		
	
	def buildTree(self, leaves):
		for leaf in leaves:
			self.addLeaf(MiniMaxLeaf(leaf))

		
			
				
def main():
	leaves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	bf = 3
	tree = MiniMax(bf, leaves)
main()
		
