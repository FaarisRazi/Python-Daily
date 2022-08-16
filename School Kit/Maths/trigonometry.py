import numpy as np
from math import *

# ---------- General Geometry Functions ----------
rad = lambda x_degree: x_degree * pi/180 # "radians" is available in the math-library
deg = lambda x_rad: x_rad * 180/pi # Convert some x degrees to radian form. 

# Finding angles (theta) and sides for right-angled triangles:
soh = lambda opp, hyp: asin(opp/hyp) # Sin-method (when only 'opposite' and 'hypotenuse' are available)
cah = lambda adj, hyp: acos(adj/hyp) # Cosine-method (when 'adjacent' and 'hypotenuse' are available)
toa = lambda opp, adj: atan(opp/adj) # Tan-method (when 'opposite' and 'adjacent' available)

opp = lambda theta, side, use_hyp=True: sin(theta)*side if use_hyp else tan(theta)*side # Else: side = Adjacent (adj)
adj = lambda theta, side, use_hyp=True: cos(theta)*side if use_hyp else side/tan(theta) # Else: side = Opposite (opp)


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
    
# ---------- Some Trigonometric Identities ----------
cot = lambda theta: 1/tan(theta) # Or: cos(theta)/sin(theta)
csc = lambda theta: 1/sin(theta)
sec = lambda theta: 1/cos(theta)
sin_2 = lambda theta: 2*sin(theta)*cos(theta) # sin(2*theta) function

def cos_2(theta, use_cos=True, use_sin=True): # cos(2*theta) function
    if (use_cos + use_sin) in {0, 2}:
        return cos(theta)**2 - sin(theta)**2
    
    elif use_cos:
        return 2*cos(theta)**2 - 1
    
    return 1 - 2*sin(theta)**2 # Else use only with sin()

tan_2 = lambda theta: 2*tan(theta)/(1 - tan(theta)**2)

# ---------- Area-finder functions ----------
class triangle:
# To be worked on...
    
    def __init__(self, angle, twin_angle=True, side, twin_sides=True):
        self.angle = angle
        # To be worked on...
    
    def right_angled(self, a, b, c):
        return 
        # To be worked on...
    
right_triangle = lambda base, height: 0.5 * base*height

class isosceles:
    def __init__(self, angle, twin_angle=True, side, twin_sides=True):
        if angle >= 90:
            raise ValueError("Twin-angles cannot be greater than or equal to 90 degrees.")
        
        self.focal_angle = self.twin_angle = angle
        self.focal_side = self.twin_side = side
                
        if twin_angles:
            self.focal_angle = 180 - angle*2
        else:
            self.twin_angle = (180 - angle)/2
            
#         if twin_sides:
#             self.focal_side
