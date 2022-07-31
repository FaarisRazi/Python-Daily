# Handy functions for Statistics to be added InshaAllah!

# (Import functions from repo-directory: Python-Daily/School Kit/Maths/mymaths.py)
from mymaths import nCr, nPr, factorial

# HyperGeometric Distribution formula
hypergeo = lambda N, Ns, n, x: ( nCr(Ns,x) * nCr(N-Ns,n-x) ) / nCr(N,n) 
