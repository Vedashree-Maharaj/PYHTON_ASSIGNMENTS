import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (accuracy_score,
                             confusion_matrix,
                             classification_report)
                             


def BreastCanser(Filename):
   border = "-"*80
   print(border)
   #--------------------------------------------
      # Step  1: Load the dataset
   #--------------------------------------------
   df = pd.read_csv(Filename)
   print("First 5 entries:")
   print(df.head())
   print("Shape of Dataset:",df.shape)

   #--------------------------------------------
   # Step 2: Preprocessing
   #--------------------------------------------
   print(border)

   print("Find the missing values:")
   print(df.isnull().sum())

   X = df.drop("target",axis=1)
   Y = df["target"]

   print("X shape",X.shape)
   print("Y shape",Y.shape)
   print(border)
   #--------------------------------------------
   # Step 3: seprate the features and label
   #--------------------------------------------
   
   X_train,X_test,Y_train,Y_test = train_test_split(
                        X,
                        Y,
                        test_size=0.5,
                        random_state=42
   )

   print("X_train",X_train.shape)
   print("X_test",X_test.shape)
   print(border)
   #------------------------------------------------
   # Step 4: Build the model
   #--------------------------------------------

   model = DecisionTreeClassifier()
   print("Model build succesfully..")
   print(border)
   #------------------------------------------------
   # Step 5: Train the model
   #--------------------------------------------
   
   model = model.fit(X_train,Y_train)
   print("Model train succesfully")

   #------------------------------------------------
   # Step 6: Test the model
   #--------------------------------------------
   """new_sample = np.array([
    12.83,15.73,82.89,506.9,0.0904,0.08269,0.05835,0.03078,0.1705,	0.05913,	0.1499,	0.4875,	1.195,	11.64,	0.004873,	0.01796,	0.03318,	0.00836,	0.01601,	0.002289,	14.09,	19.35,	93.22,	605.8,	0.1326,	0.261,	0.3476,	0.09783,	0.3006,	0.07802

]).reshape(1, -1)"""
   Y_pred = model.predict(X_test)

   print("Actual ans:")
   print(X_test)

   print("Predicted ans:")
   print(Y_pred)

   print("Accuracy is:")
   accuracy = accuracy_score(Y_test,Y_pred)
   print(accuracy)

   print("Confusion matrix:")
   print(confusion_matrix(Y_test,Y_pred))



def main():
   datapath = "breast_cancer.csv"
   BreastCanser(datapath)


if __name__ == "__main__":
  main()s
