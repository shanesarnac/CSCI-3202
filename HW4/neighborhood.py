# Author: Shane Sarnac
# Date: 5 December 2017
# This code should not be used for any purpose without my permission. 

class House:
	occupied = 0
	def __init__(self, occ):
		if occ < 0:
			print("invalid occupant")
			exit()
		self.occupied = occ
		
	def isOccupied(self):
		return self.occupied != 0
		
class Neighborhood:
	def __init__(self):
		
		House(1)

def main():
	Neighborhood()
	
main()
