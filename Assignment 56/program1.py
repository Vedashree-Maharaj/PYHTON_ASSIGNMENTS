import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier, RandomForestClassifier, AdaBoostClassifier, VotingClassifier

border = "-" * 50

# --------------------------------------------------
# Step 1 : Load the Dataset
# --------------------------------------------------
print(border)
print("Step 1 : Load the Dataset")
print(border)

df = pd.read_csv("Fraudulent_Transaction_Detection.csv")
print(df)

# --------------------------------------------------
# Step 2 : Check Missing Values
# --------------------------------------------------
print(border)
print("Step 2 : Check Missing Values")
print(border)

print(df.isnull().sum())

# --------------------------------------------------
# Step 3 : Separate Input and Output Variables
# --------------------------------------------------
print(border)
print("Step 3 : Separate Input and Output Variables")
print(border)

X = df.drop("Fraud", axis=1)
Y = df["Fraud"]

print("Shape of X :", X.shape)
print("Shape of Y :", Y.shape)

# --------------------------------------------------
# Step 4 : Split Dataset into Training and Testing Data
# --------------------------------------------------
print(border)
print("Step 4 : Split Dataset into Training and Testing Data")
print(border)

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.5,
    random_state=42,
    stratify=Y
)

print("Shape of X_train :", X_train.shape)
print("Shape of X_test  :", X_test.shape)
print("Shape of Y_train :", Y_train.shape)
print("Shape of Y_test  :", Y_test.shape)

# --------------------------------------------------
# Step 5 : Train Decision Tree Model
# --------------------------------------------------
print(border)
print("Step 5 : Train Decision Tree Model")
print(border)

Dmodel = DecisionTreeClassifier(max_depth=4,random_state=42)
Dmodel.fit(X_train, Y_train)

print("Decision Tree Model Trained Successfully!")

# --------------------------------------------------
# Step 6 : Train Bagging Classifier
# --------------------------------------------------
print(border)
print("Step 6 : Train Bagging Classifier")
print(border)

Bmodel = BaggingClassifier(n_estimators=5,random_state=42)
Bmodel.fit(X_train, Y_train)

print("Bagging Classifier Trained Successfully!")

# --------------------------------------------------
# Step 7 : Train Random Forest Classifier
# --------------------------------------------------
print(border)
print("Step 7 : Train Random Forest Classifier")
print(border)

Rmodel = RandomForestClassifier(n_estimators=100,max_depth=2,random_state=42)
Rmodel.fit(X_train, Y_train)

print("Random Forest Classifier Trained Successfully!")

# --------------------------------------------------
# Step 8 : Train AdaBoost Classifier
# --------------------------------------------------
print(border)
print("Step 8 : Train AdaBoost Classifier")
print(border)

Amodel = AdaBoostClassifier(learning_rate=0.5,n_estimators=10,random_state=42)
Amodel.fit(X_train, Y_train)

print("AdaBoost Classifier Trained Successfully!")

# --------------------------------------------------
# Step 9 : Train Voting Classifier
# --------------------------------------------------
print(border)
print("Step 9 : Train Voting Classifier")
print(border)

Vmodel = VotingClassifier(
    estimators=[
        ("decision_tree", Dmodel),
        ("bagging", Bmodel),
        ("random_forest", Rmodel),
        ("adaboost", Amodel)
    ],
    voting="hard"
)

Vmodel.fit(X_train, Y_train)

print("Voting Classifier Trained Successfully!")

# --------------------------------------------------
# Step 10 : Evaluate All Models
# --------------------------------------------------
print(border)
print("Step 10 : Evaluate All Models")
print(border)

models = {
    "Decision Tree": Dmodel,
    "Bagging": Bmodel,
    "Random Forest": Rmodel,
    "AdaBoost": Amodel,
    "Voting": Vmodel
}

results = []

for name, model in models.items():

    print(border)
    print(name)
    print(border)

    Y_pred = model.predict(X_test)

    accuracy = accuracy_score(Y_test, Y_pred)
    precision = precision_score(Y_test, Y_pred)
    recall = recall_score(Y_test, Y_pred)
    f1 = f1_score(Y_test, Y_pred)
    cm = confusion_matrix(Y_test, Y_pred)

    print("Accuracy  :", accuracy)
    print("Precision :", precision)
    print("Recall    :", recall)
    print("F1 Score  :", f1)
    print("Confusion Matrix :")
    print(cm)

    results.append([name, accuracy, precision, recall, f1])

# --------------------------------------------------
# Step 11 : Final Comparison Table
# --------------------------------------------------
print(border)
print("Step 11 : Final Comparison Table")
print(border)

result_df = pd.DataFrame(
    results,
    columns=["Algorithm", "Accuracy", "Precision", "Recall", "F1 Score"]
)

print(result_df)
print(border)