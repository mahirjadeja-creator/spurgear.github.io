import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time

# Function to draw a spur gear
def draw_gear(ax, radius, thickness, num_teeth, angle):
    # Create gear outline
    theta = np.linspace(0, 2 * np.pi, num_teeth + 1)
    x_outer = radius * np.cos(theta + angle)
    y_outer = radius * np.sin(theta + angle)

    # Teeth coordinates
    tooth_height = 0.2
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

    # Draw gear thickness
    ax.bar3d(x_outer, y_outer, 0, 0.1, 0.1, thickness, shade=True, color='gray')

# Streamlit layout
st.title("Real-Time Animation of Spur Gears")

# User inputs for gear parameters
radius = st.slider("Gear Radius (mm)", 1, 500, 100)
thickness = st.slider("Gear Thickness (mm)", 0.1, 10.0, 1.0)
num_teeth = st.slider("Number of Teeth", 5, 100, 20)

# Create a placeholder for the figure
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Animation loop
angle = 0
while True:
    ax.clear()
    draw_gear(ax, radius, thickness, num_teeth, angle)
    ax.set_title("3D Animation of Spur Gears")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_xlim([-600, 600])
    ax.set_ylim([-600, 600])
    ax.set_zlim([0, 10])
    ax.view_init(elev=30, azim=angle)

    # Update the angle for rotation
    angle += 0.1  # Rotation speed
    if angle >= 360:
        angle = 0

    # Display the updated plot
    st.pyplot(fig)

    # Pause for a moment to create animation effect
    time.sleep(0.05)  # Adjust this for speed of rotation





    

   
