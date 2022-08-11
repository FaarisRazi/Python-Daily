import numpy as np
from math import *

# ---------- Geometry Functions ----------
torad = lambda x_degree: x_degree * pi/180 # "radians" is available in the math-library
todegree = lambda x_rad: x_rad * 180/pi # Convert some x degrees to radian form. 

# Finding angles (theta) for right-angled triangles:
soh = lambda opp, hyp: asin(opp/hyp) # Sin-method (when only 'opposite' and 'hypotenuse' are available)
cah = lambda adj, hyp: acos(adj/hyp) # Cosine-method (when 'adjacent' and 'hypotenuse' are available)
toa = lambda opp, adj: atan(opp/adj) # Tan-method (when 'opposite' and 'adjacent' available)

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
