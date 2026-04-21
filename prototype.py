import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

# Create grid
x = np.linspace(-5, 5, 25)
y = np.linspace(-5, 5, 25)
X, Y = np.meshgrid(x, y)

# Traffic flow model
def field(x, y):
    u = -x * np.exp(-x**2 - y**2)
    v = -y * np.exp(-x**2 - y**2)
    return u, v

U, V = field(X, Y)

# Compute divergence
dU_dx = np.gradient(U, axis=1)
dV_dy = np.gradient(V, axis=0)
divergence = dU_dx + dV_dy

# Compute curl
dV_dx = np.gradient(V, axis=1)
dU_dy = np.gradient(U, axis=0)
curl = dV_dx - dU_dy

# Create plot
fig, ax = plt.subplots(figsize=(6,6))
plt.subplots_adjust(bottom=0.2)

# Default plot
quiver = ax.quiver(X, Y, U, V)
ax.set_title("Traffic Vector Field")

# Functions for buttons
def show_vector(event):
    ax.clear()
    ax.quiver(X, Y, U, V)
    ax.set_title("Traffic Flow Vector Field")
    plt.draw()

def show_div(event):
    ax.clear()
    ax.contourf(X, Y, divergence)
    ax.set_title("Divergence (Congestion)")
    plt.draw()

def show_curl(event):
    ax.clear()
    ax.contourf(X, Y, curl)
    ax.set_title("Curl (Rotation)")
    plt.draw()

# Buttons
ax_vec = plt.axes([0.1, 0.05, 0.2, 0.075])
ax_div = plt.axes([0.4, 0.05, 0.2, 0.075])
ax_curl = plt.axes([0.7, 0.05, 0.2, 0.075])

btn_vec = Button(ax_vec, 'Vector Field')
btn_div = Button(ax_div, 'Divergence')
btn_curl = Button(ax_curl, 'Curl')

btn_vec.on_clicked(show_vector)
btn_div.on_clicked(show_div)
btn_curl.on_clicked(show_curl)

plt.show()