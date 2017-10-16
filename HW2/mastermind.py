# Shane Sarnac
# Simple Mastermind game
# October 2017
# This code should not be used by anyone besides myself without my permission

MAX_COLORS = 4

class Color:
	RED = "Red"
	BLUE = "Blue"
	ORANGE = "Orange"
	WHITE = "White"
	
class Guess:
	colors_list = []
	def __init__(self, lst):
		if len(lst) != MAX_COLORS:
			print("Invalid guess")
			return
		self.colors_list = lst
		

class Mastermind:
	possible_guesses = []
	def __init__(self):
		print("Hello World!")

def main():
	Mastermind()
main()
