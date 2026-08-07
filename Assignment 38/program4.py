import pandas as pd

################################################################################
#  Distribution of FinalResult
################################################################################

Border = "-"*50

df = pd.read_csv("student_performance_ml.csv")

print(Border)
print("Distribution of FinalResult")
print(Border)

total = len(df)

passed = (df["FinalResult"] == 1).sum()
failed = (df["FinalResult"] == 0).sum()

print("Passed :", passed)
print("Failed :", failed)

print("Pass Percentage :", (passed/total)*100)
print("Fail Percentage :", (failed/total)*100)