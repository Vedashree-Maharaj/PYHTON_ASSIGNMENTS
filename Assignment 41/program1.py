import pandas as pd
import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.preprocessing import StandardScaler

def MarvellousClassifier(DataPath):
    border ="-"*50

    # Step 1 : Load the dataset from CSV file
    print(border)
    print("Step 1 : Load the dataset from CSV file")
    print(border)

    df = pd.read_csv(DataPath)

    print(border)
    print("Some entries from dataset")
    print(df.head())
    print(border)

    # Step 2 : Clean the Dataset
    print(border)
    print("Step 2 : Clean the Dataset")
    print(border)

    df.dropna(inplace=True) # Removes missing values

    print("Shape of dataset :",df.shape)
    print("Total Records :",df.shape[0])
    print("Total Columns :",df.shape[1])

    print(border)

    # Step 3 : Separate Dependent and Independent Variables
    print(border)
    print("Step 3 : Separate Dependent and Independent Variables")
    print(border)

    X = df.drop(columns=['Class']) # exclude 'Class' and save all in X
    Y = df['Class']

    print("Shape of X:",X.shape)
    print("Shape of Y :",Y.shape)

    print(border)
    print("Input Columns :",X.columns.tolist())
    print("Output Column : Class")
    print(border)

    # Step 4 : Split the dataset for training and testing
    print(border)
    print("Step 4 : Split the dataset for training and testing")
    print(border)

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.5,random_state=42,stratify=Y)

    print(border)
    print("Details of training and teating data")

    print("Shape of X_train  :",X_train.shape)
    print("Shape of X_test  :",X_test.shape)
    print("Shape of Y_train  :",Y_train.shape)
    print("Shape of Y_test  :",Y_test.shape)

    print(border)

    # Step 5 : Feature scaling
    print(border)
    print("Step 5 : Feature scaling")
    print(border)

    scalar = StandardScaler()
    X_train_scale = scalar.fit_transform(X_train)
    X_test_scale = scalar.fit_transform(X_test)

    print("Feature scaling is done")

    print(border)

    # Step 6 : Build the model
    print(border)
    print("Step 6 : Build the model")
    print(border)

    model = KNeighborsClassifier(n_neighbors=9)

    print("Classification model is created")

    # Step 7 : Train the model
    print(border)
    print("Step 7 : Train the model")
    print(border)

    model = model.fit(X_train_scale,Y_train)

    print("Model train completed")

    print(border)

    # Step 8 : Test the model
    print(border)
    print("Step 8 : Test the model")
    print(border)

    Y_pred = model.predict(X_test_scale)

    accuracy = accuracy_score(Y_test,Y_pred)

    print("Model Accuracy is :",accuracy*100)
def main():
    MarvellousClassifier("WinePredictor.csv")

if __name__ =="__main__":
    main()