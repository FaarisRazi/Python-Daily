# Physics Formulae/Functions to be added InshaAllah
from math import sqrt

# ------------------ Kinematics ------------------
#(vf = Final Velocity, v0 = Initial Velocity, a = acceleration, 
# x = displacement, t = time)

# Final Velocity
vf_0at = lambda v0,a,t: v0 ± a*t # (with only v0, a, t)
vf_0xt = lambda v0,x,t: 2*x/t - v0 # (with only v0, x, t)
vf_0ax = lambda v0,a,x: sqrt(v0**2 + 2*a*x) # (with only v0, a, x)

# Displacement
x_v0at = lambda v0, a, t: v0*t ± 0.5*a*t**2 (with only, v0, a, t)
x_v0ft = lambda v0, vf, t: 0.5*(v0 + vf)*t (with only, v0, vf, t)
x_v0fa = lambda v0, vf, a: 0.5*a*(vf**2 - v0**2) (with only, v0, vf, a)

# Time
t_v0fa = lambda v0, vf, a: (v - v0)/a
t_v0fx = lambda v0, vf, x: 2*x / (v0 + v)
