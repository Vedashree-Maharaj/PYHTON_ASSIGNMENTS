import tensorflow as tf

# Take user input
x = float(input("Enter input: "))
weight = float(input("Enter weight: "))
bias = float(input("Enter bias: "))
target = float(input("Enter target output: "))
learning_rate = float(input("Enter learning rate: "))

# Convert to TensorFlow tensors
x = tf.constant(x)
weight = tf.constant(weight)
bias = tf.constant(bias)
target = tf.constant(target)
learning_rate = tf.constant(learning_rate)

# Calculate prediction
prediction = x * weight + bias

# Calculate error
error = target - prediction

# Calculate gradient
gradient = -2 * x * error

# Store old weight
old_weight = weight

# Update weight using gradient descent
new_weight = weight - learning_rate * gradient

# Display results
print("\n------------------------------")
print("Prediction     :", prediction.numpy())
print("Error          :", error.numpy())
print("Gradient       :", gradient.numpy())
print("Old Weight     :", old_weight.numpy())
print("Updated Weight :", new_weight.numpy())
print("------------------------------")