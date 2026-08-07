import pandas as pd

################################################################################
# Total students, Passed and Failed
################################################################################

Border = "-"*50

df = pd.read_csv("student_performance_ml.csv")

print(Border)
print("Total students, Passed and Failed")
print(Border)

# Total students
print("Total Students :", len(df))

# Passed students
print("Passed Students :", (df["FinalResult"] == 1).sum())

# Failed students
print("Failed Students :", (df["FinalResult"] == 0).sum())