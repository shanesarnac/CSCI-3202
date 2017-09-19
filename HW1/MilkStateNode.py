class MilkStateNode:
	state = [0, 0, 0, 0]
	jug_max = [40, 40, 4, 5]
	
	def __init__(self, jug_a, jug_b, jug_c, juc_d):
		self.state = [jug_a, jug_b, jug_c, juc_d]
		
	def setMax(self, jug, new_max):
		self.jug_max[jug] = new_max
		
	def isFull(self, jug):
		return self.state[jug] == self.jug_max[jug]
	
	def isEmpty(self, jug):
		return self.state[jug] == 0
		
	def equals(self, node):
		if node.state[0] != self.state[0] :
			return False
		elif node.state[1] != self.state[1]:
			return False
		elif node.state[2] != self.state[2]:
			return False
		elif node.state[3] != self.state[3]:
			return False
		else:
			return True
			
	def pourJug(self, jug1, jug2):
		if self.state[jug1] == self
