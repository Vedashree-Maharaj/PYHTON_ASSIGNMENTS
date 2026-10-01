import tensorflow as tf

border = "-"*80

inputs = tf.constant([2.0,3.0])

weights = tf.constant([0.4,0.6])

bias = tf.constant(0.5)

weights = tf.reduce_sum(inputs * weights) + bias
output = tf.sigmoid(weights)


print(border)
print("Weighted sum:",weights)
print("Sigmoid:",output)
print(border)


# From the code the Output is near to 1

# OR
"""
import numpy as np
import math

def Sigmoid(z):
  return 1/(1+math.exp(-z))
X1 = 2
X2 = 3
W1 = 0.4
W2 = 0.6
bias = 0.5

weightded_sum = (W1 * X1  + W2 * X2  + bias)

sigmoid1 = Sigmoid(weightded_sum)


"""