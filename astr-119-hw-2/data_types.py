import numpy as np 		#import numpy lib

#integers

i = 10 			#integer
print(type(i))	#print out the data type of i

a_i = np.zeros(i, dtype=int)	#declare an array of ints
print(type(a_i)) 			 	#will return ndarray
print(type(a_i[0])) 			#will return int64

#floats

x = 119.10			#float point number
print(type(x))		

y = 1.19e2 			#float 119 in sci not
print(type(y))

z = np.zeros(i, dtype = float)	#declare an array of floats
print(type(z))					#will return nd array
print(type(z[0]))				#will return float64