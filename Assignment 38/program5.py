import pandas as pd

################################################################################
# Analysis
################################################################################

Border = "-"*50

df = pd.read_csv("student_performance_ml.csv")

print(Border)
print("Analysis")
print(Border)

print(df.groupby("FinalResult")[["StudyHours", "Attendance"]].mean())

