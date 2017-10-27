# Shane Sarnac
# Simple Mastermind game
# October 2017
# This code should not be used by anyone besides myself without my permission

import random

MAX_POSITIONS = 3
MAX_COLORS = 4

class Color:
	RED = "R"
	BLUE = "B"
	ORANGE = "O"
	WHITE = "W"
	
	
class Guess:
	colors_list = []
	def __init__(self, lst):
		if len(lst) != MAX_POSITIONS:
			print("Invalid guess")
			return
		self.colors_list = lst
		
	def getColors(self):
		return self.colors_list
		
	def getColor(self, index):
		return self.colors_list[index]
		
	def printGuess(self):
		color_string = ""
		for color in self.colors_list:
			color_string = color_string + color
		print("This must be it: " + color_string)
	
	def contains(self, color):
		return color in self.colors_list
			
			

class Mastermind:
	colors_list = [Color.BLUE, Color.ORANGE, Color.RED, Color.WHITE]
	possible_guesses = []
	is_game_over = False
	def __init__(self):
		self.generateGuesses()
		self.printWelcomeMessage()
		
	def isGameOver(self):
		return self.is_game_over
		
	def generateGuesses(self):
		for color1 in self.colors_list:
			for color2 in self.colors_list:
				for color3 in self.colors_list:
					self.possible_guesses.append(Guess([color1, color2, color3]))
					
	def printWelcomeMessage(self):
		print("Welcome to Mastermind, the game where I try to crack your code.")
		print("Your code must be three positions long and each position can only have")
		print("One of four colors: Blue, Orange, Red, or White")
		print("If I correctly guess a color but it is in the incorrect position, ")
		print("indicate that with an O")
		print("If I correctly guess a color and it is in the correct position, ")
		print("indicate that with an X")

		response = raw_input("Are you ready to begin? (y)es or (n)o: ")
		if response != "y":
			print("Too bad!")
		print("")
		self.startGame()
		
	def removeAll(self, guess):
		for color in guess.getColors():
			i = 0
			while i < len(self.possible_guesses):
				if self.possible_guesses[i].contains(color):
					del self.possible_guesses[i]
					i -= 1
				i += 1		
				
	def removeAllNotInGuess(self, guess):
		for color in self.colors_list:
			if not guess.contains(color):
				self.removeAllWithColor(color)
				
	def removeAllWithoutColorsInGuess(self, guess):
		for color in self.colors_list:
			if guess.contains(color):
				self.removeAllWithoutColor(color)
				
	def removeAllWithSimilarOrder(self, guess):
		for i in range(len(guess.getColors())):
			self.removeAllWithColorAtIndex(guess.getColor(i), i)
	
	def removeAllWithColorAtIndex(self, color, index):
		i = 0
		while i < len(self.possible_guesses):
			if self.possible_guesses[i].getColor(index) == color:
				del self.possible_guesses[i]
				i -= 1
			i += 1
				
	def removeAllWithoutColor(self, color):
		i = 0
		while i < len(self.possible_guesses):
			if not self.possible_guesses[i].contains(color):
				del self.possible_guesses[i]
				i -= 1
			i += 1
				
	def removeAllWithColor(self, color):
		i = 0
		while i < len(self.possible_guesses):
			if self.possible_guesses[i].contains(color):
				del self.possible_guesses[i]
				i -= 1
			i += 1
			
	def removeAllWithoutTwoColorsInGuess(self, guess):
		guess_colors = guess.getColors()
		valid = []
		i = 0
		while i < len(self.possible_guesses):
			possible_colors = self.possible_guesses[i].getColors()
			if guess_colors[0] in possible_colors and guess_colors[1] in possible_colors:
				valid.append(self.possible_guesses[i])
			elif guess_colors[1] in possible_colors and guess_colors[2] in possible_colors:
				valid.append(self.possible_guesses[i])
			elif guess_colors[0] in possible_colors and guess_colors[2] in possible_colors:
				valid.append(self.possible_guesses[i])
				
			if self.possible_guesses[i] not in valid:
				#print("Preparing to delete " + str(self.possible_guesses[i].getColors()) + " from available options")
				del self.possible_guesses[i]
				i -= 1
			i += 1
		self.possible_guesses.remove(guess)
	
	def removeAllWithoutOneColorInGuess(self, guess):
		guess_colors = guess.getColors()
		valid = []
		i = 0
		while i < len(self.possible_guesses):
			possible_colors = self.possible_guesses[i].getColors()
			if guess_colors[0] in possible_colors:
				valid.append(self.possible_guesses[i])
			elif guess_colors[1] in possible_colors:
				valid.append(self.possible_guesses[i])
			elif guess_colors[0] in possible_colors:
				valid.append(self.possible_guesses[i])
				
			if self.possible_guesses[i] not in valid:
				#print("Preparing to delete " + str(self.possible_guesses[i].getColors()) + " from available options")
				del self.possible_guesses[i]
				i -= 1
			i += 1
		self.possible_guesses.remove(guess)
			
	def removeAllWithoutTwoCorrectPositionsInGuess(self, guess):
		guess_colors = guess.getColors()
		valid = []
		i = 0
		while i < len(self.possible_guesses):
			possible_colors = self.possible_guesses[i].getColors()
			if guess_colors[0] == possible_colors[0] and guess_colors[1] == possible_colors[1] and not guess_colors[2] == possible_colors[2] :
				valid.append(self.possible_guesses[i])
			elif guess_colors[0] == possible_colors[0] and not guess_colors[1] == possible_colors[1] and guess_colors[2] == possible_colors[2] :
				valid.append(self.possible_guesses[i])
			elif not guess_colors[0] == possible_colors[0] and guess_colors[1] == possible_colors[1] and guess_colors[2] == possible_colors[2] :
				valid.append(self.possible_guesses[i])
				
			if self.possible_guesses[i] not in valid:
				#print("Preparing to delete " + str(self.possible_guesses[i].getColors()) + " from available options")
				del self.possible_guesses[i]
				i -= 1
			i += 1
	
	def removeAllWithoutOneCorrectPositionInGuess(self, guess):
		guess_colors = guess.getColors()
		valid = []
		i = 0
		while i < len(self.possible_guesses):
			possible_colors = self.possible_guesses[i].getColors()
			if guess_colors[0] == possible_colors[0] and not guess_colors[1] == possible_colors[1] and not guess_colors[2] == possible_colors[2] :
				valid.append(self.possible_guesses[i])
			elif not guess_colors[0] == possible_colors[0] and guess_colors[1] == possible_colors[1] and not guess_colors[2] == possible_colors[2] :
				valid.append(self.possible_guesses[i])
			elif not guess_colors[0] == possible_colors[0] and not guess_colors[1] == possible_colors[1] and guess_colors[2] == possible_colors[2] :
				valid.append(self.possible_guesses[i])
				
			if self.possible_guesses[i] not in valid:
				#print("Preparing to delete " + str(self.possible_guesses[i].getColors()) + " from available options")
				del self.possible_guesses[i]
				i -= 1
			i += 1
			
		
	def pickGuess(self):
		guess_idx = random.randint(0, len(self.possible_guesses)-1)
		return self.possible_guesses[guess_idx]
		
	
	def processResponse(self, response, guess):
		# No X or O given
		if len(response) == 0:
			self.removeAll(guess)
			return
		
		# XXX
		if len(response) == MAX_POSITIONS and "X" in response and "O" not in response:
			print("Haha! I Win!")
			self.is_game_over = True
			return
			
		# OOO
		if len(response) == MAX_POSITIONS and "O" in response and "X" not in response:
			self.removeAllNotInGuess(guess)
			self.removeAllWithoutColorsInGuess(guess)
			self.removeAllWithSimilarOrder(guess)
			return
			
		# XOO
		if len(response) == MAX_POSITIONS and "O" in response and "X" in response:
			self.removeAllNotInGuess(guess)
			self.removeAllWithoutColorsInGuess(guess)
			self.removeAllWithoutOneCorrectPositionInGuess(guess)
			return
		
		# OO
		if len(response) == (MAX_POSITIONS-1) and "O" in response and "X" not in response:
			self.removeAllWithoutTwoColorsInGuess(guess)
			return
		
		# XO
		if len(response) == (MAX_POSITIONS-1) and "O" in response and "X" in response:
			self.removeAllWithoutTwoColorsInGuess(guess)
			self.removeAllWithoutOneCorrectPositionInGuess(guess)
			return
			
		# XX
		if len(response) == (MAX_POSITIONS-1) and "X" in response and "O" not in response:
			self.removeAllWithoutTwoCorrectPositionsInGuess(guess)
			return
		
		# O
		if len(response) == (MAX_POSITIONS-2) and "O" in response and "X" not in response:
			self.removeAllWithoutOneColorInGuess(guess)
			return
			
		# X
		if len(response) == (MAX_POSITIONS-2) and "X" in response and "O" not in response:
			self.removeAllWithoutOneCorrectPositionInGuess(guess)
			return
			
		print("There is " + str(len(self.possible_guesses)) + " guesses remaining and they are:")
		for guess in self.possible_guesses:
			print(guess.getColors())
			
		
	def startGame(self):
		while not self.isGameOver():
			guess = self.pickGuess()
			guess.printGuess()
			response = raw_input("Is this the correct guess? ")
			self.processResponse(response, guess)
		
				

def main():
	Mastermind()
main()
