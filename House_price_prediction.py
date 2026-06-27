import matplotlib.pyplot as plt

def house_price():
    
    # House size ( square meters)
    size = [50, 70, 90, 110, 130, 150, 170, 190]

    # Number of Bedrooms
    bedrooms = [1, 2, 2, 3, 3, 4, 4, 5]

    # House price (Millions of Php) 
    price = [2.0, 2.8, 3.5, 4.5, 5.2, 6.1, 7.0, 8.3]

    return size, bedrooms, price

# Get Data
x, y, z = house_price()

# Create a 3D figure
fig = plt.figure(figsize=(8, 6))

# Add a 3D Axis
ax = fig.add_subplot(111, projection="3d")

# Plot the Data
ax.scatter(x, y, z, marker="o")

# Add title and labels
ax.set_title("House Size vs Bedrooms vs Price")
ax.set_xlabel("House Size (m^2)")
ax.set_ylabel("Bedrooms")
ax.set_zlabel("Price (Million of Php)")

plt.show()

#------------------------------------

import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def house_price():

    # House size (square meters)
    size = [50, 70, 90, 110, 130, 150, 170, 190]

    # Number of bedrooms
    bedrooms = [1, 2, 2, 3, 3, 4, 4, 5]

    # House price (Million PHP)
    price = [2.0, 2.8, 3.5, 4.5, 5.2, 6.1, 7.0, 8.3]

    return size, bedrooms, price


# Get data
size, bedrooms, price = house_price()

# Prepare the features (X)
X = list(zip(size, bedrooms))

# Target (y)
y = price

# Create the model
model = LinearRegression()


# Train the model
model.fit(X, y)

# Predict a new house
prediction = model.predict([[140, 3]])

print("Predicted Price:", prediction[0], "Million PHP")

# Plot the data
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection="3d")

ax.scatter(size, bedrooms, price, marker="o")

ax.set_title("House Size vs Bedrooms vs Price")
ax.set_xlabel("House Size (m²)")
ax.set_ylabel("Bedrooms")
ax.set_zlabel("Price (Million PHP)")

plt.show()

#----------------------------

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# -----------------------------
# Data
# -----------------------------
size = np.array([50, 70, 90, 110, 130, 150, 170, 190])
bedrooms = np.array([1, 2, 2, 3, 3, 4, 4, 5])
price = np.array([2.0, 2.8, 3.5, 4.5, 5.2, 6.1, 7.0, 8.3])

# -----------------------------
# Prepare features (X) and target (y)
# -----------------------------
X = np.column_stack((size, bedrooms))
y = price

# -----------------------------
# Train the model
# -----------------------------
model = LinearRegression()
model.fit(X, y)

# -----------------------------
# Create a grid for the regression plane
# -----------------------------
size_grid = np.linspace(40, 200, 20)
bed_grid = np.linspace(1, 5, 20)

S, B = np.meshgrid(size_grid, bed_grid)

grid = np.column_stack((S.ravel(), B.ravel()))

# Predict price on the grid
Z = model.predict(grid).reshape(S.shape)

# -----------------------------
# Predict a new house
# -----------------------------
new_house = np.array([[140, 3]])
pred = model.predict(new_house)[0]

print(f"Predicted price for 140 m² and 3 bedrooms: {pred:.3f} Million PHP")

# Print the learned equation
print("\nRegression Equation:")
print(f"Price = ({model.coef_[0]:.4f} × Size)"
      f" + ({model.coef_[1]:.4f} × Bedrooms)"
      f" + ({model.intercept_:.4f})")

# -----------------------------
# 3D Plot
# -----------------------------
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection="3d")

# Actual data
ax.scatter(size, bedrooms, price,
           color="blue",
           s=60,
           label="Training Data")

# Regression plane
ax.plot_surface(S, B, Z,
                alpha=0.5,
                cmap="viridis")

# Predicted point
ax.scatter(140, 3, pred,
           color="red",
           s=100,
           label="Prediction")

# Vertical line from floor to predicted point
ax.plot([140, 140],
        [3, 3],
        [0, pred],
        "k--")

# Labels
ax.set_title("House Price Regression Plane")
ax.set_xlabel("House Size (m²)")
ax.set_ylabel("Bedrooms")
ax.set_zlabel("Price (Million PHP)")

ax.legend()

plt.show()