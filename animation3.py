# same as animation1 but the angular velocity of the second arm is updated based on the number of revolutions of the first arm.

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Golden Ratio
phi = (1 + np.sqrt(5)) / 2

# Parameters
phi = (1 + np.sqrt(5)) / 2  # Golden Ratio
r1, r2 = 1.5, 1.5  # Radii
omega1 = np.pi / 2  # Angular velocity for the first arm
omega2 = phi * omega1  # Angular velocity for the second arm

# Initialize the figure and axis

width = 12 # Specify the width of the figure (in inches)
height = (5/8) * width # Calculate the height based on the width and the 5/8 ratio

# Initialize the figure with custom dimensions
fig, ax = plt.subplots(figsize=(height, width))
ax.set_facecolor('black') 
line, = ax.plot([], [], 'w', lw=1)  # 'o-' creates a line with circle markers
trace, = ax.plot([], [], 'w', lw=1)  # Trace line
ax.set_xlim(-5, 5)
ax.set_ylim(-10, 10)

# Store the trace of the pendulum
x_trace, y_trace = [], []

# Initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    trace.set_data([], [])
    return line,

# Animation function: this is called sequentially
def animate(theta_degrees):
    theta_radians = np.radians(theta_degrees)  # Convert degrees to radians

    # Calculate the number of complete revolutions
    num_revolutions = theta_degrees / 360.0  # 360 degrees in a revolution

    # Update omega1 and omega2 based on the number of revolutions
    omega1 = (np.pi / 2) + (num_revolutions * np.pi)
    omega2 = (phi * omega1) + (num_revolutions * np.pi)

    # Position of the first pendulum end
    x1 = r1 * np.cos(omega1 * theta_radians)
    y1 = r1 * np.sin(omega1 * theta_radians)

    # Position of the second pendulum end relative to the first
    x2 = x1 + r2 * np.cos(omega2 * theta_radians)
    y2 = y1 + r2 * np.sin(omega2 * theta_radians)

    # Update the pendulum line and trace
    line.set_data([0, x1, x2], [0, y1, y2])
    x_trace.append(x2)
    y_trace.append(y2)
    trace.set_data(x_trace, y_trace)

    return line, trace


# Call the animator
ani = FuncAnimation(fig, animate, init_func=init, frames=np.linspace(0, 15000, 5000), interval=30, blit=True)

plt.show()