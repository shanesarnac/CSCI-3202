# Shane Sarnac
# Minimax Tree Algorithm
# October 2017
# This code should not be used by anyone besides myself without my permission

class MiniMaxNode:
	value = 0
	branches = []
	is_leaf = False
	
	def __init__(self, val, isleaf):
		self.value = val
		self.is_leaf = isleaf
		
	def setValue(self, val):
		self.value = val
		
	def isLeaf(self):
		return is_leaf
		

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
		print("Height = " + str(self.height))
	
	def buildTree(self, leaves):
		for i in range(self.height):
			print("depth = " + str(i))
		
		
		
def main():
	leaves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	bf = 3
	tree = MiniMax(bf, leaves)
main()
		
