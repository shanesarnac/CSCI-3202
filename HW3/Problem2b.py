
import math

epsilon = 0.0001

def infB(X):
	coeff = (X + 50.0) / 100.0
	prob_1 = X / (X + 50)
	prob_2 = 50 / (X + 50)
	#print("coeff = " + str(coeff))
	#print("prob_1 = " + str(prob_1))
	#print("prob_2 = " + str(prob_2))
	term_1 = -prob_1 * math.log(prob_1, 2)
	term_2 = -prob_2 * math.log(prob_2, 2)
	#print("term_1 = " + str(term_1))
	#print("term_2 = " + str(term_2))
	return coeff*(term_1 + term_2 )
	

def main():
	#inf_a = (-80/100)*math.log(80/100, 2) + (-20/100)*math.log(20/100, 2)
	inf_a = (-0.8)*math.log(0.8, 2) + (-0.2)*math.log(0.2, 2)
	
	
	print("Inf(A) = " + str(inf_a))
	print("Inf(B, X = 0.1) = " + str(infB(0.1)))
	print("Inf(B, X = 50.0) = " + str(infB(50.0)))
	X = 1.0
	while inf_a - infB(X) > epsilon:
		X += 1
		print("Inf(B, X = " + str(X) + ") = " + str(infB(X)))
		
	
	
main()
