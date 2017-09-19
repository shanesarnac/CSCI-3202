from MilkStateNode import MilkStateNode

class MilkStateTester:
	def isEqual(self):
		node1 = MilkStateNode([10, 10, 5, 4])
		node2 = MilkStateNode([10, 5, 3, 2])
		node3 = MilkStateNode([10, 10, 5, 3])
		node4 = MilkStateNode([10, 10, 5, 4])
		if node1.isEqual(node2):
			return False
		if node1.isEqual(node2):
			return False
		if node1.isEqual(node3):
			return False
		if node1.isEqual(node4):
			return True
	
	def runTests(self):
		if not self.isEqual():
			print("Node equals check failed")
			return False
		return True
		
	
