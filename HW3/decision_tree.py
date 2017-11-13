# Shane Sarnac
# CSCI 3202
# Cannot be used without expressed consent by original creator
import csv

# TV Attributes
# Seen ~ Seen before
# Enj ~ Enjoyed
# Length ~ Length of show (<=30 min)
# Super ~ Supernatural elements
# Survive ~ Survival Show
# Hero ~ Super Hero
# Reality ~ Reality Tv
# Funny ~ Commedy 
# Watch ~ Should watch (Training answer)

TV_FILE = "tv_shows.csv"

class TV_Show:	
	def __init__(self, show_name, attr, watch):
		self.name = show_name
		self.attributes = attr
		self.should_watch = watch
		
	

class TV_Show_Creator:
	def buildTvShowsFromFile(self,filename):
		tv_file = open(filename, "r")
		headers = tv_file.readline()
		headers = headers.split(",")
		for i in range(len(headers)):
			headers[i] = headers[i].rstrip()
		
		tv_show_list = []
		for line in tv_file:
			i = 0
			attr = line.split(",")
			name = ""
			attributes = {}
			for head in headers:
				if attr[i].rstrip() == "TRUE":
					attributes[head] = True
				elif attr[i].rstrip() == "FALSE":
					attributes[head] = False
				else:
					attributes[head] = attr[i].rstrip()
				i += 1
			name = attributes.pop("Name")
			tv_show_list.append(TV_Show(name, attributes))	
			print(tv_show_list[-1].attributes)
		
		tv_file.close()
		return tv_show_list		
		
class DecisionTree:
	def __init__(self, tv_shows):
		

def main():
	creator = TV_Show_Creator()
	tv_shows = creator.buildTvShowsFromFile(TV_FILE)
	
	
	
main()
