import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

border = "-"*70

data = {
  
    'Name':['Amit','Sagar','Pooja'],
    'Math':[85,90,78],
    'Science':[92,88,80],
    'English':[75,85,82]
  
}
####################################################################
#print the dataframe
print(border)
df = pd.DataFrame(data)
print("Data Frame:")
print(df)
print(border)
##################################################################
# Print The Shape
##################################################################
print("Shape of Data:")
print(df.shape)
print(border)
print("Shape of Column:")
print(df.columns)
print(border)
print("Datatypes of Data")
print(type(df))
print(border)
################################################################################

print("Describe the data:")
print(df.describe())
print(border)
#####################################################################

df['Total'] = [252,260,242]
print(border)
print("Add new total column into dataframe")
print(df)
print(border)
##############################################################################

print("Print the score who got more than 85 score in science")
for i in df['Science']:
  if i > 85:
   print("More than 85 score in science",i)
print(border)
##############################################################################

print("Replace Pooja to pooja")
df['Name'] = df['Name'].replace('Pooja','pooja')
print(df)
print(border)

########################################################################

print("Print Total column Values in Decending order:")
df = df.sort_values("Total",ascending=False)
print(df)

print(border)
#########################################################################

print("Bar Plot Name vs Total Marks")
plt.bar(df['Name'],df['Total'])
plt.xlabel("Name")
plt.ylabel("Total marks")
plt.title("Student Records")

plt.show()
print(border)

################################################################

print("Line charts of marks for amit across all sub:")

amit = df[df["Name"] == "Amit"]

subjects = ["Math", "Science", "English"]

marks = [
    amit["Math"].iloc[0],
    amit["Science"].iloc[0],
    amit["English"].iloc[0]
]

plt.plot(subjects, marks)

plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Amit's Marks")

plt.show()
print(border)
#################################################################3

print("Create data frame with missing values and fill them with column mean")
data2 = {
  'Name':['Amit','Sagar','Pooja'],
  'Math':[None,90,78],
  'Science':[92,None,80],

}

df2 = pd.DataFrame(data2)

print(df2)
print(border)

print("Values filled using np.mean()")

df2["Science"] = df2["Science"].fillna(np.mean(df2["Science"]))
df2["Math"] = df2["Math"].fillna(np.mean(df2["Math"]))

print(df2)
print(border)

################################################################

print("Drop the English column from original DataFrame")

df = df.drop("English",axis=1)

print(df)
