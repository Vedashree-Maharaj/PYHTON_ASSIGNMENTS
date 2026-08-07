import matplotlib.pyplot as plt
import pandas as pd

################################################################################
# Histogram of StudyHours
################################################################################

Border = "-"*50

df = pd.read_csv("student_performance_ml.csv")

print(Border)
print("Histogram of StudyHours ")
print(Border)
plt.hist(df["StudyHours"], bins=10) 

plt.title("Histogram of Study Hours")
plt.xlabel("Study Hours")
plt.ylabel("Number of Students")

plt.show()