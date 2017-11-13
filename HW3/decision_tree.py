# Shane Sarnac
# CSCI 3202
# Cannot be used without expressed consent by original creator

import math

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
	def __init__(self, show_name, attr):
		self.name = show_name
		self.attributes = attr
		
	

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
			#print(tv_show_list[-1].attributes)
		
		tv_file.close()
		headers.remove("Name")
		headers.remove("Watch")
		
		return (tv_show_list, headers)	
		
class DecisionTreeNode:
	def __init__(self, attr, pointers):
		self.attribute = attr
		self.pointers_list = pointers	
		
class DecisionTree:
	
	def __init__(self, headers, tv_shows):
		print("Length of tv_shows = " + str(len(tv_shows)))
		#self.headers_list = headers
		#self.shows_list = tv_shows
		self.tree = self.buildTree(headers, tv_shows)
		
	def buildTree(self, headers, shows_list):
		if len(shows_list) == 0 or len(headers) == 0:
			return
		best_attr = ""
		best_attr_value = 100
		for header in headers:
			info = self.getInfo(header, shows_list)
			if info < best_attr_value:
				best_attr = header
				best_attr_value = info
		print("best attr = " + best_attr)
		print("best_attr_value = " + str(best_attr_value))
		headers.remove(best_attr)
		(shows_with, shows_without) = self.getListWithAttribute(best_attr, shows_list)
		return DecisionTreeNode(best_attr, [self.buildTree(headers, shows_with), self.buildTree(headers, shows_without)])
		
	def getListWithAttribute(self, attr, shows_list):
		shows_with = []
		shows_without = []
		for show in shows_list:
			if show.attributes[attr]:
				shows_with.append(show)
			else:
				shows_without.append(show)
				
		return (shows_with, shows_without)
		
	def getNumberWithAttribute(self, attr, shows_list):
		count = 0
		for show in shows_list:
			if show.attributes[attr]:
				count += 1
		return count	
			
	def getInfo(self, attr, shows_list):
		print("")
		print("attr = " + attr)
		print("size of shows_list = " + str(len(shows_list)))
		(shows_with, shows_without) = self.getListWithAttribute(attr, shows_list)
		total_with_attribute = float(len(shows_with))
		total_without_attribute = float(len(shows_without))
		total = float(len(shows_list))
		
		weight_with = total_with_attribute / total
		weight_without = total_without_attribute / total
		
		number_watch_with = float(self.getNumberWithAttribute("Watch", shows_with))
		number_watch_without = float(self.getNumberWithAttribute("Watch", shows_without))
		
		print("number_watch_with = " + str(number_watch_with))
		print("number_watch_without = " + str(number_watch_without))
		print("total_with_attribute = " + str(total_with_attribute))
		print("total_without_attribute = " + str(total_without_attribute))
		
		prob_1_with = 0.0
		prob_2_with = 0.0
		if total_with_attribute != 0:
			prob_1_with = number_watch_with / total_with_attribute
			prob_2_with = 1.0 - prob_1_with
		
		prob_1_without = 0.0
		prob_2_without = 0.0
		if total_without_attribute != 0:
			prob_1_without = number_watch_without / total_without_attribute
			prob_2_without = 1.0 - prob_1_without
		
		print("prob_1_with = " + str(prob_1_with))
		print("prob_2_with = " + str(prob_2_with))
		print("prob_1_without = " + str(prob_1_without))
		print("prob_2_without = " + str(prob_2_without))
		
		info_with = 0.0
		if prob_1_with != 0: 
			info_with += (-prob_1_with) * math.log(prob_1_with, 2)
		if prob_2_with != 0:
			info_with += (-prob_2_with) * math.log(prob_2_with, 2)
		info_with *= weight_with
		print("info_with = " + str(info_with))
		
		info_without = 0.0
		if prob_1_without != 0:
			info_without += (-prob_1_without) * math.log(prob_1_without, 2)
		if prob_2_without != 0:
			info_without += (-prob_2_without) * math.log(prob_2_without, 2)
		info_without *= weight_without
		print("info_without = " + str(info_without))
		
		return info_with + info_without
		
		
		

def main():
	creator = TV_Show_Creator()
	(tv_shows, headers) = creator.buildTvShowsFromFile(TV_FILE)
	decision_tree = DecisionTree(headers,tv_shows[0:20])
	
	
	
main()
