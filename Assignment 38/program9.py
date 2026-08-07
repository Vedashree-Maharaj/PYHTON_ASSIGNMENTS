import matplotlib.pyplot as plt
import pandas as pd

################################################################################
# Relationship between AssignmentsCompleted and FinalRes
################################################################################

Border = "-"*50

df = pd.read_csv("student_performance_ml.csv")

print(Border)
print("Scatter Plot (StudyHours vs PreviousScore) ")
print(Border)

plt.scatter(df["AssignmentsCompleted"], df["FinalResult"])

plt.title("Assignments Completed vs Final Result")
plt.xlabel("Assignments Completed")
plt.ylabel("Final Result")

plt.show()