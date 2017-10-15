
class Sim:
	node_count = 0
	
	def __init__(self):
		self.gameSetup()
		
	def gameSetup(self):
		print("Welcome to SIM")
		self.node_count = input("Enter the number of points you want to play with: ")
		print(self.node_count)
		


def main():
	Sim()
main()
