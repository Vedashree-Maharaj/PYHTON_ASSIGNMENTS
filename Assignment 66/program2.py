import tensorflow as tf
import matplotlib.pyplot as plt

border = "-"*80
# Input values from -10 to 10
x = tf.linspace(-10.0, 10.0, 100)

# Activation Functions
sigmoid = tf.sigmoid(x)
relu = tf.nn.relu(x)
tanh = tf.nn.tanh(x)

# Plot
plt.figure(figsize=(10, 6))

plt.plot(x, sigmoid, label="Sigmoid")
plt.plot(x, relu, label="ReLU")
plt.plot(x, tanh, label="Tanh")

plt.xlabel("Input Values")
plt.ylabel("Activation Output")
plt.title("TensorFlow Activation Functions")
plt.grid(True)
plt.legend()

plt.show()

print(border)

print("Sigmoid: Output range is 0 to 1")
print("ReLU: Negative values become 0, positive values remain unchanged")
print("Tanh: Output range is -1 to 1")

print(border)
"""
import numpy as np
import matplotlib.pyplot as plt

# Activation Functions

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximum(0, x)

def tanh(x):
    return np.tanh(x)


# Accept input values from -10 to 10
x = np.linspace(-10, 10, 100)

# Calculate activation function values
y_sigmoid = sigmoid(x)
y_relu = relu(x)
y_tanh = tanh(x)


# Plot activation functions
plt.figure(figsize=(10, 6))

plt.plot(x, y_sigmoid, label="Sigmoid")
plt.plot(x, y_relu, label="ReLU")
plt.plot(x, y_tanh, label="Tanh")

plt.xlabel("Input Values")
plt.ylabel("Activation Output")
plt.title("Activation Functions")
plt.grid(True)
plt.legend()

plt.show()


# Display explanation
print("Sigmoid:")
print("Maps values between 0 and 1.")
print("It is commonly used for binary classification.")

print("\nReLU:")
print("Returns 0 for negative values and x for positive values.")
print("It is widely used in hidden layers of neural networks.")

print("\nTanh:")
print("Maps values between -1 and 1.")
print("It is useful when both positive and negative outputs are required.")
"""