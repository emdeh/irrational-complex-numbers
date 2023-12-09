import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters for the circular motions
r1 = 2.0  # Radius of the first circle
r2 = 2.0  # Radius of the second circle
omega1 = np.pi / 2  # Angular velocity of the first circle
omega2 = np.pi / 2  # Angular velocity of the second circle

# Initialize the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black') 
line, = ax.plot([], [], 'w', lw=1)  # 'o-' creates a line with circle markers
trace, = ax.plot([], [], 'w', lw=1)  # Trace line
ax.set_xlim(-2 * (r1 + r2), 2 * (r1 + r2))
ax.set_ylim(-2 * (r1 + r2), 2 * (r1 + r2))

# Store the trace of the pendulum
x_trace, y_trace = [], []

# Initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    trace.set_data([], [])
    return line,

# Animation function: this is called sequentially
def animate(t):
    # Position of the first pendulum end
    x1 = r1 * np.cos(omega1 * t)
    y1 = r1 * np.sin(omega1 * t)

    # Position of the second pendulum end relative to the first
    x2 = x1 + r2 * np.cos(omega2 * t)
    y2 = y1 + r2 * np.sin(omega2 * t)

    # Update the pendulum line
    line.set_data([0, x1, x2], [0, y1, y2])

    # Update the trace
    x_trace.append(x2)
    y_trace.append(y2)
    trace.set_data(x_trace, y_trace)

    return line, trace

# Call the animator
ani = FuncAnimation(fig, animate, init_func=init, frames=np.linspace(0, 20, 500), interval=20, blit=True)

plt.show()
