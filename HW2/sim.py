
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
		
	def isGameOver(self):
		return False
		
	def isValidEdge(self, v1, v2):
		def isEdgeInEdgeList(v1, v2, edge_list):
			if edge_list == []:
				return False
			for edge in edge_list: 
				if edge.getEdge() == (v1, v2):
					return True
			return False
				
		if v1 == v2:
			return False
		if v1 not in self.node_list or v2 not in self.node_list:
			return False
		return not isEdgeInEdgeList(v1, v2, self.edge_list)
		
		
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
	
	def printEdgeList(self):
		red_edge_str = "Red Edges:"
		blue_edge_str = "Blue Edges: "
		for edge in self.edge_list:
			if edge.getPlayer() == "Red":
				red_edge_str += str(edge.getEdge()) + ","
			else:
				blue_edge_str += str(edge.getEdge()) + ","
		print(red_edge_str)
		print(blue_edge_str)
			
	def setPlayerColor(self):
		player_choice = raw_input("Would you like to be (r)ed or (b)lue? ")
		if player_choice == "r":
			self.player1 = Player.RED
			self.player2 = Player.BLUE
			self.current_player = self.player1
		elif player_choice == "b":
			self.player1 = Player.BLUE
			self.player2 = Player.RED
			self.current_player = self.player2
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
			
	def addEdge(self, edge_choice_lst):
		self.edge_list.append(Edge(edge_choice_lst[0], edge_choice_lst[1], self.current_player))
		
	def chooseEdge(self):
		print(self.current_player + " it is your turn!")
		self.printNodeList()
		self.printEdgeList()
		edge_choice = raw_input("Enter edge (ex: A,B): ")
		edge_choice_lst = edge_choice.split(",")
		if len(edge_choice_lst) != 2:
			print("Not a valid edge choice!")
			self.chooseEdge()
		elif not self.isValidEdge(edge_choice_lst[0], edge_choice_lst[1]):
			print("Not a valid edge choice!")
			self.chooseEdge()
		else: 
			self.addEdge(edge_choice_lst)
		
	def playGame(self):
		while not self.isGameOver():
			self.chooseEdge()
			self.switchPlayer()
			print("")
			
		# Check game state: Has anyone lost yet?
		# If not, let the next player pick a new edge
		print("Hello World")
		
	def switchPlayer(self):
		if self.current_player == self.player1:
			self.current_player = self.player2
		else:
			self.current_player = self.player1
		
	
		


def main():
	Sim()
main()
