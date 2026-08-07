import pandas as pd

################################################################################
# Basic Information of Dataset
################################################################################

Border = "-"*50

df = pd.read_csv("student_performance_ml.csv")

print(Border)
print("Basic Information of Dataset")
print(Border)

print("First 5 Records:")
print(df.head())  # Display first 5 records

print("Last 5 Records:")
print(df.tail())  # Display last 5 records

print("\nTotal Rows and Columns:")
print(df.shape) # Display total number of rows and columns

print("\n Column names :")
print(list(df.columns))  # Display list of column names

print("\nData Types of Each Column:")
print(df.dtypes)  # Display data types of each column
