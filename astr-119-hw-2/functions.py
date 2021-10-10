import numpy as np 
import sys

#define a func. that returns a value
def expo(x): 
	return np.exp(x) #return e^x
	

#define a subroutine that does not return a value
def show_expo(n):
	for i in range(n):
		print(expo(float(i))) #calls expo(x)


#define a main function
def main():
	n = 10 #prov default value for n

	#check if there is a command line argument provided
	if(len(sys.argv) > 1):
		n = int(sys.argv[1]) #if an argument was provided, we use it for n

	show_expo(n) #call show_expo(n)


#run the main function
if __name__ == '__main__': 
	main()


