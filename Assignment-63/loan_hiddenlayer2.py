#------------------------------------------------
# Step 1 : Import the Libraries
#-----------------------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network  import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix,precision_score,classification_report,recall_score,f1_score
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import log_loss

#------------------------------------------------
# Step 2 : Load the dataset
#-----------------------------------------------
df = pd.read_csv("Customer_Loan_Approval (1).csv")
print("Display 5 rows:")
print(df.head())

print("Display shape:")
print(df.shape)

print("Coumn names:")
print(df.columns)

print("--------------------------------------------------------------------")

#------------------------------------------------
# Step 3 : Data Analysis
#-----------------------------------------------

print("Check missing values:")
print(df.isnull().sum())


print("--------------------------------------------------------------------")

#------------------------------------------------
# Step 4 : Preprocessing
#-----------------------------------------------
print("Seprate the Features:")
X = df.drop(['LoanApproved'],axis=1)
print("Features:",X.shape)

print("Label:")
Y = df["LoanApproved"]
print("Label:",Y.shape)

print("--------------------------------------------------------------------")

#------------------------------------------------
# Step 5 : Apply Train-Test-Split
#-----------------------------------------------
print("Apply Train test split method")
X_train,X_test,Y_train,Y_test = train_test_split(
                                       X,
                                       Y,
                                       test_size=0.30,
                                       random_state=42
)

print("Shape of Training X_train:",X_train.shape)
print("Shape of Testing X_test:",X_test.shape)

print("Shape of Training Y_train:",Y_train.shape)
print("Shape of Testing Y_test:",Y_test.shape)

print("--------------------------------------------------------------------")

#------------------------------------------------
# Step 5 : Apply stndard scaler
#-----------------------------------------------
print("Apply standard scaler:")

scaler = StandardScaler()
X_train_scale = scaler.fit_transform(X_train)
X_test_scale = scaler.transform(X_test)

print("Scaled trained data:")
print(X_test_scale[:5])

print("--------------------------------------------------------------------")

#------------------------------------------------
# Step 6 : Design a MLP model 
#-----------------------------------------------

print("Design a MLP Model:")

model = MLPClassifier(
    hidden_layer_sizes=(20,10),
    activation='relu',
    solver='adam',
    max_iter=1000,
    random_state=42
)

print(model)

print("Train the model:")

model.fit(X_train_scale,Y_train)

print("Model Traning completed")

print("--------------------------------------------------------------------")

#------------------------------------------------
# Step 7 : Model Evaluation
#-----------------------------------------------

print("Model Evaluation:")

Y_pred = model.predict(X_test_scale)

Accuracy = accuracy_score(Y_test,Y_pred)
print("Accuracy is :",Accuracy*100)

confusion = confusion_matrix(Y_test,Y_pred)
print("Confusion matrix:")
print(confusion)

classificationreport = classification_report(Y_test,Y_pred)
print(classificationreport)

print("Precision is:")
precision = precision_score(Y_test,Y_pred)
print(precision)

print("Recall is:")
recall = recall_score(Y_test,Y_pred)
print(recall)

print("F1 score is:")
f1 = f1_score(Y_test,Y_pred)
print(f1)


print("--------------------------------------------------------------------")







