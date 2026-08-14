import pandas as pd

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler

border = "-" * 50


def MarvellousClassifier(DataPath):

    # Step 1 : Load the dataset from CSV file
    print(border)
    print("Step 1 : Load the dataset from CSV file")
    print(border)

    df = pd.read_csv(DataPath)

    print("Some entries from dataset")
    print(df.head())

    # Step 2 : Clean the Dataset
    print(border)
    print("Step 2 : Clean, Prepare and Manipulate Data")
    print(border)

    df.dropna(inplace=True)

    # Convert categorical values into numerical values
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

    print("Shape of dataset :", df.shape)
    print("Total Records :", df.shape[0])
    print("Total Columns :", df.shape[1])

    # Step 3 : Separate Independent and Dependent variables
    print(border)
    print("Step 3 : Separate Dependent and Independent Variables")
    print(border)

    X = df[["Wether", "Temperature"]]
    Y = df["Play"]

    print("Shape of X :", X.shape)
    print("Shape of Y :", Y.shape)

    print("Input Columns :", X.columns.tolist())
    print("Output Column : Play")

    # Step 4 : Split dataset
    print(border)
    print("Step 4 : Split the dataset for training and testing")
    print(border)

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.5,
        random_state=42,
        stratify=Y
    )

    print("Shape of X_train :", X_train.shape)
    print("Shape of X_test :", X_test.shape)
    print("Shape of Y_train :", Y_train.shape)
    print("Shape of Y_test :", Y_test.shape)

    # Feature Scaling
    print(border)
    print("Feature Scaling")
    print(border)

    scaler = StandardScaler()

    X_train_scale = scaler.fit_transform(X_train)
    X_test_scale = scaler.transform(X_test)

    print("Feature scaling is done")

    # Step 5 : Train the KNN model
    print(border)
    print("Step 5 : Train the KNN Model")
    print(border)

    model = KNeighborsClassifier(n_neighbors=3)

    model.fit(X_train_scale, Y_train)

    print("Model training completed")

    # Test the model
    print(border)
    print("Testing the Model")
    print(border)

    Y_pred = model.predict(X_test_scale)

    print("Actual Values    :", Y_test.tolist())
    print("Predicted Values :", Y_pred.tolist())

    # Step 6 : Calculate Accuracy
    print(border)
    print("Step 6 : Calculate Accuracy")
    print(border)

    accuracy = accuracy_score(Y_test, Y_pred)

    print("Accuracy of KNN Model :", accuracy * 100, "%")

    # Confusion Matrix
    print(border)
    print("Confusion Matrix")
    print(border)

    cm = confusion_matrix(Y_test, Y_pred)

    print(cm)

    # Prediction for new data
    print(border)
    print("Prediction for New Data")
    print(border)

    # Example:
    # Sunny = 0
    # Overcast = 1
    # Rainy = 2
    #
    # Hot = 0
    # Mild = 1
    # Cool = 2

    Weather = 0
    Temperature = 1

    new_data = [[Weather, Temperature]]

    new_data_scaled = scaler.transform(new_data)

    result = model.predict(new_data_scaled)

    if result[0] == 1:
        print("Prediction : Yes")
    else:
        print("Prediction : No")

    print(border)
    print("Accuracy for different K values")
    print(border)

    for k in range(1, 8):

        model = KNeighborsClassifier(n_neighbors=k)

        model.fit(X_train, Y_train)

        Y_pred = model.predict(X_test)

        accuracy = accuracy_score(Y_test, Y_pred)

        print("K =", k, "Accuracy =", accuracy * 100, "%")
def main():

    MarvellousClassifier("MarvellousInfosystems_PlayPredictor.csv")


if __name__ == "__main__":
    main()
