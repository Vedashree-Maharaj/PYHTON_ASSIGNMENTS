Actualvalues = [1,1,1,1,0,0,0,0]
PredictedValues = [1,1,0,1,0,1,0,0]

TP = TN = FP = FN = 0

for i in range(len(Actualvalues)):
    actual = Actualvalues[i]
    pred = PredictedValues[i]

    if actual == 1 and pred == 1:
        TP += 1
    elif actual == 0 and pred == 0:
        TN += 1
    elif actual == 0 and pred == 1:
        FP += 1
    elif actual == 1 and pred == 0:
        FN += 1

Accuracy = (TP + TN)/(TP+TN+FP+FN)  
precision = TP / (TP+FP)
recall = TP / (TP+FN)
F1_Score = (2 * precision * recall) / (precision + recall)

print("True Positives:", TP)
print("True Negatives:", TN)
print("False Positives:", FP)
print("False Negatives:", FN)

print("Accuracy is:",Accuracy)
print("Precision is:",precision)
print("Recall is:",recall)
print("F1 score is:",F1_Score)

