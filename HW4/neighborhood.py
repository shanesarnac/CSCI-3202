

class House:
	def __init__(self):
		print("Hello World!")
		
class Neighborhood:
	def __init__(self):
		House()

def main():
	Neighborhood()
	
main()
