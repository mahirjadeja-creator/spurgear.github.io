import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

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
