import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.ensemble import VotingClassifier

border = "-" * 50

# --------------------------------------------------
# Step 1 : Load the Dataset
# --------------------------------------------------
print(border)
print("Step 1 : Load the Dataset")
print(border)

df = pd.read_csv("Customer_Loan_Approval.csv")
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

X = df.drop("LoanApproved", axis=1)
Y = df["LoanApproved"]

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
    test_size=0.3,
    random_state=42,
    stratify=Y
)

print("Shape of X_train :", X_train.shape)
print("Shape of X_test  :", X_test.shape)
print("Shape of Y_train :", Y_train.shape)
print("Shape of Y_test  :", Y_test.shape)

# --------------------------------------------------
# Step 5 : Feature Scaling
# --------------------------------------------------
print(border)
print("Step 5 : Feature Scaling")
print(border)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

print("Feature Scaling Completed Successfully!")

# --------------------------------------------------
# Step 6 : Train Logistic Regression Model
# --------------------------------------------------
print(border)
print("Step 6 : Train Logistic Regression Model")
print(border)

Lmodel = LogisticRegression(max_iter=1000, C=0.5)
Lmodel.fit(X_train, Y_train)

print("Logistic Regression Model Trained Successfully!")

# --------------------------------------------------
# Step 7 : Train Decision Tree Model
# --------------------------------------------------
print(border)
print("Step 7 : Train Decision Tree Model")
print(border)

Dmodel = DecisionTreeClassifier(max_depth=4, random_state=42)
Dmodel.fit(X_train, Y_train)

print("Decision Tree Model Trained Successfully!")

# --------------------------------------------------
# Step 8 : Train K-Nearest Neighbors Model
# --------------------------------------------------
print(border)
print("Step 8 : Train K-Nearest Neighbors Model")
print(border)

Kmodel = KNeighborsClassifier(n_neighbors=3)
Kmodel.fit(X_train, Y_train)

print("KNN Model Trained Successfully!")

# --------------------------------------------------
# Step 9 : Accuracy of Individual Models
# --------------------------------------------------
print(border)
print("Step 9 : Accuracy of Individual Models")
print(border)

# Logistic Regression Accuracy
L_accuracy = accuracy_score(Y_test, Lmodel.predict(X_test))
print("Logistic Regression Accuracy :", L_accuracy)

print(border)

# Decision Tree Accuracy
D_accuracy = accuracy_score(Y_test, Dmodel.predict(X_test))
print("Decision Tree Accuracy       :", D_accuracy)

print(border)

# KNN Accuracy
K_accuracy = accuracy_score(Y_test, Kmodel.predict(X_test))
print("KNN Accuracy                 :", K_accuracy)

# --------------------------------------------------
# Step 10 : Hard Voting Classifier
# --------------------------------------------------
print(border)
print("Step 10 : Hard Voting Classifier")
print(border)

Hmodel = VotingClassifier(
    estimators=[
        ("logistic", Lmodel),
        ("decision_tree", Dmodel),
        ("knn", Kmodel)
    ],
    voting="hard"
)

Hmodel.fit(X_train, Y_train)

H_accuracy = accuracy_score(Y_test, Hmodel.predict(X_test))
print("Hard Voting Accuracy :", H_accuracy)

# --------------------------------------------------
# Step 11 : Soft Voting Classifier
# --------------------------------------------------
print(border)
print("Step 11 : Soft Voting Classifier")
print(border)

Smodel = VotingClassifier(
    estimators=[
        ("logistic", Lmodel),
        ("decision_tree", Dmodel),
        ("knn", Kmodel)
    ],
    voting="soft"
)

Smodel.fit(X_train, Y_train)

S_accuracy = accuracy_score(Y_test, Smodel.predict(X_test))
print("Soft Voting Accuracy :", S_accuracy)

# --------------------------------------------------
# Step 12 : Final Accuracy Comparison
# --------------------------------------------------
print(border)
print("Step 12 : Final Accuracy Comparison")
print(border)

print("Logistic Regression Accuracy :", L_accuracy)
print("Decision Tree Accuracy       :", D_accuracy)
print("KNN Accuracy                 :", K_accuracy)
print("Hard Voting Accuracy         :", H_accuracy)
print("Soft Voting Accuracy         :", S_accuracy)

print(border)