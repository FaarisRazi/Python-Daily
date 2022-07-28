import numpy as np
from math import sqrt, gcm 
# gcm: Greatest Common Multiple (or Greatest Common Divisor)

# Convert list/tuple into array of numbers
vector = lambda lst: np.array(lst) # set/dict will be 0-dimensional arrays

# Sum numbers 1 upto x.
#(Known as "Triangular number": https://en.wikipedia.org/wiki/Triangular_number)
sumto = lambda x: (x**2 + x)//2

# Lowest Common Multiple (or Least Common Divisor)
def lcm(numbers):
    if isinstance(numbers, (set, dict)):
        numbers = tuple(numbers)
        
    return np.lcm.reduce(numbers)


# Get x solutions for your quadratic equation: ax^2 + bx + c
def quadratic(a,b,c, show=True, equal1 = False): 
    # Example for x^2 - 5x + 6 = quadratic(1,-5,6):
    # Factorized: (x - 3)(x - 2)
    # [3. 2.]
    
    # Quadratic formula: (-b +- sqrt(b^2 - 4ac))/2a
    result = (-b + np.array((1,-1))*sqrt(b**2 - 4*a*c))/(2*a)

    if show:
        eq = '(x + %.4g)'
        print('Factorized: '+ 
              ''.join(map(lambda x: eq%x if x>0 else (eq%x).replace('+ -', '- '),
                          result * -1))
              )
    if equal1:
        result = 1/result * -1 # Return factorized x equations as = 1.
    
    return result

# ---------- Common in Statistics ----------
# Using Numpy for factorial (instead of the commonly used recursion)
factorial = lambda n: np.prod(np.arange(1,n+1))

# Above factorial() vectorized for numpy-arrays
np_factorial = np.vectorize(factorial)

# Sums of factorials upto n (1! + 2! + ... + n!)
factorial_sums = lambda n: sum(np_factorial(np.arange(1,n+1)))

# Find the mean of an array of numbers
mean = lambda numbers: np.mean(numbers)

# Find the mode of an array of numbers
def mode(numbers):
    uniqs = np.unique(numbers, return_counts=True)
    freqs = np.asarray(uniqs).T # Array of number and their count
    most_counts = max(uniqs[-1]) # The highest count (of some number)
    
    # Return Number/s with the highest count
    return freqs[np.where(freqs[:,1] == most_counts)][:,0]
    
    
# Find the median of an array of numbers
median = lambda numbers: np.median(numbers)
