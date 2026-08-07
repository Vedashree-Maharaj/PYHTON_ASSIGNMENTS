import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
     ConfusionMatrixDisplay,
)

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

############################################################################
# predict result for X test
############################################################################

print(Border)
print("predict result for X test")
print(Border)  

Y_pred = model.predict(X_test)

print("Predicted Values")
print(Y_pred)

############################################################################
# Calculate accuracy and print percentage
############################################################################

print(Border)
print("Calculate accuracy and print percentage")
print(Border)  

accuracy = accuracy_score(Y_test,Y_pred)
print("Accuracy of model is :",accuracy*100)

############################################################################
# Confusion matrix
############################################################################

print(Border)
print("Confusion matrix")
print(Border)  

cm = confusion_matrix(Y_test, Y_pred)

disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()

plt.show()

print("\nConfusion Matrix")
print(cm)

print("\nTrue Negative :", cm[0][0])
print("False Positive :", cm[0][1])
print("False Negative :", cm[1][0])
print("True Positive :", cm[1][1])
