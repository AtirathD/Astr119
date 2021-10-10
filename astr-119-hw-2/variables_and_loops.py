import numpy as np 

def main():
	i = 0
	n = 10
	x = 119.0

	y = np.zeros(n, dtype = float) #declares n (defined as 10 above) zeros as floats using np

	#loops can be used to iterate with a variable

	for i in range(n): #i in range [0, n-1]
		y[i] = 2.0 * float(i) + 1 #set element = 2i + 1 as float

	# we can iterate through a variable as well:
	for y_element in y:
		print (y_element)



	#executes the main function
	if __name__ == '__main__':
		main()

		
