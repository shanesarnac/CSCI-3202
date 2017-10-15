

class Player:
	RED = 0
	BLUE = 1
	
class GameMode:
	ONEPLAYER = 0
	TWOPLAYER = 1
	


class Sim:
	node_count = 0
	node_list = []
	game_mode = 0
	
	def __init__(self):
		self.gameSetup()
		
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
			if type(node_count_response) is int:
				self.node_count = node_count_response
			else:
				print("Invalid entry")
				self.setNodeCount()
		except NameError:
			print("Invalid entry")
			self.setNodeCount()
		
	def gameSetup(self):
		print("Welcome to SIM")
		self.setGameMode()
		self.setNodeCount()
		print(self.node_count)
		
		
		


def main():
	Sim()
main()
