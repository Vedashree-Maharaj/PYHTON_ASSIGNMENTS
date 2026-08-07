import matplotlib.pyplot as plt
import pandas as pd

################################################################################
# SleepHours vs FinalResult
################################################################################

Border = "-"*50

df = pd.read_csv("student_performance_ml.csv")

print(Border)
print("SleepHours vs FinalResult")
print(Border)

plt.scatter(df["SleepHours"], df["FinalResult"])

plt.title("Sleep Hours vs Final Result")
plt.xlabel("Sleep Hours")
plt.ylabel("Final Result")

plt.show()