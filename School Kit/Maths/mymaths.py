import numpy as np

# Sum numbers 1 upto x.
#(Known as "Triangular number": https://en.wikipedia.org/wiki/Triangular_number)
sumto = lambda x: (x**2 + x)//2

# Convert list/tuple into array of numbers
vector = lambda lst: np.array(lst) # set/dict will be 0-dimensional arrays

# Using Numpy for factorial (instead of the commonly used recursion)
factorial = lambda n: np.prod(np.arange(1,n+1))

# Above factorial() vectorized for numpy-arrays
np_factorial = np.vectorize(factorial)

# Sums of factorials upto n (1! + 2! + ... + n!)
factorial_sums = lambda n: sum(np_factorial(np.arange(1,n+1)))
