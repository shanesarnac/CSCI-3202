# Shane Sarnac
# Sim Game
# October 2017

import math

debug = False

def nCr(n, r):
	if r >= n:
		return 0
	return math.factorial(n)/(math.factorial(r)*math.factorial(n-r))


class SimAI:
	my_edges = []
	opponents_edges = []
	node_list = []
	node_overlap = {}
	
	def __init__(self, nodes):
		self.node_list = nodes
		for node in self.node_list:
			self.node_overlap[node] = 0
		
	def countNodeOverlap(self):
		for node in self.node_list:
			self.node_overlap[node] = 0
		for edge in self.my_edges:
			(node1, node2) = edge.getEdge()
			self.node_overlap[node1] += 1
			self.node_overlap[node2] += 1
			
	def buildEdgeWeightTree(self, remaining):
		weighted_edges = []
		for edge in remaining:
			(node1, node2) = edge.getEdge()
			weight = self.node_overlap[node1] + self.node_overlap[node2]
			weighted_edges.append((edge, weight))
			#print("Edge: (" + node1 + "," + node2 + ")")
			#print("Weight: " + str(weight))
		return weighted_edges
				
	def findBestEdge(self, remaining):
		self.countNodeOverlap()
		edge_weight_tree = self.buildEdgeWeightTree(remaining)
		best_edge_weight = 100
		best_edge = 0
		for node in edge_weight_tree:
			(edge, weight) = node
			print("Edge: " + str(edge.getEdge()) + " Weight: " + str(weight))
			print(best_edge_weight)
			if weight < best_edge_weight:
				best_edge_weight = weight
				best_edge = edge
		return best_edge
	
	def chooseBestEdge(self, myedges, oppedges, remaining):
		self.my_edges = myedges
		self.opponents_edges = oppedges
		return self.findBestEdge(remaining)

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
	red_edge_list = []
	blue_edge_list = []
	max_edges = 0
	player1 = 0
	player2 = 0
	
	
	def __init__(self):
		self.gameSetup()
		self.playGame()
	
	def isTriangle(self, edge_list):
		# if there are only 3 unique characters, it must be a triangle
		unique_chars = []
		for edge in edge_list:
			for character in edge.getEdge():
				if character not in unique_chars:
					unique_chars.append(character)
		
		if debug:
			print("Edge List = " + str(edge_list[0].getEdge()) + "," + str(edge_list[1].getEdge()) + "," + str(edge_list[2].getEdge()))
			print("Unique Chars = " + str(unique_chars))
		return len(unique_chars) == 3

		
		
	def isGameOver(self):
		player_list = []
		if self.current_player == Player.RED:
			player_list = self.red_edge_list
		else:
			player_list = self.blue_edge_list
		
		if debug:
			print("\nisGameOver - Player is" + self.current_player)
			edge_str = "isGameOver - edge_list is "
			for edge in player_list:
				edge_str += str(edge.getEdge()) + "," 
			print(edge_str + "\n")
		
		if len(player_list) < 3:
			return False

		for i in range(len(player_list)-2):
			for j in range(i+1, len(player_list)-1):
				for k in range(j+1,len(player_list)):
					if (self.isTriangle([player_list[i], player_list[j], player_list[k]])):
						return True
		
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
		
	def getRemainingEdges(self):
		remaining_edges = []
		for i in range(self.node_count-1):
			for j in range(i+1, self.node_count):
				if self.isValidEdge(self.node_list[i], self.node_list[j]):
					remaining_edges.append(Edge(self.node_list[i], self.node_list[j],[]))
		return remaining_edges
		
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
				self.max_edges = nCr(self.node_count, 2)
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
		edge_to_add = Edge(edge_choice_lst[0], edge_choice_lst[1], self.current_player)
		self.edge_list.append(edge_to_add)
		if self.current_player == Player.RED:
			self.red_edge_list.append(edge_to_add)
		else:
			self.blue_edge_list.append(edge_to_add)
		
	def chooseEdge(self):
		if self.game_mode == GameMode.ONEPLAYER and self.current_player == self.player2:
			self.chooseEdgeAI()
		else:
			self.chooseEdgeUser()
			
	def chooseEdgeUser(self):
		print(self.current_player + " it is your turn!")
		self.printNodeList()
		self.printEdgeList()
		edge_choice = raw_input("Enter edge (ex: A,B): ")
		edge_choice_lst = edge_choice.split(",")
		edge_choice_lst = sorted(edge_choice_lst)
		if len(edge_choice_lst) != 2:
			print("Not a valid edge choice!\n")
			self.chooseEdge()
		elif not self.isValidEdge(edge_choice_lst[0], edge_choice_lst[1]):
			print("Not a valid edge choice!\n")
			self.chooseEdge()
		else: 
			self.addEdge(edge_choice_lst)
			
	def chooseEdgeAI(self):
		# Find all remaining options
		ai_edges = []
		usr_edges = []
		if self.current_player == Player.RED:
			ai_edges = self.red_edge_list
			usr_edges = self.blue_edge_list
		else:
			ai_edges = self.blue_edge_list
			usr_edges = self.red_edge_list
		ai = SimAI(self.node_list)
		edge_choice = ai.chooseBestEdge(ai_edges, usr_edges, self.getRemainingEdges())
		self.addEdge([edge_choice.getEdge()[0], edge_choice.getEdge()[1]])

		
	def playGame(self):
		if debug:
			print("Max edges = " + str(self.max_edges))
		print("")
		self.chooseEdge()
		print("")
		while not self.isGameOver() and len(self.edge_list) < self.max_edges:
			self.switchPlayer()
			self.chooseEdge()
			print("")
		
		if len(self.edge_list) == self.max_edges:
			print("This game is a draw!")
		else:
			print(self.current_player + ", you lose!")
			self.switchPlayer()
			print(self.current_player + ", you win!")
		
	def switchPlayer(self):
		if self.current_player == self.player1:
			self.current_player = self.player2
		else:
			self.current_player = self.player1
		
	
		


def main():
	Sim()
main()
