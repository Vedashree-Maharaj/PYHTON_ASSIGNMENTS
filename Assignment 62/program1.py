#------------------------------------------------
# Step 1 : Import the Libraries
#------------------------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

#------------------------------------------------
# Step 2 : Load the Dataset
#------------------------------------------------
df = pd.read_csv("Employee_Attrition.csv")

print("First 5 Records:")
print(df.head())

print("\nShape of Dataset:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("------------------------------------------------")

#------------------------------------------------
# Step 3 : Data Analysis
#------------------------------------------------
print("Missing Values:")
print(df.isnull().sum())

print("\nCategorical Columns:")
categorical_cols = df.select_dtypes(include=['object', 'string', 'category']).columns
print(categorical_cols)

print("\nNumerical Columns:")
numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
print(numerical_cols)

print("------------------------------------------------")

#------------------------------------------------
# Step 4 : Label Encoding
#------------------------------------------------
print("Label Encoding Categorical Columns:")

le = LabelEncoder()

for col in categorical_cols:
    df[col] = le.fit_transform(df[col])

print(df.head())

print("------------------------------------------------")

#------------------------------------------------
# Step 5 : Separate Features and Target
#------------------------------------------------
print("Separate Independent and Dependent Variables")

X = df.drop("Attrition", axis=1)
Y = df["Attrition"]

print("Features Shape:", X.shape)
print("Target Shape:", Y.shape)

print("------------------------------------------------")

#------------------------------------------------
# Step 6 : Train-Test Split
#------------------------------------------------
print("Train Test Split")

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.30,
    random_state=42
)

print("X_train Shape :", X_train.shape)
print("X_test Shape  :", X_test.shape)
print("Y_train Shape :", Y_train.shape)
print("Y_test Shape  :", Y_test.shape)

print("------------------------------------------------")

#------------------------------------------------
# Step 7 : Feature Scaling
#------------------------------------------------
print("Apply Feature Scaling")

scaler = StandardScaler()

X_train_scale = scaler.fit_transform(X_train)
X_test_scale = scaler.transform(X_test)

print("First 5 Scaled Records:")
print(X_train_scale[:5])

print("------------------------------------------------")

#------------------------------------------------
# Step 8 : Design MLP Classifier
#------------------------------------------------
print("Design MLP Model")

model = MLPClassifier(
    hidden_layer_sizes=(15, 4),     # Two Hidden Layers
    activation="relu",
    solver="adam",
    max_iter=1000,
    random_state=42
)

print(model)

print("------------------------------------------------")

#------------------------------------------------
# Step 9 : Train the Model
#------------------------------------------------
print("Training the Model...")

model.fit(X_train_scale, Y_train)

print("Model Training Completed.")

print("------------------------------------------------")

#------------------------------------------------
# Step 10 : Number of Iterations
#------------------------------------------------
print("Number of Iterations Required:")
print(model.n_iter_)

print("------------------------------------------------")

#------------------------------------------------
# Step 11 : Training Accuracy
#------------------------------------------------
train_prediction = model.predict(X_train_scale)
train_accuracy = accuracy_score(Y_train, train_prediction)

print("Training Accuracy : {:.2f}%".format(train_accuracy * 100))

print("------------------------------------------------")

#------------------------------------------------
# Step 12 : Testing Accuracy
#------------------------------------------------
test_prediction = model.predict(X_test_scale)
test_accuracy = accuracy_score(Y_test, test_prediction)

print("Testing Accuracy : {:.2f}%".format(test_accuracy * 100))

print("------------------------------------------------")

#------------------------------------------------
# Step 13 : Confusion Matrix
#------------------------------------------------
print("Confusion Matrix")

cm = confusion_matrix(Y_test, test_prediction)

print(cm)

print("------------------------------------------------")

#------------------------------------------------
# Step 14 : Plot Loss Curve
#------------------------------------------------
print("Loss Curve")

plt.figure(figsize=(7,5))
plt.plot(model.loss_curve_)
plt.title("MLP Classifier Loss Curve")
plt.xlabel("Iterations")
plt.ylabel("Loss")
plt.grid(True)
plt.show()

print("------------------------------------------------")

#------------------------------------------------
# Step 15 : Prediction Function
#------------------------------------------------
def PredictAttrition(employee_data):

    employee_scaled = scaler.transform(employee_data)

    prediction = model.predict(employee_scaled)
    probability = model.predict_proba(employee_scaled)

    print(employee_data)
    print("Prediction Probability:", probability)

    if prediction[0] == 1:
        print("Prediction : Employee is likely to Leave.")
    else:
        print("Prediction : Employee is likely to Stay.")

#------------------------------------------------
# Step 16 : Test New Employee Records
#------------------------------------------------
print("Prediction for New Employee 1")

new_employee1 = pd.DataFrame(
    [[41,60000,8,63,45,4,3,1,6,6]],
    columns=[
        "Age","MonthlyIncome","YearsAtCompany","TotalWorkingYears",
        "DistanceFromHome","JobSatisfaction","WorkLifeBalance",
        "OverTime","NumCompaniesWorked","TrainingTimesLastYear"
    ]
)

PredictAttrition(new_employee1)

print("------------------------------------------------")

print("Prediction for New Employee 2")

new_employee2 = pd.DataFrame(
    [[42,67304,6,15,44,2,1,1,4,6]],
    columns=[
        "Age","MonthlyIncome","YearsAtCompany","TotalWorkingYears",
        "DistanceFromHome","JobSatisfaction","WorkLifeBalance",
        "OverTime","NumCompaniesWorked","TrainingTimesLastYear"
    ]
)

PredictAttrition(new_employee2)

print("------------------------------------------------")

#------------------------------------------------
# Step 17 : Test Last Five Employee Records
#------------------------------------------------
print("Last Five Employee Records Prediction")

last_five = df.tail(5)

X_last = last_five.drop("Attrition", axis=1)
Y_last = last_five["Attrition"]

X_last_scale = scaler.transform(X_last)

last_prediction = model.predict(X_last_scale)

result = X_last.copy()
result["Actual"] = Y_last.values
result["Predicted"] = last_prediction

print(result)

print("------------------------------------------------")

#------------------------------------------------
# Step 18 : Model Performance Analysis
#------------------------------------------------
print("Model Performance Analysis")

difference = train_accuracy - test_accuracy

if difference > 0.10:
    print("The model is suffering from Overfitting.")
elif difference < -0.05:
    print("The model is suffering from Underfitting.")
else:
    print("The model is well fitted.")

print("------------------------------------------------")

#------------------------------------------------
# Step 19 : Final Summary
#------------------------------------------------
print("Final Result")
print("Training Accuracy : {:.2f}%".format(train_accuracy * 100))
print("Testing Accuracy  : {:.2f}%".format(test_accuracy * 100))
print("Iterations Used   :", model.n_iter_)