# Handy functions for Statistics to be added InshaAllah!

# (Import functions from repo-directory: Python-Daily/School Kit/Maths/mymaths.py)
from mymaths import nCr, nPr, factorial

# Sum-range handler function for the distribution formulae below
def distrange(x, sumto):
    if sumto == True:
        sumto = range(x+1)

    elif isinstance(sumto, (range, list, tuple, set, dict)):
        start, end = min(sumto), max(sumto)+1
        sumto = range(start, end)
    
    elif sumto and not isinstance(sumto, bool):
        raise ValueError('Invalid sumto input, please use a range or collection of numbers.')
    
    return sumto
        
# HyperGeometric Distribution
def hypergeo(N, Ns, n, x, sumto=False): 
  formula = lambda x: ( nCr(Ns,x) * nCr(N-Ns,n-x) ) / nCr(N,n)
  
  return formula(x) if not sumto else sum(map(formula, distrange(sumto)))

# Geometric Distribution
def geometric(p, x, sumto=False):
  formula = lambda x: p * (1-p)**(x-1)
  
  return formula(x) if not sumto else sum(map(formula, distrange(sumto)))


# Possion Distribution
def pois(x, lamda, sumto=False):
  formula = lambda x: (lamda**x)/factorial(x) * e**-lamda
  
  return formula(x) if not sumto else sum(map(formula, distrange(sumto)))
