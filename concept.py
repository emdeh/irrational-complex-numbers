import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters for the circular motion
r = 1.0           # Radius
omega = 2 * np.pi # Angular velocity (one revolution per second)

# Initialize the figure and axis
fig, ax = plt.subplots()
line, = ax.plot([], [], 'bo', ms=10)  # 'bo' creates a blue circle marker
ax.set_xlim(-1.5 * r, 1.5 * r)
ax.set_ylim(-1.5 * r, 1.5 * r)

# Initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,

# Animation function: this is called sequentially
def animate(t):
    x = r * np.cos(omega * t)
    y = r * np.sin(omega * t)
    line.set_data(x, y)
    return line,

# Call the animator
ani = FuncAnimation(fig, animate, init_func=init, frames=np.linspace(0, 2*np.pi, 128), interval=20, blit=True)

plt.show()
