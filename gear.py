import numpy as np # type: ignore
import pandas as pd # type: ignore
from sklearn.model_selection import train_test_split # type: ignore
from sklearn.ensemble import RandomForestRegressor # type: ignore
from sklearn.metrics import mean_squared_error # type: ignore

# Sample dataset (hypothetical features and target variable)
data = {
    'gear_diameter': np.random.uniform(50, 500, 1000),  # in mm
    'num_teeth': np.random.randint(20, 200, 1000),
    'material_strength': np.random.uniform(200, 800, 1000),  # in MPa
    'speed': np.random.uniform(100, 3000, 1000),  # in RPM
    'load': np.random.uniform(10, 1000, 1000),  # in N
    'torque': np.random.uniform(10, 500, 1000),  # in Nm
    'temperature': np.random.uniform(20, 200, 1000),  # in Celsius
    'wear_rate': np.random.uniform(0.01, 0.2, 1000)  # target variable (hypothetical)
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Features (X) and target (y)
X = df.drop(columns=['wear_rate'])
y = df['wear_rate']
# New real-time data for a specific gear
new_gear_data = np.array([[200, 50, 600, 1500, 300, 200, 100]])  # Example input

import streamlit as st
import numpy as np
import joblib  # For loading a trained model
import pandas as pd

# Function to simulate wear rate prediction (replace with your model)
def predict_wear_rate(radius, num_teeth, material_strength, speed, load, torque, temperature):
    # Placeholder for a trained model prediction
    # This function should load your model and return a prediction
    # Example using a mock formula: wear_rate = f(radius, num_teeth, ...) (replace with actual model)
    return (
        0.1 * radius +
        0.05 * num_teeth +
        0.02 * material_strength +
        0.01 * speed +
        0.003 * load +
        0.005 * torque -
        0.1 * temperature
    )

# Streamlit layout
st.title("Wear Rate Prediction for Spur Gears")

# User inputs
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



# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse:.4f}")

    

   
