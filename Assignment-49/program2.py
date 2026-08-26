import pandas as pd
import numpy as np

print("Write a program that calculate Variance and standard deviation")

data = [6,7,8,9,10,11,12]

mean = np.mean(data)

sumx = 0
for i in data:
  sub = i- mean
  square = sub**2
  sumx = square + sumx
  divide = sumx / len(data)
print("Variance is :",divide)
print("SD is:",np.sqrt(divide))


