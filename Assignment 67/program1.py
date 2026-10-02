import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score,confusion_matrix

border = "-"*50

# ---------------------------------------------------
# Step 1: Create or Load the dataset
# ---------------------------------------------------
print(" 1: Create the dataset")
print(border)

X = np.array([
    [25, 500, 12, 1, 2],
    [30, 700, 24, 0, 1],
    [45, 1200, 6, 5, 8],
    [50, 1500, 5, 6, 10],
    [28, 600, 18, 1, 1],
    [35, 800, 30, 0, 0],
    [48, 1400, 4, 7, 9],
    [52, 1600, 3, 8, 12],
    [27, 550, 20, 0, 1],
    [42, 1300, 8, 4, 7]
])

Y = np.array([
    0, 0, 1, 1, 0,
    0, 1, 1, 0, 1
])

print("Input Features:")
print(X)

print("Labels :")
print(Y)

print(border)

#---------------------------------------------------------------------
# Step 2 : Clean the dataset
#---------------------------------------------------------------------
print("2 : Clean the dataset")
print(border)

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.30,
    random_state=42
)

print("Training Input Shape :", X_train.shape)
print("Testing Input Shape :", X_test.shape)
print("Training Output Shape :", Y_train.shape)
print("Testing Output Shape :", Y_test.shape)

print(border)

#---------------------------------------------------------------------
# Step 3 : Feature Scaling
#---------------------------------------------------------------------
print("3 : Feature Scaling")
print(border)

scalar = StandardScaler()

X_train_scaled = scalar.fit_transform(X_train)
X_test_scaled = scalar.transform(X_test)

print("Scaled Training Data :")
print(X_train_scaled[:5])

print(border)

#---------------------------------------------------------------------
# Step 4 : FNN Model Training
#---------------------------------------------------------------------
print("4 : FNN Model Training")
print(border)

model = MLPClassifier(
    hidden_layer_sizes=(8,4),
    activation='relu',
    solver='adam',
    max_iter=1000,
    random_state=42
)

print(model)

print("Train the model")

model = model.fit(X_train_scaled, Y_train)

print("Model Training Completed")

print(border)

#---------------------------------------------------------------------
# Step 5 : Model Evaluation
#---------------------------------------------------------------------
print("5 : Model Evaluation")
print(border)

Y_pred = model.predict(X_test_scaled)

accuracy = accuracy_score(Y_test, Y_pred)

print("Accuracy is :", accuracy)

cm = confusion_matrix(Y_test, Y_pred)

print("Confusion matrix :")
print(cm)

print("Predict the probability")

Y_prob = model.predict_proba(X_test_scaled)

print(Y_prob[:5])

print(border)

#---------------------------------------------------------------------
# Step 6 : Final Prediction
#---------------------------------------------------------------------
print("6 : Final Prediction")
print(border)

new_customer = [[46,1450,5,6,9]]

new_customer_scaled = scalar.transform(new_customer)

final_prediction = model.predict(new_customer_scaled)

new_customer_prob = model.predict_proba(new_customer_scaled)

print("Prediction Probability:")
print(new_customer_prob)

prob = new_customer_prob[0][1]

print("Probability of Customer may leave :", prob)

if prob >= 0.5:
    print("Prediction : Customer may leave")
else:
    print("Prediction : Customer will stay")

print(border)