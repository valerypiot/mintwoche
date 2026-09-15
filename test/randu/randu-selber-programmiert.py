import numpy as np

seed = np.int32(1)  # Initial seed value
a = np.int32(65539) # Multiplier => easy to calculate because of bit shifting
m = 2**31           # Modulus limit of 32bit 2**31 too big for 32bit int 

def randu(seed, n):
	random_numbers = []
	for _ in range(n):
		seed = np.int32((int(a) * int(seed)) % m)   # overflow if not casted to int
		random_numbers.append(seed)                 # append new random number to array   
	return random_numbers


print(randu(seed, 10))