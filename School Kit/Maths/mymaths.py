import numpy as np

# Sum numbers 1 upto x.
#(Known as "Triangular number": https://en.wikipedia.org/wiki/Triangular_number)
sumto = lambda x: (x**2 + x)//2

# Using Numpy for factorial (instead of the commonly used recursion)
factorial = lambda n: np.prod(np.arange(1,n+1))
