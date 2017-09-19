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
		
	def isFullJugA(self):
		return self.state[0] == self.max_jug_a
		
	def isFullJugB(self):
		return self.state[1] == self.max_jug_b
	
	def isFullJugC(self): 
		return self.state[2] == self.max_jug_c
	
	def isFullJugD(self):
		return self.state[3] == self.max_jug_d
		
	def isEmptyJugA(self):
		return self.state[0] == 0
	
	def isEmptyJugB(self):
		return self.state[1] == 0
	
	def isEmptyJugC(self):
		return self.state[2] == 0
		
	def isEmptyJugD(self):
		return self.state[3] == 0
		
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
