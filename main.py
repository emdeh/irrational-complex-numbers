import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import odeint

# Parameters for the double pendulum
g = 9.81  # Acceleration due to gravity
L1 = 1.0  # Length of the first pendulum
L2 = 1.0  # Length of the second pendulum
m1 = 1.0  # Mass of the first pendulum
m2 = 1.0  # Mass of the second pendulum

# Initial conditions: theta1, theta2, p_theta1, p_theta2
initial_conditions = [np.pi / 2, np.pi / 2, 0, 0]

# Time array
t = np.linspace(0, 20, 500)

# Equations of motion for the double pendulum
def equations(y, t, L1, L2, m1, m2, g):
    theta1, theta2, p1, p2 = y

    # Constants for the equations
    delta = theta2 - theta1
    M = m1 + m2

    # Differential equations for the double pendulum
    theta1_dot = p1 / (m1 * L1**2)
    theta2_dot = p2 / (m2 * L2**2)
    p1_dot = -(M * g * L1 * np.sin(theta1)) - (m2 * L1 * L2 * theta2_dot**2 * np.sin(delta)) - (2 * m2 * L1 * L2 * theta2_dot * theta1_dot * np.sin(delta))
    p2_dot = -(m2 * g * L2 * np.sin(theta2)) + (m2 * L1 * L2 * theta1_dot**2 * np.sin(delta))

    return [theta1_dot, theta2_dot, p1_dot, p2_dot]

# Solve the ODE
solution = odeint(equations, initial_conditions, t, args=(L1, L2, m1, m2, g))

# Extracting the angles
theta1 = solution[:, 0]
theta2 = solution[:, 1]

# Convert to Cartesian coordinates for plotting
x1 = L1 * np.sin(theta1)
y1 = -L1 * np.cos(theta1)
x2 = x1 + L2 * np.sin(theta2)
y2 = y1 - L2 * np.cos(theta2)

# Initialize the figure and axis
fig, ax = plt.subplots()
line, = ax.plot([], [], 'o-', lw=2)  # 'o-' creates a line with circle markers
ax.set_xlim(-2 * (L1 + L2), 2 * (L1 + L2))
ax.set_ylim(-2 * (L1 + L2), 2 * (L1 + L2))

# Initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,

# Animation function: this is called sequentially
def animate(i):
    line.set_data([0, x1[i], x2[i]], [0, y1[i], y2[i]])
    return line,

# Call the animator
ani = FuncAnimation(fig, animate, init_func=init, frames=len(t), interval=20, blit=True)

plt.show()


# Not going to lie - ChatGPT4 helped me with this one...