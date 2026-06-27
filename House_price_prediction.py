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