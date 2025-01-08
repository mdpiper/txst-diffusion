import numpy as np
import matplotlib.pyplot as plt


def calculate_time_step(grid_spacing, diffusivity):
    return 0.5 * grid_spacing**2 / diffusivity


D = 100  # diffusivity
Lx = 300 # domain size

dx = 0.5
x = np.arange(start=0, stop=Lx, step=dx)
nx = len(x)

C = np.zeros_like(x)
C_left = 500
C_right = 0
C[x <= Lx//2] = C_left
C[x > Lx//2] = C_right

plt.figure()
plt.plot(x, C, "r")
plt.xlabel("x")
plt.ylabel("C")
plt.title("Initial concentration profile")

time = 0
nt = 5000
dt = calculate_time_step(dx, D)

for t in range(0, nt):
    C += D * dt / dx**2 * (np.roll(C, -1) - 2*C + np.roll(C, 1))
    C[0] = C_left
    C[-1] = C_right

plt.figure()
plt.plot(x, C, "b")
plt.xlabel("x")
plt.ylabel("C")
plt.title("Final concentration profile")
