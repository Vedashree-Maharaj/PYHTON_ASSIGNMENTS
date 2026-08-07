import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split


Border = "-"*50

############################################################################
# Load Dataset
############################################################################

df = pd.read_csv("student_performance_ml.csv")

print(Border)
print("Load Dataset")
print(Border)

############################################################################
# Prepare Data
############################################################################

print(Border)
print("Prepare data")
print(Border)

X = df[["StudyHours","Attendance","PreviousScore",
        "AssignmentsCompleted","SleepHours"]]

Y = df["FinalResult"]

############################################################################
# Train-Test Split
############################################################################

print(Border)
print("Train-Test Split")
print(Border)

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42)

############################################################################
# Train model
############################################################################

print(Border)
print("Train model")
print(Border)

model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, Y_train)