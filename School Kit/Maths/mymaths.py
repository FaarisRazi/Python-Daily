import numpy as np
from math import *
from fractions import Fraction

# Convert a decimal number to a fraction (smallest/largest ratio):
fraction = lambda x, lowest=True: Fraction(x).limit_denominator() if lowest else '%d/%d'%(x.as_integer_ratio())

# Convert list/tuple into array of numbers
vector = lambda lst: np.array(lst) # set/dict will be 0-dimensional arrays

# Sum numbers from a starting number (default start = 0) upto a final (x).
#(Known as "Triangular number": https://en.wikipedia.org/wiki/Triangular_number)
sumfrom = lambda x, start=0: (x**2 + x)//2 - (start**2 + start)//2

# Check if a number is Prime (else it is Composite).
def is_prime(n):
    # Fastest algorithm from: geekflare.com/prime-number-in-python/
    for i in range(2, int(sqrt(n))+1):
        if n%i:
            return True
    return False

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

# ---------- Geometry Functions ----------
torad = lambda x_degree: x_degree * pi/180 # "radians" is available in the math-library
todegree = lambda x_rad: x_rad * 180/pi # Convert some x degrees to radian form. 

# Pythogarus Theorum (c^2 = a^2 + b^2)
def pythogarus(show=True, c=False, **kwargs):
    # Pass any two parameters with their values, examples with formula equivalence:
    # pythogarus(a=1, b=2) gives:           sqrt(a^2 + b^2), traditional way of finding c.
    # pythogarus(g=3, h=4, c=True):         sqrt(h^2 - g^2), c = True: sqrt((largest value)^2 - (smallest value)^2)

    comment = 'sqrt( %.4g^2 + %.4g^2 ) = %.4g'

    if len(kwargs) == 2:

        smaller, bigger = sorted(kwargs, key=kwargs.get)
        y, x = kwargs[bigger], kwargs[smaller]
        inner = y**2 + x**2
        
        if c:
            inner -= 2*(x**2)
            comment = comment.replace('+','-')
    
        if show:
            print(comment % (y, x, inner**0.5))

        return inner**0.5
 

# ---------- Common in Statistics ----------
# Using Numpy for factorial (instead of recursion or the math library)
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

# Getting the Standard Deviation and Variance of numbers:
stdev = lambda numbers: np.std(numbers)
variance = lambda numbers: stdev(numbers)**2

# Permutations for "r" number of objects from a total of "n" number of objects
nPr = lambda n, r, rep=False: factorial(n) / factorial(n-r) if not rep else n**r

# Combinations of "r" number of objects chosen from "n" number of objects
nCr = lambda n, r: nPr(n,r) * 1/factorial(r)
