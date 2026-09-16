import randu

numbers = randu.randu(seed=1, n=10, multiplier=65539, modulus=2**31)
print(numbers)
