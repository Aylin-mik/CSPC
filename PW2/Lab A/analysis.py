import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

# TODO 1: read freefall.csv into arrays t and y
#         (hint: np.loadtxt with a comma delimiter, skipping the header)
data = np.loadtxt("freefall.csv", delimiter = ",", skiprows = 1)
t = data[:, 0]
y = data[:, 1]
# TODO 2: compute velocity v = derivative of y w.r.t. t   (np.gradient)
#         and acceleration a = derivative of v w.r.t. t    (np.gradient again)
#         Print the mean acceleration. Is it close to -9.81? Is it noisy?
v = np.gradient(y,t)
a= np.gradient(v, t)
print("Mean acceleration:", a.mean())
print("Standart deviation:", a.std())
# TODO 3: integrate a back up to recover velocity and position
#         (hint: cumulative_trapezoid(a, t, initial=0) + v[0], then again)
vel = cumulative_trapezoid(a, t, initial = 0) + v[0]
pos = cumulative_trapezoid(v, t, initial = 0) + y[0]
max_dif = np.max(np.abs(pos) - y)
print("Largest difference:", max_dif)
# TODO 4: make a figure with 3 stacked panels: position, velocity, acceleration
#         vs time. Mark the true -9.81 line on the acceleration panel.
#         Save it as motion.png
fig, axes = plt.subplots(3, 1, sharex=True)

axes[0].plot(t, y)
axes[0].set_ylabel("Position (m)")
axes[0].set_title("Motion from free fall data")

axes[1].plot(t, v)
axes[1].set_ylabel("Velocity (m/s)")

axes[2].plot(t, a)
axes[2].axhline(-9.81, linestyle="--", label="g = -9.81")
axes[2].set_ylabel("Acceleration (m/s^2)")
axes[2].set_xlabel("Time (s)")
axes[2].legend()

plt.tight_layout()
plt.savefig("motion.png")