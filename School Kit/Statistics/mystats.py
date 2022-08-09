# Handy functions for Statistics to be added InshaAllah!

# (Import functions from repo-directory: Python-Daily/School Kit/Maths/mymaths.py)
from mymaths import nCr, nPr, factorial

# HyperGeometric Distribution
hypergeo = lambda N, Ns, n, x: ( nCr(Ns,x) * nCr(N-Ns,n-x) ) / nCr(N,n)

# Geometric Distribution
def geometric(p, x, sumto=False):
  return p * (1-p)**(k-1) if not sumto else p * sum([(1-p)**(k-1) for k in range(1,x+1)])
