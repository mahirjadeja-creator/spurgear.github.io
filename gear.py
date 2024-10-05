
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Function to draw a spur gear
def draw_gear(ax, radius, thickness, num_teeth, angle):
    # Create a gear outline
    theta = np.linspace(0, 2 * np.pi, num_teeth + 1)
    x_outer = radius * np.cos(theta + angle)
    y_outer = radius * np.sin(theta + angle)

    # Teeth coordinates
    tooth_height = 0.1
    for i in range(num_teeth):
        x_tooth = [
            x_outer[i], 
            x_outer[i] * 0.8, 
            x_outer[i] * 0.8, 
            x_outer[i], 
            x_outer[i] * 1.1,
            x_outer[i] * 1.1,
            x_outer[i],
        ]
        y_tooth = [
            y_outer[i], 
            y_outer[i], 
            y_outer[i] + tooth_height, 
            y_outer[i] + tooth_height, 
            y_outer[i],
            y_outer[i] - tooth_height,
            y_outer[i] - tooth_height,
        ]
        ax.plot(x_tooth, y_tooth, zs=[0, 0, 0, 0, 0, 0, 0], color='black')

    # Gear thickness
    ax.bar3d(x_outer, y_outer, 0, 0.1, 0.1, thickness, shade=True, color='gray')

# Streamlit layout
st.title("Real-time 3D Animation of Spur Gears")

# Parameters
radius = st.slider("Gear Radius", 1, 10, 5)
thickness = st.slider("Gear Thickness", 0.1, 5.0, 1.0)
num_teeth = st.slider("Number of Teeth", 5, 50, 20)

# Setup the figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Animation function
def animate(frame):
    ax.clear()
    angle = frame * 0.1  # Adjust rotation speed
    draw_gear(ax, radius, thickness, num_teeth, angle)
    ax.set_title("3D Animation of Spur Gears")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_xlim([-15, 15])
    ax.set_ylim([-15, 15])
    ax.set_zlim([0, 10])
    ax.view_init(elev=30, azim=frame)

# Create an animation
ani = FuncAnimation(fig, animate, frames=np.arange(0, 360), interval=50)

# Display the animation in Streamlit
st.pyplot(fig)
