import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Function to simulate wear rate prediction
def predict_wear_rate(radius, num_teeth, material_strength, speed, load, torque, temperature):
    return (
        0.1 * radius +
        0.05 * num_teeth +
        0.02 * material_strength +
        0.01 * speed +
        0.003 * load +
        0.005 * torque -
        0.1 * temperature
    )

# Function to draw a spur gear
def draw_gear(ax, radius, thickness, num_teeth, angle):
    theta = np.linspace(0, 2 * np.pi, num_teeth + 1)
    x_outer = radius * np.cos(theta + angle)
    y_outer = radius * np.sin(theta + angle)

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

    ax.bar3d(x_outer, y_outer, 0, 0.1, 0.1, thickness, shade=True, color='gray')

# Streamlit layout
st.title("Animated Spur Gears Based on Predicted Wear Rate")

# User inputs for gear parameters
radius = st.slider("Gear Radius (mm)", 1, 500, 200)
num_teeth = st.slider("Number of Teeth", 5, 200, 50)
material_strength = st.slider("Material Strength (MPa)", 200, 800, 600)
speed = st.slider("Speed (RPM)", 100, 3000, 1500)
load = st.slider("Load (N)", 10, 1000, 300)
torque = st.slider("Torque (Nm)", 10, 500, 100)
temperature = st.slider("Temperature (°C)", 20, 200, 100)

# Predict wear rate
if st.button("Predict Wear Rate"):
    wear_rate = predict_wear_rate(radius, num_teeth, material_strength, speed, load, torque, temperature)
    st.success(f"Predicted Wear Rate: {wear_rate:.4f} (arbitrary units)")

    # Setup the figure and 3D axis for animation
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Animation function
    def animate(frame):
        ax.clear()
        angle = frame * (wear_rate / 10)  # Adjust rotation speed based on wear rate
        draw_gear(ax, radius, 1.0, num_teeth, angle)  # Thickness fixed for simplicity
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



    

   
