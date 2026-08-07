import matplotlib.pyplot as plt
import pandas as pd

################################################################################
# Boxplot of Attendance
#################################################################################

Border = "-"*50

df = pd.read_csv("student_performance_ml.csv")

print(Border)
print("Boxplot of Attendance")
print(Border)

plt.boxplot(df["Attendance"])

plt.title("Attendance Boxplot")
plt.ylabel("Attendance")

plt.show()