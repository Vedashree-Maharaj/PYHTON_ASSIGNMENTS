
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

data = np.array([[25,20000],
        [30,40000],
        [35,40000]])

print("Pick Two Points")

pointA = data[0]
pointB = data[2]

dist_before = np.linalg.norm(pointA-pointB)
print("Euclidian distance before scaling",dist_before)

Standard_Scaler = StandardScaler()
Standard_Scaler = Standard_Scaler.fit_transform(data)

scaledA = data[0]
scaledB = data[2]

dist_after = np.linalg.norm(scaledA-scaledB)
print("Euclidian distance after scaling",dist_after)
