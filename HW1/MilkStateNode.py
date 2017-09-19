class MilkStateNode:
	state = [0, 0, 0, 0]
	max_jug_a = 40
	max_jug_b = 40
	max_jug_c = 4
	max_jug_d = 5
	
	def __init__(self, jug_a, jug_b, jug_c, juc_d):
		self.state = [jug_a, jug_b, jug_c, juc_d]
		
	def setMaxJugA(self, maxA):
		self.max_jug_a = maxA
		
	def setMaxJugB(self, maxB):
		self.max_jug_b = maxB
		
	def setMaxJugC(self, maxC):
		self.max_jug_c = maxC
		
	def setMaxJugD(self, maxD):
		self.max_jug_d = maxD
		
	def isMaxJugA(self):
		return self.state[0] == self.max_jug_a
		
	def isMaxJugB(self):
		return self.state[1] == self.max_jug_b
	
	def isMaxJugC(self): 
		return self.state[2] == self.max_jug_c
	
	def isMaxJugD(self):
		return self.state[3] == self.max_jug_d
		
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
