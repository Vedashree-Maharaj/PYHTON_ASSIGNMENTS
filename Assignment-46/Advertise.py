import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score

def AdvertiseCase(filename):
  border = "-"*70

  print(border)
  print("Step 1 : Load the Data")
  df = pd.read_csv(filename)
  print(df.head())
  print(border)

################################################
  print("Step 2 : Clean Prepare and manipulate the data")

  if "Unnamed: 0" in df.columns:
    df = df.drop(columns=["Unnamed: 0"])
  print(df.head())

  print(border)
  print("Check Missing values:")
  print(df.isnull().sum())
  print(border)
##################################################

  print("Step 3:Statistical report:")
  print(df.describe())
  print(border)

  ##########################################
  print("Step 4 : Seprate Independent and Dependent variable")

  X = df[["TV","radio","newspaper"]]
  Y = df["sales"]

  print("shape of X",X.shape)
  print("shape of Y",Y.shape)

  print("Independent Variables:")
  print(X.head())

  print("Dependent Variable:")
  print(Y.head())
  print(border)
##################################################

  print("Step 5 : Split the dataset")

  X_train,X_test,Y_train,Y_test = train_test_split(
    X,
    Y,
    test_size= 0.2,
    random_state=42
  )

  print("X_train:",X_train.shape)
  print("X_test:",X_test.shape)

  print("Y_train:",Y_train.shape)
  print("Y_test:",Y_test.shape)
  print(border)
##################################################
  
  print("Step 6 : Create the model")

  Model = LinearRegression()

  print("Model created succesfully..")

  print(border)

##################################################
  
  print("Step 7 : Train the model")

  Model = Model.fit(X_train,Y_train)

  print("Model trained succesfully")

###############################################
  print("Step 8 : Test the model")

  Y_pred = Model.predict(X_test)

  print("Accurate ans:")
  print(Y_test[:3])

  print("Predicted ans:")
  print(Y_pred[:3])

 ###############################################

  print("Step 9 : Evaluate the model")

  mrc = mean_squared_error(Y_test,Y_pred)

  rmsc = np.sqrt(mrc)

  r2 = r2_score(Y_test,Y_pred)

  print("MSC : ",mrc)
  print("RMSC :",rmsc)
  print("R2 : ",r2)

  




def main():
 AdvertiseCase("Advertising.csv")


if __name__ == "__main__":
  main()
