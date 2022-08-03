# Physics Formulae/Functions to be added InshaAllah

# ------------------ Kinematics ------------------
# Final Velocity (a = acceleration, v0 = Initial Velocity, x = displacement, t = time)
vf_0at = lambda v0,a,t: v0 ± a*t # (with only v0, a, t)
vf_0xt = lambda v0,x,t: 2*x/t - v0 # (with only v0, x, t)
vf_0ax = lambda v0,a,x: sqrt(v0**2 + 2*a*x) # (with only v0, a, x)

xdis = lambda v0,a,t: v0*t ± 0.5*a*t**2 # Displacement
