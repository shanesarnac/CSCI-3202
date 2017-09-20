class MilkStateNode:
	state = [0, 0, 0, 0]
	jug_max = [40, 40, 4, 5]
	
	def __init__(self, given_jugs):
		self.state = given_jugs
		
	def setMax(self, jug, new_max):
		self.jug_max[jug] = new_max
		
	def isFull(self, jug):
		return self.state[jug] == self.jug_max[jug]
	
	def isEmpty(self, jug):
		return self.state[jug] == 0
		
	def isEqual(self, node):
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
	
	def equals(self, node):
		for i in range(4):
			self.state[i] = node.state[i]
			self.jug_max[i] = node.jug_max[i]
			
	def pourJug(self, jug1, jug2):
		if self.isEmpty(jug1) or self.isFull(jug2):
			#print("the first jug is either empty or the second jug is already full")
			return
		newJug2 = self.state[jug2] + self.state[jug1]
		newJug1 = 0
		if newJug2 > self.jug_max[jug2]:
			delta = newJug2 - self.jug_max[jug2]
			newJug2 = newJug2 - delta
			newJug1 = newJug1 + delta 
		new_states = [0,0,0,0]
		for i in range(4):
			new_states[i] = self.state[i]
		
		new_states[jug1] = newJug1
		new_states[jug2] = newJug2
		#print("new states = " + str(new_states))
		return new_states
