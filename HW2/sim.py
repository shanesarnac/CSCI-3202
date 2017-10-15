
debug = False

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
	
	def getEdge(self):
		return self.edge
	
	def getPlayer(self):
		return self.player

class Sim:
	game_mode = 0
	node_count = 0
	node_list = []
	edge_list = []
	player1 = 0
	player2 = 0
	
	
	def __init__(self):
		self.gameSetup()
		self.playGame()
		
	def isValidEdge(self, v1, v2):
		def isEdgeInEdgeList(v1, v2, lst):
			for edge in edge_list:
				if edge.getEdge() == (v1, v2):
					return True
				return False
				
		if v1 == v2:
			return False
		return !isEdgeInEdgeList(v1, v2, self.edge_list)
		
		
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
			
	def printNodeList(self):
		node_str = "Available Points: "
		for node in self.node_list:
			node_str += node + ", "
		print(node_str)
			
	def setPlayerColor(self):
		player_choice = raw_input("Would you like to be (r)ed or (b)lue? ")
		if player_choice == "r":
			self.player1 = Player.RED
			self.player2 = Player.BLUE
		elif player_choice == "b":
			self.player1 = Player.BLUE
			self.player2 = Player.RED
		else:
			print("Invalid choice")
			self.setPlayerColor()
			
		
	def gameSetup(self):
		print("Welcome to SIM")
		self.setGameMode()
		self.setNodeCount()
		self.generateNodeList()
		self.setPlayerColor()
		if debug == True:
			print("Game mode = " + str(self.game_mode))
			print("Node count = " + str(self.node_count))
			print("Node list = " + str(self.node_list))
			print("Player 1 Color: " + self.player1)
			print("Player 2 Color: " + self.player2)
		
	def chooseEdge(self):
		self.printNodeList()
		
	def playGame(self):
		if player1 == Player.RED:
			self.current_player = player1
		else:
			self.current_player = player2
		# Check game state: Has anyone lost yet?
		# If not, let the next player pick a new edge
		print("Hello World")
		
	
		


def main():
	Sim()
main()
