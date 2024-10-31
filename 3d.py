import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.axis('off')  # Turn off the axis for a clean look

# Generate data for the kaleidoscope pattern
x = np.linspace(-2 * np.pi, 2 * np.pi, 400)
y = np.linspace(-2 * np.pi, 2 * np.pi, 400)
X, Y = np.meshgrid(x, y)
Z = np.sin(X**2 + Y**2)

# Initialize the plot
img = ax.imshow(Z, cmap='hsv', interpolation='bilinear')

# Update function for the animation
def update(frame):
    # Create a morphing effect by shifting the wave patterns
    Z = np.sin(X**2 + Y**2 + frame * 0.1) * np.cos(X**2 - Y**2 + frame * 0.1)
    img.set_array(Z)
    img.set_cmap(plt.cm.get_cmap('twilight', 256))  # Change colors dynamically
    return [img]

# Create animation
ani = FuncAnimation(fig, update, frames=200, interval=50, blit=True)

# Show the animated kaleidoscope illusion
plt.show()
