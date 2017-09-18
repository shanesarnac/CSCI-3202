class MilkStateNode:
	state = {0, 0, 0, 0}
	max_jug_a = 40
	max_jug_b = 40
	max_jug_c = 4
	max_jug_d = 5
	
	def __init__(self, jug_a, jug_b, jug_c, juc_d):
		self.state = {jug_a, jug_b, jug_c, juc_d}
		
	def setMaxJugA(self, maxA):
		self.max_jug_a = maxA
		
	def setMaxJugB(self, maxB):
		self.max_jug_b = maxB
		
	def setMaxJugC(self, maxC):
		self.max_jug_c = maxC
		
	def setMaxJugD(self, maxD):
		self.max_jug_d = maxD
