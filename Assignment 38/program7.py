import pandas as pd
import matplotlib.pyplot as plt

################################################################################
# Scatter Plot (StudyHours vs PreviousScore)
################################################################################

Border = "-"*50

df = pd.read_csv("student_performance_ml.csv")

print(Border)
print("Scatter Plot (StudyHours vs PreviousScore) ")
print(Border)

# Separate pass and fail students
passed = df[df["FinalResult"] == 1]
failed = df[df["FinalResult"] == 0]

plt.figure(figsize=(7,5))

plt.scatter(passed["StudyHours"], passed["PreviousScore"],
            color="green", label="Pass")

plt.scatter(failed["StudyHours"], failed["PreviousScore"],
            color="red", label="Fail")

plt.title("StudyHours vs PreviousScore")
plt.xlabel("Study Hours")
plt.ylabel("Previous Score")

plt.legend()
plt.grid()
plt.show()