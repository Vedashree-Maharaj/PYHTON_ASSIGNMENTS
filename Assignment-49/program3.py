import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

data = [[25,20000],
        [30,40000],
        [35,40000]]

scaler = StandardScaler()

scaler.fit(data)   # learn mean + std

scaled_data = scaler.transform(data)  # Apply scaling

scaled_data = scaler.fit_transform(data)  # Step 1 + step 2 togethers

print(scaled_data)