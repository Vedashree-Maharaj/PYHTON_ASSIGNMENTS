import pandas as pd

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.preprocessing import StandardScaler

border="-"*50
def MarvellousClassifier(DataPath):
    # Step 1 : Load the dataset from CSV file
    print(border)
    print("Step 1 : Load the dataset from CSV file")
    print(border)

    df = pd.read_csv(DataPath)

    print(border)
    print("Some entries from dataset")
    print(df.head())
    print(border)

    # Step 2 : Clean the Dataset and Separate Dependent and Independent Variables
    print(border)
    print("Step 2 : Clean the Dataset and Separate Dependent and Independent Variables")
    print(border)

    df.dropna(inplace=True) # Removes missing values
    
    df.dropna(inplace=True)

    df["Wether"] = df["Wether"].map({
    "Sunny": 0,
    "Overcast": 1,
    "Rainy": 2
})

    df["Temperature"] = df["Temperature"].map({
    "Hot": 0,
    "Mild": 1,
    "Cool": 2
})

    df["Play"] = df["Play"].map({
    "No": 0,
    "Yes": 1
})
    X = df[["Wether", "Temperature"]]
    Y = df["Play"]

    print("Shape of dataset :",df.shape)
    print("Total Records :",df.shape[0])
    print("Total Columns :",df.shape[1])

    print(border)
    print("Step 3 : Separate Dependent and Independent Variables")
    print(border)

    X = df[["Wether","Temperature"]] 
    Y = df['Play']

    print("Shape of X:",X.shape)
    print("Shape of Y :",Y.shape)

    print(border)
    print("Input Columns :",X.columns.tolist())
    print("Output Column : Play")
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
    X_test_scale = scalar.transform(X_test)

    print("Feature scaling is done")

    print(border)

    # Step 6 : Hyper parameter Tuning
    accuracy_scores = []
    K_values = range(1,8)

    for k in K_values:
        model = KNeighborsClassifier(n_neighbors = k)
        model = model.fit(X_train_scale,Y_train)
        Y_pred = model.predict(X_test_scale)
        accuracy = accuracy_score(Y_test,Y_pred)
        accuracy_scores.append(accuracy)

    print("Accuracy report :")
    for no in accuracy_scores:
        print(no)

    print(border)
    
    
def main():
    MarvellousClassifier("MarvellousInfosystems_PlayPredictor.csv")
    
if __name__ =="__main__":
        main()



