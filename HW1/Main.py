from MilkStateNode import MilkStateNode
from UnitTests import MilkStateTester
from MilkStateDepthFirstSearch import DepthFirstSearch

jugA = 40
jugB = 40
jugC = 0
jugD = 0


def goalFunction(node):
	if node.state[0] > 40:
		return False
	if node.state[1] > 40:
		return False
	if node.state[2] != 2:
		return False
	if node.state[3] != 2:
		return False
	if node.state[0] + node.state[1] + node.state[2] + node.state[3] != 80:
		return False
	return True
	
def goalFunction2(node):
	if node.state[0] != 38:
		return False
	if node.state[1] != 38:
		return False
	if node.state[2] != 2:
		return False
	if node.state[3] != 2:
		return False
	if node.state[0] + node.state[1] + node.state[2] + node.state[3] != 80:
		return False
	return True

def main():
	milk_state_tester = MilkStateTester()
	if not milk_state_tester.runTests():
		exit()
	
	initial_state = MilkStateNode([jugA, jugB, jugC, jugD])
	dfs = DepthFirstSearch(initial_state, goalFunction2)
	dfs.printSolutionPath()
	
	
	
main()
