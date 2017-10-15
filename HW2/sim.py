

class Player:
	RED = "Red"
	BLUE = "Blue"
	
class GameMode:
	ONEPLAYER = "One Player"
	TWOPLAYER = "Two Player"

class Edge:
	def __init__(self, v1, v2, p):
		self.edge = (v1, v2)
		self.player = p

class Sim:
	game_mode = 0
	node_count = 0
	node_list = []
	edge_list = []
	
	
	def __init__(self):
		self.gameSetup()
		self.launchGame()
		
	def setGameMode(self):
		mode = 0
		try:
			mode = input("Would you like to play a (1) one-player or (2) two-player game? ")
			if (mode == 1):
				self.game_mode = GameMode.ONEPLAYER
			elif(mode == 2):
				self.game_mode = GameMode.TWOPLAYER
			else:
				print("Invalid entry")
				self.setGameMode()
		except NameError:
			print("Invalid entry")
			self.setGameMode()	
		
			
	def setNodeCount(self):
		node_count_response = 0
		try:
			node_count_response = input("Enter the number of points you want to play with: ")
			if type(node_count_response) is int and node_count_response > 3:
				self.node_count = node_count_response
			else:
				print("Invalid entry")
				self.setNodeCount()
		except NameError:
			print("Invalid entry")
			self.setNodeCount()
			
	def generateNodeList(self):
		for count in range(self.node_count):
			self.node_list.append(chr(ord('A') + count))
			
		
	def gameSetup(self):
		print("Welcome to SIM")
		self.setGameMode()
		self.setNodeCount()
		self.generateNodeList()
		print("Game mode = " + str(self.game_mode))
		print("Node count = " + str(self.node_count))
		print("Node list = " + str(self.node_list))
		
	def launchGame(self):
		print("Hello World!")
		


def main():
	Sim()
main()
