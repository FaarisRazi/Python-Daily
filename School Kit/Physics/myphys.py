# Physics Formulae/Functions to be added InshaAllah
from math import sqrt

# ------------------ 1D Kinematics ------------------
#(vf = Final Velocity, v0 = Initial Velocity, a = acceleration, 
# x = displacement, t = time)

# Final Velocity
vf_0at = lambda v0,a,t: v0 ± a*t 
vf_0xt = lambda v0,x,t: 2*x/t - v0
vf_0ax = lambda v0,a,x: sqrt(v0**2 + 2*a*x)

# Initial Velocity
v0_fat = lambda vf,a,t: vf - a*t
v0_fxt = lambda vf,x,t: 2*x/t - vf
v0_fax = lambda vf,a,x: sqrt(vf**2 - 2*a*x)

# Displacement
x_v0at = lambda v0, a, t: v0*t ± 0.5*a*t**2
x_v0ft = lambda v0, vf, t: 0.5*(v0 + vf)*t
x_v0fa = lambda v0, vf, a: 0.5*(vf**2 - v0**2)/a

# Time
t_v0fa = lambda v0, vf, a: (v - v0)/a
t_v0fx = lambda v0, vf, x: 2*x / (v0 + v)

# Acceleration
a_v0ft = lambda v0, vf, t: (v - v0)/t
a_v0xt = lambda v0, x, t: 2*(x - v0*t)/t**2)
a_v0fx = lambda v0, vf, x: 0.5*(vf**2 - v0**2)/x

# ------------------ 2D Kinematics ------------------
a_g = 9.8 # Acceleration due to gravity.
a_xproj, a_yproj = 0, -g # Accelerations (x and y) at projectile.

# Velocity from it's vector sum of x and y components in projectile.
def vf_proj(v0x, vy, peak=False):
    if peak:
        vy = 0
    return sqrt(v0x**2 + vy**2)
