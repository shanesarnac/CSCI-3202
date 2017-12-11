# Author: Shane Sarnac
# Date: 5 December 2017
# This code should not be used for any purpose without my permission. 

from random import randint

class House:
	occupied = 0
	def __init__(self, occ):
		if occ < 0:
			print("invalid occupant")
			exit()
		self.occupied = occ
		
	def isOccupied(self):
		return self.occupied != 0
		
	def getOccupant(self):
		return self.occupied
		
class Neighborhood:
	total_ones = 0
	total_twos = 0
	total_empty = 0
	neighborhood = []
	empty = [] # holds the indices of empty homes in the neighborhood
	
	def __init__(self, ones, twos, empty):
		self.total_ones = ones
		self.total_twos = twos
		self.total_empty = empty 
		self.buildNeighborhood()
		#self.printNeighborhood()
	
	def buildNeighborhood(self):
		ones_remaining = self.total_ones
		twos_remaining = self.total_twos
		empty_remaining = self.total_empty
		
		
		while ones_remaining > 0 or twos_remaining > 0 or empty_remaining > 0:
			occupant = randint(0,2)
			if occupant == 2 and twos_remaining > 0:
				self.neighborhood.append(House(occupant))
				twos_remaining = twos_remaining - 1
			elif occupant == 1 and ones_remaining > 0:
				self.neighborhood.append(House(occupant))
				ones_remaining = ones_remaining - 1
			elif occupant == 0 and empty_remaining > 0:
				self.neighborhood.append(House(occupant))
				empty_remaining = empty_remaining - 1
				self.empty.append(len(self.neighborhood)-1)
				
	def printNeighborhoodExtended(self):
		neighborhood_str = ""
		ones_count = 0
		twos_count = 0
		for i in range(len(self.neighborhood)):
			neighborhood_str += "Address = " + str(i) + ", Occupant = " + str(self.neighborhood[i].getOccupant())
			if self.neighborhood[i].getOccupant() == 0:
				neighborhood_str += " <= Empty"
			neighborhood_str += "\n"
			
			if self.neighborhood[i].getOccupant() == 1:
				ones_count += 1
			if self.neighborhood[i].getOccupant() == 2:
				twos_count += 1
		print(neighborhood_str)
		print("Ones count = " + str(ones_count))
		print("Twos count = " + str(twos_count))
		
	def printNeighborhood(self):
		neighborhood_str = ""
		zeroes_str = ""
		for i in range(len(self.neighborhood)):
			neighborhood_str += str(self.neighborhood[i].getOccupant())
			
		for i in range(len(self.empty)):
			zeroes_str += str(self.empty[i]) + ","
		# print(neighborhood_str + "     " + zeroes_str)
		# print(neighborhood_str + "\n")
		print(neighborhood_str)
				
	def findDissatisfied(self):
		neighborhood_size = len(self.neighborhood)
		dissatisfied = [] # contains index of dissatisfied occupants
		left_1 = 0
		left_2 = 0
		right_1 = 0
		right_2 = 0
		
		for i in range(len(self.neighborhood)):
			preferred_neighbor_count = 0
			left_2 = self.neighborhood[(i-2)%neighborhood_size].getOccupant()
			left_1 = self.neighborhood[(i-1)%neighborhood_size].getOccupant()
			occupant = self.neighborhood[i].getOccupant()
			right_1 = self.neighborhood[(i+1)%neighborhood_size].getOccupant()
			right_2 = self.neighborhood[(i+2)%neighborhood_size].getOccupant()
			
			if occupant == left_2:
				preferred_neighbor_count += 1
			if occupant == left_1:
				preferred_neighbor_count += 1
			if occupant == right_1:
				preferred_neighbor_count += 1
			if occupant == right_2:
				preferred_neighbor_count += 1
				
			if preferred_neighbor_count < 2 and occupant != 0:
				dissatisfied.append(i)
		return dissatisfied
		
	def moveDissatisified(self, dissatisfied):
		if len(dissatisfied) == 0:
			return
		random_dissatisfied_index = dissatisfied[randint(0, len(dissatisfied)-1)]
		random_empty_index = randint(0, len(self.empty)-1)
		
		# print("random_dissatisfied_index = " + str(random_dissatisfied_index))
		# print("random_empty_index = " + str(random_empty_index))
		# print("empty index = " + str(self.empty[random_empty_index]))
		
		# get the unhappy resident from the neighborhood and make the home empty
		unhappy_occupant = self.neighborhood[random_dissatisfied_index] 
		self.neighborhood[random_dissatisfied_index] = House(0) 
		
		# find a new empty home, move the resident into it, 
		# and store the the new empty home in the empty list
		new_home = self.empty[random_empty_index]
		self.neighborhood[new_home] = unhappy_occupant
		self.empty[random_empty_index] = random_dissatisfied_index
			
				
	def runSimulation(self, print_iter, max_iter):
		for i in range(max_iter):
			if i % print_iter == 0:
				self.printNeighborhood()	
			dissatisfied = self.findDissatisfied()	
			self.moveDissatisified(dissatisfied)
		

def main():
	neighborhood = Neighborhood(27, 27, 6)
	neighborhood.runSimulation(5, 100)
	
	
	
main()
